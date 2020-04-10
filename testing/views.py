#!python3
# Inclusion of js files in testing now works in the following way:
#
# In functions.py, question has attribute "js", if "js"=="y", testing includes static/js/{{question.idd}}.js file, that includes js content present on page (see first pages with plots for q and p)
# If there is no "js" attribute set, it tries to load image, if there is no image, it just renders the answers
# There are two empy divs on the page, "content1" and "content2", that can be filled with any content using js (this can make tables/pictures dynamic)

import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from dAuction2.settings import UNIQUEIZER
from api.serializers import sTreatmentSerializer, sVSerializer
from forward_and_spot.models import Voucher, Player, Auction, Treatment
from master.models import MasterMan
from testing.models import Question, Option_MC, Player_Questions, Player_Question_Options
log = logging.getLogger(__name__)


@login_required(redirect_field_name="login_user", login_url='master-login_user')
def main(request, tmpl='testing/testing.html', data={}):
    # print("SUBJECT ON the main of testing")
    # print(request)
    auction, treatment = Auction.cache_or_create_auction()
    # auction = Auction.cache_get()
    if not auction:
        auction = Auction.objects.get(active=True)
    if not auction.app == Auction.TESTING:
        return redirect('master-main')
    if request.user.username == 'admin':
        raise ValueError('Admin got into testing')
    else:
        if not hasattr(request.user, 'player'):
            raise ValueError('PLayer doesnt exist!!!')
    user = request.user
    player = user.player.get(auction=auction)
    log.info("landed on main, user:{}, playerid:{}, group:{}".format(user, player, player.group))


    if auction.removing and not player.selected:
        return redirect('master-main')

    if player.app != Player.TEST:
        player.TEST_app()
    if request.POST:
        if "Next" in request.POST:
            question = Question.objects.get(id=player.page + (auction.id * UNIQUEIZER))
            player_question = Player_Questions.objects.get(player=player, question=question)
            if player_question.finished and player.page < auction.testing_totalquestions:
                player.page += 1
        elif "Previous" in request.POST:
            # print("Previous!!!")
            if player.page > 1:
                player.page -= 1
        elif "Finish" in request.POST:
            player.testing_finished = True
            player.state=3
            player.save(update_fields=['testing_finished','state'])
        elif "value" in request.POST:
            i = int(request.POST["value"])
            player.page = i
            player.save(update_fields=['page'])
            # print("iii:{}".format(i))

    elif request.GET:
        if "option_id" in request.GET:
            option_id = (request.GET.get('option_id', None))
            if option_id:
                option_id = int(option_id)
                # print("option_id:{}".format(option_id))
            else:
                return redirect('testing-main')
        else:
            return redirect('testing-main')
        log.info("player_page:{}".format(player.page))
        question = Question.objects.get(id=player.page + (auction.id * UNIQUEIZER))
        player_question = Player_Questions.objects.get(player=player, question=question)
        option_chosen = Option_MC.objects.get(question=player_question.question, idd=option_id)
        pqo = Player_Question_Options.objects.get(player_question=player_question, option=option_chosen)
        if not option_chosen.correct and not pqo.reveal and not player_question.finished:
            player.testing_errors += 1
        elif option_chosen.correct:
            if not player_question.finished:
                player.testing_correct += 1
            if player_question.question.id - (auction.id * UNIQUEIZER) == auction.testing_totalquestions:
                player.testing_finished = True
                player.state = 3
                player.save(update_fields=['testing_finished', 'state'])
        pqo.reveal = True
        pqo.save()
        if not player_question.finished:
            player_question.trials += 1
            player.testing_trials += 1
        player_question.finished = player_question.finished or (option_chosen.correct == True)
        player_question.save()
        player.page = (player_question.question.id  - (auction.id * UNIQUEIZER))
    player.save()
    # print("player:{}".format(player))
    # print("player.page:{}".format(player.page))
    question = Question.objects.get(id=player.page + (auction.id * UNIQUEIZER))
    pq_list = Player_Questions.objects.filter(player=player).order_by('pk').select_related('question')
    player_question = pq_list.get(question=question)
    # print("player_question :{}".format(player_question ))
    option_correct = Option_MC.objects.get(question=player_question.question, correct=True)
    option_list = Option_MC.objects.filter(question=player_question.question)
    player_list = Player.objects.filter(auction=auction)
    pqo_list = Player_Question_Options.objects.filter(player_question=player_question).order_by('ord').select_related(
            'option')
    if not player_question.pqo_init:
        for option in option_list:
            player_question_option = Player_Question_Options(player_question=player_question, option=option)
            player_question_option.save()
        player_question.pqo_init = True
        # dynamically adds options to questions :)
        player_question.save()

    # in testmode allow browsing through questions without checking
    # print("pq_list :{}".format(pq_list))
    # for pq in pq_list:
    #     print("pq:{}".format(pq.id))
    auction, treatment = Auction.cache_or_create_auction()
    if not treatment.test_mode:
        end = pq_list.filter(finished=True).count() + 1
        if player_question.finished:
            end = max(end, player.page + 1)
        else:
            end = max(end, player.page)
        pq_list = pq_list.filter(question__id__range=[(auction.id * UNIQUEIZER) ,  end+ (auction.id* UNIQUEIZER)])
        log.info("end:{}, pq_list:{} for user:{}, player:{}".format(end, pq_list, user,player))

    # for pq in pq_list:
    #     print("pq2:{}".format(pq.id-(auction.id * UNIQUEIZER)))
    # print("pq_list :{}".format(pq_list))
    voucher_list = cache.get('voucher_list')
    if not voucher_list:
        voucher_list = Voucher.objects.filter(auction=auction)
        MasterMan.cache_it('voucher_list', voucher_list)
    tmpl = 'testing/testing.html'
    # print("pq_list :{}".format(pq_list))
    data = {'pq_list': pq_list,
            'players': player_list,
            'player': player,
            "auction": auction,
            'player_question': player_question,
            'option_list': option_list,
            'pqo_list': pqo_list,
            'option_correct': option_correct,
            # 'treatment': sTreatmentSerializer(treatment).data,
            'treatment_js': sTreatmentSerializer(treatment).data,
            "auction_js": sTreatmentSerializer(treatment).data,
            "vouchers_js": sVSerializer(voucher_list, many=True).data}
    return render(request, tmpl, context=data)