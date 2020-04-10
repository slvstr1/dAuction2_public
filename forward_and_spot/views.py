#!python3
import time
import copy
import logging
# from django.utils import timezone
from django.db import transaction
from django_bulk_update.helper import bulk_update
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from api.serializers import sPlayerSerializer, sPlayer_statsSerializer,sPlayer_statsSerializer_with
from master.models import MasterMan
from forward_and_spot.models import Auction, Treatment,Offer, Player, Phase, Player_stats, Voucher, Timer, Period
from .functions import set_voucher, clear_offer_larger, clear_offer_smaller, set_products

log = logging.getLogger(__name__)


@login_required(redirect_field_name="login_user", login_url='master-login_user')
def main(request,tmpl='instructions-main', data={}):
    # log.info("ON THE FS MAIN")
    start = time.time()
    auction, treatment = Auction.cache_or_create_auction()
    if not auction.app == Auction.FS:
        log.info("return redirect('master-main')")
        return redirect("master-main")
    user=request.user

    try:
        player = user.player.get(auction=auction)
        group = player.group

    except Player.DoesNotExist:
        # log.info("return redirect('master-main')")
        end = time.time() - start
        log_string = "def fs.main-redirect: " + str(round(end, 4)) + "has no player, for user_id: " + str(user.id)
        log.info(log_string)
        return redirect('master-main')
    if not player.selected:
        return redirect('master-main')
    log.info("landed on main, user:{}, playerid:{}, group:{}".format(user, player, player.group))
    player.FS_app()
    tmpl='forward_and_spot/auction_page.html'
    data = { "auction": auction, "user":user,"player":player, "group":group}
    end = time.time() - start
    # log_string = "def fs.main: " + str(round(end, 4)) + "for user_id: " + str(player.user_id)
    # log.info(log_string)
    return render(request, tmpl, context=data)


# subfunctions belonging to set_offer # ## Official Python hack to leave them global to allow tests ## yes, it is super fucked up but Python is not perfect (http://code.activestate.com/recipes/580716-unit-testing-nested-functions/)
def is_using_vouchers(player_role, posedc_type):
    return (player_role - posedc_type == 0)

def get_wait_key(user_id):
    return 'wait_four_seconds{}'.format(user_id)

def offer_was_made_just_before(user_id):
    return cache.get(get_wait_key(user_id))

# def must_wait_check(wait_key):
#     wait_four_seconds = cache.get(wait_key)
#     return wait_four_seconds

def must_wait_set(user_id, time_for_succession):
    cache.set(get_wait_key(user_id), 'True', time_for_succession)

def has_enough_vouchers(max_vouchers, postedc_quantity, vouchers_used):
    return vouchers_used + postedc_quantity <= max_vouchers

def is_not_too_short_on_vouchers(short_maximum, postedc_quantity, vouchers_negative):
    return postedc_quantity + vouchers_negative  <= short_maximum

@csrf_exempt
@transaction.atomic
def set_offer(request, data={}):
    """
    Checks if the offer is correct
    :param request:
    :param data:
    :return:
    """
# imagine here the non-nested nested functions

    start = time.time()
    # log.info("set offer")
    if request.method =='POST':
        postedc_price = int(request.POST.get("priceOriginal"))
        postedc_quantity = int(request.POST.get("unitsOriginal"))
        posedc_type = int(request.POST.get("Type"))
        auction_id = request.POST.get("auction_id")
        user_id = request.POST.get("user_id")
        player_id = request.POST.get("player_id")
        group_id = request.POST.get("group_id")
        # log.info('posedc_type', posedc_type)
        # log.info ('auction_id',auction_id)
        # log.info('user_id', user_id)
        # log.info('player_id', player_id)
    else:
        return
    if user_id:
        user_id=int(user_id)
    else:
        # log.info('NO USER ID', user_id)
        log_string = "NO USER ID: {}".format(user_id)
        log.info(log_string)
        user_id = request.user.id

    tt = Timer.cache_get()
    if not tt:
        tt=Timer()
    if tt.seconds_left < 0:
        log.info("Time is up for:{}".format(user_id))
        message = "Time is up"
        return JsonResponse(["error", message], safe=False)

    auction, treatment = Auction.cache_or_create_auction()

    if offer_was_made_just_before(user_id):
        return JsonResponse(["wait", "Your offer status has been changed just before (< {} sec)!".format(
            treatment.time_for_succession)], safe=False)

    # HERE HE GETS THE PHASE - what if the phase changes?
    phase = Phase.cache_get()
    if not phase:
        phase=Phase.objects.filter(auction_id=auction_id).select_related('period').last()
        phase.cache_me()
        period = phase.period
        period.cache_me()
    else:
        period = Period.cache_get()
        if not period:
            period = phase.period
            period.cache_me()

    if player_id:
        player_id = int(player_id)
        p_stats = Player_stats.objects.select_related('player','group').get(auction_id=auction_id, player_id=player_id, period=period)
        player = p_stats.player
    else:
        # log.info('NO PLAYER ID', player_id)
        log_string = "NO PLAYER ID: {}".format(player_id)
        log.info(log_string)
        user = request.user
        player = user.player.get(auction=auction)
        player_id = player.id

    offer_validated=False
    if is_using_vouchers(player.role, posedc_type): # is using vouchers / going long

        if has_enough_vouchers(treatment.max_vouchers, postedc_quantity, p_stats.vouchers_used):
            offer_validated = True
        else:
            log.info("Set offer: reached the maximum short position for {}".format(user_id))
            message = "You have have reached maximum short position of {} units!".format(treatment.short_maximum)
            return JsonResponse(["error", message], safe=False)

    else: # is acquiring vouchers / going short

        if is_not_too_short_on_vouchers(treatment.short_maximum,postedc_quantity, p_stats.vouchers_negative):
            offer_validated = True
        else: # is too short on vouchers
            log.info("Set offer: not enough vouchers for {}".format(user_id))
            message = "You have not enough vouchers for this order!"
            return JsonResponse(["error", message], safe=False)

    if offer_validated:
        # log.info("set_offer called!")
        must_wait_set(user_id, treatment.time_for_succession)
        timenow=time.time()
        set_offer_nr(treatment, auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type,postedc_quantity, postedc_price, period, phase, start)
        log.info(".........................................time for offer:'{0:.3f}".format(time.time()-timenow))
        # note, offer is made with a specific phase - can this phase be changed in the meantime?
    return HttpResponse(status=204)


def set_offer_nr(treatment,auction,auction_id, group_id, player,player_id, user_id, p_stats,posedc_type, postedc_quantity,postedc_price,period, phase, start):

  # log.info("previous_offers_same_type)",previous_offers_same_type)
    c, reuse, cc= Offer.create_present_offer(treatment, auction_id, phase,player_id,posedc_type,postedc_quantity,postedc_price,group_id,player)
    if cc:
      cc.save(update_fields=['canceled'])
    offer_list = c.create_matching_offer_list(auction_id,phase,player_id,group_id)
    # log.info("offer_list: {}".format(offer_list))


    if offer_list:
        player_stats_CHANGED=True
        first_index = 0
        first = offer_list[first_index]
        # log.info("first = offer_list[first_index]: {}".format(first))
        # offers_to_update =[]
        end = False
        offer_list_items = len(offer_list)
        # log.info("offer_list_items: {}".format(offer_list_items))
        # to_update = [cc, ]
    else:
        end = True
        player_stats_CHANGED=False
        c.save()
        if cc:
            cc.save(update_fields=['canceled'])
        # log.info("connection.queries() before return", connection.queries)
        endtime = time.time() - start
        # log_string = "SETOFFER: no counteroffers {} for {}. c:{}".format(round(endtime, 4), user_id, c)
        # log.info(log_string)
        return


    if not end:
        to_insert_c=[]
        to_update=[]
        while first is not None and not end:
            # log.info("AFTER_ while first is not None and not end")
            first_player = first.player
            first_player_str =str(first_player.id)

            wait_key = 'wait_four_seconds{}'.format(first_player_str )
            cache.set(wait_key, 'True', treatment.time_for_succession)

            # offers_to_update.append(first.id)
            f_stats = Player_stats.objects.get(auction_id=auction_id, player=first_player, period=period)

            # log.info("Before_ ifcond")
            if c.unitsAvailable > first.unitsAvailable:
                # log.info("c.unitsAvailable > first.unitsAvailable")
                # 1.clear the smaller, first
                first.cleared, first.unitsCleared, first.priceCleared, first.unitsAvailable, first.timeCleared = clear_offer_smaller(smaller_one=first, larger_one=first)

                # 2.make copy for the larger, c into c2
                c2 = Offer.split_offer(auction_id, group_id, to_split=c, to_split_player=player,other_offer=first, phase=phase)

                # 3.clear the larger, c (the part of the present offer that will be cleared)
                c.cleared, c.unitsCleared, c.priceCleared, c.unitsAvailable, c.timeCleared = clear_offer_larger(larger_one=first, smaller_one=first)

                # 5. set products
                c.product, first.product = set_products(c.offer_tiepe, first.unitsCleared, first.priceCleared)
                p_stats.trading_result += c.product
                f_stats.trading_result += first.product

                if reuse:
                    to_update.append(c)
                else:
                    to_insert_c.append(c)
                to_update.append(first)

                # 6. set vouchers
                # print("before_set_voucher>")
                p_stats, f_stats = set_voucher(p_stats, f_stats, first.offer_tiepe, c.unitsCleared, auction, treatment)

                c = copy.copy(c2)
                if offer_list_items > first_index + 1:
                    first_index += 1
                    # log.info("first_index:{}".format(first_index))
                    # log.info("offer_list:{}".format(offer_list))
                    offer_list_items = len(offer_list)
                    # log.info("offer_list_items: {}".format(offer_list_items))
                    first = offer_list[first_index]
                    # if offer_list2.exists():
                    #     first_nouse= offer_list2.last()
                    # here is a problem!!! IndexError: list index out of range
                    first_player = first.player
                    first_player_str = str(first_player.id)
                else:
                    to_insert_c.append(c)
                    log.debug("no more offers: %s" % offer_list)
                    first = None
                    end=True
            elif c.unitsAvailable < first.unitsAvailable:
                # log.info("c.unitsAvailable < first.unitsAvailable")
                # 1.clear the smaller, first
                # clear_offer_smaller(to_be_set=c, first=first)
                c.cleared, c.unitsCleared, c.priceCleared, c.unitsAvailable, c.timeCleared = clear_offer_smaller(smaller_one=c, larger_one=first)
                # 2.make copy for the larger, c into c2
                f2 = Offer.split_offer(auction_id, group_id, to_split=first, to_split_player=first_player,other_offer=c, phase=phase)
                # log.info("")
                # log.info("first:{}".format(first))

                # 3.clear the larger, c (the part of the present offer that will be cleared)
                # clear_offer_larger(to_be_set=first, first=first, smaller=c)
                first.cleared, first.unitsCleared, first.priceCleared, first.unitsAvailable, first.timeCleared = clear_offer_larger(larger_one=first, smaller_one=c)

                # 5. set products
                # stats_calculations(c=c, first=first, p_stats=p_stats, f_stats=f_stats)
                c.product, first.product = set_products(c.offer_tiepe, first.unitsCleared, first.priceCleared)
                p_stats.trading_result += c.product
                f_stats.trading_result += first.product
                # 6. set vouchers

                # print("before_set_voucher<")
                p_stats, f_stats = set_voucher(p_stats, f_stats, first.offer_tiepe, c.unitsCleared, auction, treatment)  # The vouchers are ticked
                to_update.append(first)
                to_insert_c.append(f2)
                if reuse:
                    to_update.append(c)
                else:
                    to_insert_c.append(c)
                end = True
            else:
                # log.info("c.unitsAvailable = first.unitsAvailable")
                # 1.clear the smaller, first
                c.cleared, c.unitsCleared, c.priceCleared, c.unitsAvailable, c.timeCleared = clear_offer_smaller(smaller_one=c, larger_one=first)

                # 3.clear the larger, c (the part of the present offer that will be cleared)
                first.cleared, first.unitsCleared, first.priceCleared, first.unitsAvailable, first.timeCleared = clear_offer_larger(larger_one=first, smaller_one=c)
                # 5. set products
                c.product, first.product = set_products(c.offer_tiepe, first.unitsCleared, first.priceCleared)
                p_stats.trading_result += c.product
                f_stats.trading_result += first.product

                if reuse:
                    to_update.append(c)
                else:
                    to_insert_c.append(c)
                to_update.append(first)

                # 6. set vouchers
                # print("before_set_voucher=")
                p_stats, f_stats = set_voucher(p_stats, f_stats, first.offer_tiepe, c.unitsCleared, auction, treatment)  # The vouchers are ticked
                end = True
            # cache.set("{}player_ser_data".format(first_player_str), None)

            first_player_stats_ser_data = Player_stats.get_stats_ser_data([f_stats,], phase)
            # MasterMan.cache_it("{}player_ser_data".format(first_player_str), first_player_ser_data, 30)
            cache.set("{}player_stats_ser_data".format(first_player_str), first_player_stats_ser_data, 30)
            first_player_ser = sPlayerSerializer(first_player)
            first_player_ser_data = first_player_ser.data
            # MasterMan.cache_it("{}player_stats_ser_data".format(first_player_str), first_player_ser_data, 15)
            cache.set("{}player_ser_data".format(first_player_str), first_player_ser_data, 15)

        msg = Offer.objects.bulk_create(to_insert_c)
        bulk_update(to_update)
        # log.info("msg",msg)
    if player_stats_CHANGED:
        if phase.active_state == Phase.CONDITIONAL:
            tt = Timer.cache_get()
            tt=tt.short_timer_set(treatment.time_conditional)
            # log.info("0000000000000000000000 RENEWED 00000000000000000000000000000000")
        # player_str = str(player_id)
        # cache.set(player_str + "player_ser_data", None)
        player_ser = sPlayerSerializer(player)
        # MasterMan.cache_it("{}player_ser_data".format(player_str), player_ser.data, 30)
        cache.set("{}player_ser_data".format(player_id), player_ser.data, 30)
        # print("phase_idd_in_fs:{}".format(phase.idd))
        p_stats_ser_data = Player_stats.get_stats_ser_data([p_stats,], phase)
        # MasterMan.cache_it("{}player_stats_ser_data".format(player_str),p_stats_ser_data , 15)
        cache.set("{}player_stats_ser_data".format(player_id), p_stats_ser_data, 15)

        # log_string = "player_str: {}, first_player_str:{}".format(player_id, first_player_str)
        # log.info(log_string)

    # end=time.time() - start
    # log_string = "SETOFFER time:{}, for player:{}".format(round(end,3),player_id)
    # log.info(log_string)


