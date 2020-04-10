#!python3
from django.shortcuts import render, render_to_response
# from django.http import HttpResponse, JsonResponse
## imports for user login
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.decorators import login_required
from forward_and_spot.models import Auction,Treatment
from forward_and_spot.models import Player
from questionnaire.forms import QuestionnaireForm, QuestionnaireIdForm
from django.core.cache import cache
from payout.functions import determine_payment, auction_pay_removed
import logging
from django.views.decorators.csrf import csrf_exempt
from master.models import MasterMan

log = logging.getLogger(__name__)

@csrf_exempt
@login_required(redirect_field_name="login", login_url='master-login_user')
def main(request, tmpl='questionnaire/questionnaire.html', data={}):
    log.info("SUBJECT ON the main of questionnaire 1")
    if not Auction.objects.exists():
        raise ValueError('Auction doesnt exist')
    auction, treatment = Auction.cache_or_create_auction()
    if auction.app !=Auction.QUEST and auction.app!= Auction.AUCTION:
        if not auction.removing:
            return redirect('master-main')

    # # auction = Auction.objects.get_or_create(pk=1)[0]
    # treatment=Treatment.objects.get(active=True)
    # auction = Auction.objects.get(active=True)
    user = request.user
    log.info("SUBJECT ON the main of questionnaire 2")
    if not hasattr(request.user, 'player'):
        raise ValueError('PLayer doesnt exist!!!')
    elif user.id==99:
        raise ValueError('Admin in Questionairre!!!')
    else:
        try:
            player = user.player.get(auction=auction)
        except:
            # print("SUBJECT ON the main of questionnaire- but cant get player!!!")
            # print("Player matching query does not exist")
            # print("auction: {}".format(auction))
            # print("user: {}".format(user))
            log_string = "SUBJECT ON the main of questionnaire- but cant get player!!!. Player matching query does not exist. auction: {}, user: {}".format(auction,user)
            wait_key = 'wait_four_seconds{}'.format(user.id)
            wait_four_seconds = cache.get(wait_key)
            if not wait_four_seconds:
                cache.set(wait_key, 'True', 4)
                return redirect('instructions-main')
            else:

                render(request, tmpl, context=data)
    log.info("landed on main, user:{}, playerid:{}, group:{}".format(user, player, player.group))
    log.info("SUBJECT ON the main of questionnaire 3")
    if not auction.app == Auction.QUEST  and (not auction.removing or player.selected):
            return redirect('instructions-main')
    log.info("SUBJECT ON the main of questionnaire 4")
    player.QUEST_app()
    # player.save()

    data ={}
    if player.selected:
        determine_payment(treatment,auction,player)
        auction = auction.determine_payment_statistics()
        auction.save_and_cache()
        # MasterMan.cache_me('auction', auction)
    else:
        if auction.removing:
            data = auction_pay_removed(request, treatment, auction, player)
    player.payout_CZK_corr= player.get_payout_CZK_corr()
    player.save()
            # return render(request, 'payout/main.html', context=data)
    log.info("SUBJECT after determine_payment")
    form = QuestionnaireIdForm
    group_id=player.group_id
    data.update({"treatment":treatment,"auction":auction,"form":form, "player":player,"user":user, "group_id":group_id, 'message_kind_request':'Please, fill out your details', 'message_kind_request_explanation':'We need this information only for the payment receipt so we can pay you your earnings from the experiment.'})
    # data = {"auction": auction, "form": form, "player": player, "user": user,
    #         "group_id": group_id}
    return render(request, tmpl, context=data)


# @csrf_exempt
# @login_required(redirect_field_name="login", login_url='master-login_user')
# def questionnaire_save(request, tmpl='questionnaire/questionnaire.html', data={}):
#     auction, treatment = Auction.cache_or_create_auction()
#     log.info("questionnaire_save")
#     print("questionnaire_save")
#     user = request.user
#     player=user.player.get(auction=auction)
#     form = QuestionnaireForm(request.POST or None, instance=player)
#     print("player:{}".format(player))
#     if form.is_valid():
#         # print("if form.is_valid():")
#         form.save()
#         log.info("send to payout-main!!!!")
#         player.PAYOUT_app()
#         return redirect('payout-main')
#     print("end without anything")
#     return render_to_response(tmpl, {'form': form})

@csrf_exempt
@login_required(redirect_field_name="login", login_url='master-login_user')
def questionnaire_save(request, tmpl='questionnaire/questionnaire.html', data={}):
    auction, treatment = Auction.cache_or_create_auction()
    if auction.app != Auction.QUEST and auction.app != Auction.AUCTION:
        if not auction.removing:
            return redirect('master-main')

    log.info("questionnaire_save")
    # print("questionnaire_save")
    user = request.user
    player= user.player.get(auction=auction)
    # print("request_POST:{}".format(request.POST))
    if 'first_name' in request.POST:
        form = QuestionnaireIdForm(request.POST or None, instance=player)
    else:
        form = QuestionnaireForm(request.POST or None, instance=player)
    # print("player:{}".format(player))
    if form.is_valid():
        # print("if form.is_valid():")
        form.save()
        form = QuestionnaireForm
        group_id = player.group_id
        data = {"treatment": treatment, "auction": auction, "form": form, "player": player, "user": user,
                "group_id": group_id,
                'message_kind_request': 'Please, fill out the questionnaire',
                'message_kind_request_explanation': 'Your answers have no influence on your earnings and are only used for the data analysis of this specific project.'}



        if 'first_name' in request.POST:
            return render(request, tmpl, context=data)
        else:
            log.info("send to payout-main!!!!")
            player.PAYOUT_app()
            return redirect('payout-main')
            return render(request, tmpl, context=data)

    # print("send_back_to_form")
    return render_to_response(tmpl, {'form': form})