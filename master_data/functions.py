import os, math, gzip, logging, csv
from dAuction2.settings import BASE_DIR
from django.http import StreamingHttpResponse
from django.shortcuts import redirect
from django_bulk_update.helper import bulk_update
from distribution.models import Distribution
from forward_and_spot.models import Auction,  Group, Treatment
from forward_and_spot.models import Offer, Player,Player_stats, Voucher, VoucherRE, Phase,Penalty,Period
# from instructions.models import Page
from testing.models import Player_Questions, Player_Question_Options, Option_MC, Question
from master.models import MasterMan
log = logging.getLogger(__name__)

def populate_uid(auction, list):
    list_list = [Offer.objects.all(),
                 Distribution.objects.all(),
                 Option_MC.objects.all(),
                 Group.objects.all(),
                 Period.objects.all(),
                 # Page.objects.all(),
                 Penalty.objects.all(),
                 Phase.objects.all(),
                 Player.objects.all(),
                 Player_Question_Options.objects.all(),
                 Player_Questions.objects.all(),
                 Player_stats.objects.all(),
                 Question.objects.all(),
                 Voucher.objects.all(),
                 VoucherRE.objects.all(),
                 ]
    for list in list_list:
        # print("list:{}".format(list))
        for obj in list:
            obj.uid=obj.auction_id * 1000000+ obj.id
        lenpks =bulk_update(list,update_fields=['uid',])
        # print("lenpks:{}".format(lenpks))
    list= Treatment.objects.all()
    for obj in list:
        obj.idd=obj.id
    lenpks =bulk_update(list,update_fields=['idd',])
    # print("lenpks:{}".format(lenpks))


# def get_model_fields(model):
#     return model._meta.fields


# def cache_key_individual(object_to_cache_name, object_to_cache):
#     return "{}_{}".format(object_to_cache_name, object_to_cache.pk)


def make_excel_csv(treatment, auction_list, filename, tmpl):
    auction = Auction.objects.filter(active=True).last()
    filename_csv = "{}.csv".format(filename)
    log.info("excel_csv")
    rows = []
    empty_fields = False
    player_list = Player.objects.filter(auction__in=auction_list).all()
    pre_field_name = "pl"
    field_name_list_player = ["id", "role", "payout_ECU", 'pay_period', 'pay_qs_period', "total_cost", "total_values", "payout_CZK_corr",
                              'testing_finished', 'testing_correct', 'testing_errors', 'first_name', 'last_name',
                              'male', 'age', 'difficult_rating', 'interesting_rating', 'income_monthly_CZK', 'comments',"selected", "cumulative_earnings", "done_before",
                              'do_better_what']
    if not player_list:
        empty_fields = True
        auction.empty_fields_in_export = empty_fields
        auction.save()
        auction.save_and_cache()
        # cache.set("auction", auction)
        return redirect(tmpl)
    player = player_list.first()
    model_object = player
    fields_player = get_my_model_fields(model_object, field_name_list_player)

    group_list = Group.objects.filter(auction__in=auction_list).order_by('pk')
    pre_field_name = "gr"
    field_name_list_group = ['idd']
    group = group_list.last()
    model_object = group
    fields_group = get_my_model_fields(model_object, field_name_list_group)
    pre_field_name = "tr"
    field_name_list_treatment = ['id','idd', 'created', 'PR_per_group', 'RE_per_group', 'convexity_parameter', 'a', 'F', 'mu',
                                 'sigma', 'uniform_min', 'uniform_max', 'retail_price', 'demand_avg_theory',
                                 'demand_sd_theory', 'price_avg_theory', 'total_groups', 'time_for_forward_1',
                                 'time_for_forward_2', 'time_for_spot_1', 'time_for_spot_2', 'time_for_spot_3',
                                 'total_periods', 'qp_every', 'error_max', 'ECU_per_CZK_PR', 'ECU_per_CZK_RE',
                                 'max_vouchers', 'short_maximum', 'penalty_perunit','educational', ]
    model_object = treatment
    fields_treatment = get_my_model_fields(model_object, field_name_list_treatment)

    pre_field_name = "au"
    field_name_list_auction = ['id','particular_info','encountered_issues','is_part_experiment', 'demand_avg', 'demand_sd', 'price_avg', 'price_sd', 'cov_DP','ECU_per_CZK_PR','ECU_per_CZK_RE' ]
    model_object = auction
    fields_auction = get_my_model_fields(model_object, field_name_list_auction)

    # fields_period =[]
    period_list = Period.objects.filter(auction__in=auction_list).order_by('pk')
    pre_field_name = "pe"
    field_name_list_period = ['idd']
    if not period_list:
        empty_fields = True
        period = Period(auction__in=auction_list, pk=1)
        period.save()
    else:
        period = period_list.first()
    model_object = period
    fields_period = get_my_model_fields(model_object, field_name_list_period)

    phase_list = Phase.objects.filter(auction__in=auction_list).order_by('pk')
    pre_field_name = "ph"
    field_name_list_phase = ['idd', 'created']
    if not phase_list:
        empty_fields = True
        phase = Phase(auction=auction, period=period)
        phase.save()
        # phase_list = Phase.objects.filter(auction=auction).order_by('pk')
    else:
        phase = phase_list.last()
    model_object = phase
    fields_phase = get_my_model_fields(model_object, field_name_list_phase)

    offer_list = Offer.objects.all().prefetch_related('phase','phase__period').order_by('pk')
    pre_field_name = "of"
    field_name_list_offer = ['id', 'created', 'timeCleared', 'offer_tiepe', 'cleared', 'updated', 'unitsAvailable',
                             'unitsCleared', 'priceCleared', 'priceOriginal', 'product', 'canceled']
    if not offer_list:
        empty_fields = True
        offer = Offer(auction=auction, player=player, phase=phase, group=group)
        offer.save()
        # offer_list = Offer.objects.all().order_by('pk')
    else:
        offer = offer_list.last()
    model_object = offer
    fields_offer = get_my_model_fields(model_object, field_name_list_offer)

    # fields_playerstats =[]
    playerstats_list = Player_stats.objects.prefetch_related('auction__treatment','auction','player','group').filter(auction__in=auction_list).order_by('player', 'pk')
    pre_field_name = "ps"
    field_name_list = ['id', 'role', 'player_demand', 'trading_result', 'trading_result_stage1', 'total_cost',
                       'total_values', 'profit', 'end_penalty', 'penalty_perunit', 'penalty_phase_total', 'question',
                       'price_perfect_expectation', 'required_units_expectation', 'price_real_expectation',
                       'units_missing', 'vouchers_used', 'vouchers_negative', 'vouchers_negative_stage1',
                       'vouchers_used_stage1', 'auction_id', 'group_id', 'period_id', 'player_id', 'created']
    if not playerstats_list:
        empty_fields = True
        playerstats = Player_stats(auction=auction, player=player, group=group, period=period)
        playerstats.save()
    else:
        playerstats = playerstats_list.last()
    model_object = playerstats
    fields_playerstats = get_my_model_fields(model_object, field_name_list)
    auction.empty_fields_in_export = empty_fields
    auction.save()
    auction.save_and_cache()

    row_elt = []
    # for field in fields_user:
    for field in fields_player:
        row_elt += ["pl_" + field.name]
    for field in fields_group:
        row_elt += ["gr_" + field.name]
    for field in fields_period:
        row_elt += ["pe_" + field.name]
    for field in fields_phase:
        row_elt += ["ph_" + field.name]
    for field in fields_offer:
        row_elt += ["of_" + field.name]
    for field in fields_playerstats:
        row_elt += ["ps_" + field.name]
    for field in fields_auction:
        row_elt += ["au_" + field.name]
    for field in fields_treatment:
        row_elt += ["tr_" + field.name]

    rows += [row_elt]

    for group in group_list:
        for period in period_list:
            for phase in phase_list.filter(period=period):
                for playerstats in playerstats_list.filter(period=period):
                    for offer in offer_list.filter(phase=phase, group=group, player=playerstats.player):
                        row_elt = []
                        for field in fields_player:
                            row_elt += [getattr(playerstats.player, field.name)]
                        for field in fields_group:
                            row_elt += [getattr(group, field.name)]
                        for field in fields_period:
                            row_elt += [getattr(period, field.name)]
                        for field in fields_phase:
                            row_elt += [getattr(phase, field.name)]
                        for field in fields_offer:
                            row_elt += [getattr(offer, field.name)]
                        for field in fields_playerstats:
                            row_elt += [getattr(playerstats, field.name)]
                            # AUCTION
                        auction=playerstats.auction
                        treatment = playerstats.auction.treatment
                        for field in fields_auction:
                            row_elt += [getattr(auction, field.name)]
                        for field in fields_treatment:
                            row_elt += [getattr(treatment, field.name)]
                        rows += [row_elt]
    response = csv_print(filename_csv, rows)
    Auction.make_sound(duration=4, freq=2)
    # import os
    # duration = 1  # seconds
    # freq = 440  # Hz
    # os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    return response


def csv_print(filename_csv, rows):
    class Echo(object):
        """An object that implements just the write method of the file-like
        interface.
        """

        def write(self, value):
            """Write the value by returning it, instead of storing in a buffer."""
            return value

    pseudo_buffer = Echo()
    # writer = csv.writer(pseudo_buffer,dialect='excel_tab')
    writer = csv.writer(pseudo_buffer,  delimiter='\t')
    response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename_csv
    return response

def get_list_sizedir(dir_name):
    listdir = sorted(os.listdir(dir_name), reverse=False)
    list_sizedir = [[name, convert_size(os.path.getsize(os.path.join(BASE_DIR, dir_name, name)))] for name
                    in listdir]
    return list_sizedir


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


def get_my_model_fields(model,field_name_list):
    field_list=[]
    for field_name in field_name_list:
        # log.info("for model:{}, field name:{}".format(model, field_name))
        field_list += [model._meta.get_field(field_name)]
    return field_list