#!python3
import logging, time

# import pandas as pd
import glob
# from master.models import MasterMan
from django.db.models import Sum
log = logging.getLogger(__name__)
from django.shortcuts import render
# from django.core.cache import cache
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django_bulk_update.helper import bulk_update
from .forms_earnings import AuctionCorrectionForm
from django.db import transaction
from master_data.functions import get_my_model_fields,  csv_print
from master.functions import Round
from django.db.models import Avg

from forward_and_spot.models import Auction, Treatment
from forward_and_spot.models import Player
from testing.models import Player_Questions
from master.models import MasterMan


logger = logging.getLogger(__name__)
debug_logger = logging.getLogger('debug_logger')


@login_required(redirect_field_name="login", login_url='master-login_user')
@transaction.atomic
def payment_data_handle(request, tmpl='master-main', data={}):
    # print("on_payment_data_handle")
    if request.POST:
        start = time.time()
        log.info("POST---{}".format(request.POST))
        # treatment = Treatment.cache_or_create_treatment()
        auction, treatment = Auction.cache_or_create_auction()
        # print("payment_sheet before")
        master_man = MasterMan.cache_or_create_mm()

        # does all toggling of master_man object
        master_man.toggler(request.POST)

        if 'export_payment_file' in request.POST or 'export_payment_file_all' in request.POST  :
            # print("export_payment_file")
            # filename_csv = "{}.cvs".format(filename)
            # log.info("excel_csv")
            rows = []
            rows2 = []
            if 'export_payment_file' in request.POST:
                auction_list =[auction]
                filename_csv = "{}_ auction_ payment file.csv".format(auction.id)
                filename_short_csv = "{}_ summ_ auction_ payment file.csv".format(auction.id)
                # player_list = Player.objects.filter(auction=auction).all().select_related('user').order_by('auction','user__ip')
            else:
                auction_list = Auction.objects.all().order_by('-pk').select_related('treatment')
                filename_csv = "all_ auction_ payment file.csv".format(auction.id)
                filename_short_csv = "all_ summ_ auction_ payment file.csv".format(auction.id)
                # player_list = Player.objects.all().select_related('user').order_by('auction','user__ip')
            player_list = Player.objects.filter(auction=auction).select_related('user').order_by('auction', 'user__ip')
            field_name_list_player = ['auction','group', 'first_name', 'last_name', "payout_CZK_corr", "payout_CZK", "role",'pay_period', 'pay_qs_period', 'testing_finished', 'testing_errors', 'male', 'age']
            # empty_fields = False
            player = player_list.first()
            model_object = player
            fields_player = get_my_model_fields(model_object, field_name_list_player)

            field_name_list_user = ['ip']
            # empty_fields = False
            user = player.user
            model_object = user
            fields_user = get_my_model_fields(model_object, field_name_list_user)

            # for field in fields_user:
            for auction in auction_list:
                # row_elt = []
                row_elt = ["","", ]
                player_list = Player.objects.filter(auction=auction).select_related('user').order_by('auction', 'user__ip')
                for field in fields_user:
                    row_elt += ["us_" + field.name]
                for field in fields_player:
                    row_elt += ["pl_" + field.name]
                rows += [row_elt]

                for player in player_list:
                    # row_elt = []
                    row_elt = ["", "", ]
                    # for field in fields_user:
                    row_elt += [player.user.ip]
                    # print("player.user.ip:{}".format(player.user.ip))
                    for field in fields_player:
                        row_elt += [getattr(player, field.name)]
                    # print("row_elt:{}".format(row_elt))
                    rows += [row_elt]
                row_elt = []
                from django.db.models import Sum, Avg
                # print("-----{}".format(auction))
                # print("-----{}".format(Player.objects.filter(auction=auction).aggregate(Sum('earnings_CZK_corrected'))))
                # total_spend,avg_spend  = Player.objects.filter(auction=auction).aggregate(Sum('payout_CZK_corr'))['payout_CZK_corr__sum']
                # total_avg_list = Player.objects.filter(auction=auction).aggregate(Sum('payout_CZK_corr'),Avg('payout_CZK_corr')).values()
                total_avg_list = Player.objects.filter(auction=auction).aggregate(Sum('payout_CZK_corr'),Avg('payout_CZK_corr'))
                # print("total_avg_list:{}".format(total_avg_list ))
                total_spend = total_avg_list['payout_CZK_corr__sum']
                avg_spend = total_avg_list['payout_CZK_corr__avg']
                # avg_spend = Player.objects.filter(auction=auction).aggregate(Avg('payout_CZK_corr'))[
                #     'payout_CZK_corr__avg']

                total_avg_list_select = Player.objects.filter(auction=auction,selected=True).aggregate(Sum('payout_CZK_corr'),Avg('payout_CZK_corr'))
                total_spend_select = total_avg_list_select['payout_CZK_corr__sum']
                avg_spend_select = total_avg_list_select['payout_CZK_corr__avg']

                avg_spend_qs = Player.objects.filter(auction=auction,  selected=True).aggregate(
                    Avg('payout_qs'))['payout_qs__avg']
                # print("avg_spend_qs:{}".format(avg_spend_qs ))
                avg_spend_PR = Player.objects.filter(auction=auction, role=Player.PR, selected=True).aggregate(
                    Avg('payout_CZK_corr'))['payout_CZK_corr__avg']

                avg_spend_RE = Player.objects.filter(auction=auction, role=Player.RE, selected=True).aggregate(Avg('payout_CZK_corr'))['payout_CZK_corr__avg']

                # avg_spend_select = Player.objects.filter(auction=auction, selected=True).aggregate(Avg('payout_CZK_corr'))[
                #     'payout_CZK_corr__avg']
                # print("total_spend:{}".format(total_spend))
                row_elt = ["date","total_spend", "total_spend_select", "avg_spend", "avg_spend_select",
                           "avg_spend_PR",
                           "avg_spend_RE","avg_spend_qs",
                           "Treatment","Auction","multiplier","multiplier_PR", "multiplier_RE","fixed_uplift","fixed_uplift_PR","fixed_uplift_RE","ECU_per_CZK_PR","ECU_per_CZK_RE"]
                row_elt2 =row_elt
                rows += [row_elt]
                rows2 += [row_elt2]
                row_elt = ['{:%Y-%m-%d %H:%M}'.format(auction.created),
                           total_spend,
                           total_spend_select,
                           avg_spend,
                           avg_spend_select,
                           avg_spend_PR,
                           avg_spend_RE,
                           avg_spend_qs,
                           auction.treatment,auction.id,auction.multiplier,auction.multiplier_PR,auction.multiplier_RE,auction.fixed_uplift,auction.fixed_uplift_PR,auction.fixed_uplift_RE,
                           auction.treatment.ECU_per_CZK_PR, auction.treatment.ECU_per_CZK_RE ]
                for field in fields_player:
                    row_elt += ["", ]
                row_elt2 = row_elt
                rows += [row_elt]
                rows2 += [row_elt2]
                # rows += [total_spend, ]
                rows += ["",]
                rows += ["", ]
                rows += ["", ]
                # rows2 += ["", ]



            rows+=rows2
            response = csv_print(filename_csv, rows)
            end = time.time() - start
            log_string = "def data_handler:{}".format(round(end, 4))
            log.info(log_string)
            return response
        elif 'recalculate' in request.POST:
            # print("recalculate")
            form = AuctionCorrectionForm(request.POST or None, instance=auction)
            if form.is_valid():
                form.save()
                log.info("saved form of AuctionCorrectionForm:{}".format(form))
                player_list = Player.objects.filter(auction=auction).all()
                for player in player_list:
                    if player.selected:
                        # player.payout_CZK_corr = player.get_payout_CZK_corr()
                        player.payout_CZK_corr = max(0,player.get_payout_CZK_corr())
                    else:
                        player.payout_CZK_corr = player.payout_CZK
                bulk_update(player_list)
            auction = auction.determine_payment_statistics()
            auction.save_and_cache()
    return redirect(tmpl)


def master_earn_assistant_info(request, tmpl='master-main', data={}):
    from master.models import Assistant
    if request.POST:
        if 'first_name' in request.POST:
            import random
            payment_range = 100
            assistant= Assistant()
            assistant.first_name = request.POST['first_name']
            assistant.last_name = request.POST['last_name']
            assistant.target_payment = int(request.POST['target_payment'])
            assistant.earning = request.POST['target_payment']
            assistant.earning = assistant.target_payment - (payment_range / 2) + random.randrange(0, payment_range, 10)
            assistant.id_or_birth_number = request.POST['id_or_birth_number']
            assistant.cache_me()
    return redirect(tmpl)
    # return(request)

@login_required(redirect_field_name="login", login_url='master-login_user')
def main_earnings(request, tmpl='', data={}):
    # print("log.info('on views_earnings')")
    log.info("on views_earnings")
    user = request.user
    auction, treatment = Auction.cache_or_create_auction()
    if user.pk != 99:  # thus not admin
        raise Exception("player in data!!!???")

    master_man = MasterMan.cache_or_create_mm()
    # print("master_man.payment_sheet in main1:[]".format(master_man.payment_sheet))

    auctionCorrectForm = AuctionCorrectionForm(
        initial={'multiplier': auction.multiplier, 'multiplier_PR': auction.multiplier_PR,
                 'multiplier_RE': auction.multiplier_RE, 'fixed_uplift': auction.fixed_uplift,
                 'fixed_uplift_PR': auction.fixed_uplift_PR, 'fixed_uplift_RE': auction.fixed_uplift_RE})

    # log.info('treatmentFormvalue',treatment_form['fields'].value())
    # log.info("treatment.id",treatment.id)
    player_list_testing = Player.objects.filter(auction=auction, testing_correct__gte=1).order_by('-selected','user__ip','user_id','group_id')
    player_question_list = Player_Questions.objects.filter(player__in=player_list_testing).values(
        'question').annotate(trials__avg=Round(Avg('trials'))).order_by('question')


    # print("player_question_list:{}".format(player_question_list))

    # ToDo: make into dict patternmatching...
    player_list = master_man.get_selection(auction)
    log.info("player_list:{}".format(player_list))
    for player in player_list:
        # print("player:{}".format(player))
        log.info("player:{}".format(player))
        # player.get_payout_CZK_corr()
    # print("master_man.payment_sheet in main:[]".format(master_man.payment_sheet))

    from master.models import Assistant
    assistant = Assistant.cache_get()
    if not assistant:
        assistant = Assistant()
        assistant.cache_me()
    # assistant['first_name'] = 'Jan'
    # assistant['last_name'] = 'Vavra'
    # assistant['id_or_birth_number'] = '910907/1037'
    # import random
    # assistant['earning'] = 400 + random.randrange(0, 200, 10)


    if master_man.show_selection == MasterMan.SHOW_ALL:
        total_paid_out = Player.objects.filter(auction=auction).aggregate(Sum('payout_CZK_corr'))['payout_CZK_corr__sum']
    elif master_man.show_selection == MasterMan.SHOW_SELECTED_ONLY:
        total_paid_out = Player.objects.filter(auction=auction, selected=True).aggregate(Sum('payout_CZK_corr'))['payout_CZK_corr__sum']
    elif master_man.show_selection == MasterMan.SHOW_UNSELECTED_ONLY:
        total_paid_out = Player.objects.filter(auction=auction, selected=False).aggregate(Sum('payout_CZK_corr'))[
        'payout_CZK_corr__sum']
    if master_man.pay_assistant:
        if total_paid_out and assistant.earning:
            log.info("master_man.show_selection:{}".format(master_man.show_selection))
            total_paid_out += assistant.earning
    # assistantForm = AssistantForm(initial={'first_name':assistant.first_name})
    # print("assistant")
    # print("total_avg_list:{}".format(total_avg_list))
    # total_spend = total_avg_list

    data = {
        # 'assistantForm':assistantForm,
        'total_paid_out': total_paid_out,
        'players': player_list,
            "auction": auction,
            'treatment': treatment, 'view': master_man.view,
            "auctionCorrectForm": auctionCorrectForm,
            "player_question_list": player_question_list,
            'show_payments':master_man.show_payments,
            'show_table':master_man.show_table,
            'show_unselected': master_man.show_unselected,
            'master_man': master_man,
        'assistant': assistant
            }

    ###########################################
    tmpl = 'master/master.html'
    return render(request, tmpl, context=data)