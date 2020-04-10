#!python3
import time, random, logging
from api.serializers import sPlayerNestedSerializer,sTimerSerializer,sPhaseSerializer, sAuctionSerializer, sPeriodSerializer, sTreatmentSerializer
from django_bulk_update.helper import bulk_update
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.core.cache import cache
from .functions import merge_dicts, Round
from forward_and_spot.models import Player,Phase, Penalty,  Period, Timer, Group, Player_stats, Auction, Treatment
from dAuction2.settings import UNIQUEIZER
from master.models import MasterMan

log = logging.getLogger(__name__)
logger = logging.getLogger(__name__)
debug_logger = logging.getLogger('debug_logger')
##### views template for user login

# @login_required(redirect_field_name="login")


@login_required(redirect_field_name="login", login_url='master-login_user')
# @profile(immediate=True,entries=20)
def ajax_admin(request, tmpl='', data={}):
    start = time.time()
    # start1 = time.time()
    #     except Auction.DoesNotExist:
    #         missing_object = "Auction"
    #         return JsonResponse("{} does not exist".format(missing_object),safe=False)

    # auction, treatment = Auction.cache_or_create_auction()
    auction = Auction.cache_get()
    treatment = Treatment.cache_get()
    if not auction:
        return JsonResponse("auction or treatment does not exist", safe=False)
    if not treatment:
        return JsonResponse("auction or treatment does not exist", safe=False)
    group_list=cache.get("group_list")
    if not group_list:
        group_list = Group.get_groups(auction)
        MasterMan.cache_it("group_list", group_list)
    # print("a")
    cache_duration = cache.get("cache_duration")
    # log.info("cache_duration:{}".format(cache_duration ))
    if not cache_duration:
        cache_duration = auction.time_refresh_data * 0.00099
        cache.set("cache_duration", cache_duration)
    # log.info("cache_duration:{}".format(cache_duration))
    data['cache_duration']=cache_duration

    auction_ser_data= cache.get("auction_ser_data")
    if not auction_ser_data:
        auction_ser = sAuctionSerializer(auction)
        auction_ser_data = auction_ser.data
        MasterMan.cache_it("auction_ser_data", auction_ser_data, 40)

    treatment_ser_data = cache.get("treatment_ser_data")
    if not treatment_ser_data :
        # treatment = Treatment.cache_or_create_treatment()
        treatment_ser = sTreatmentSerializer(treatment)
        treatment_ser_data = treatment_ser.data
        MasterMan.cache_it("treatment_ser_data", treatment_ser_data)
    merged_auction_ser_data = merge_dicts(auction_ser_data, treatment_ser_data)
    # log.info('merged_ser_data: {}'.format(merged_auction_ser_data))

    data['auction'] = merged_auction_ser_data
    # log.info(" data['auction'] = treatment_ser_data: {}".format(data))
    # log.info("auction_ser_data: {}".format(auction_ser_data))
    # log.info("treatment_ser_data: {}".format(treatment_ser_data))

    player_list_ser_data = cache.get("player_list_ser_data")
    if not player_list_ser_data:
        start11 = time.time()
        master_man = MasterMan.cache_or_create_mm()
        # if master_man.show_selection == :
        player_list = master_man.get_selection(auction)
        player_list = player_list.filter(user__isnull=False)
        # log.info("player_list:{}".format(player_list))
        # if master_man.show_unselected:
        #     player_list = Player.objects.filter(auction=auction,user__isnull=False,selected=True).order_by('user__ip','user_id')
        # else:
        #     player_list = Player.objects.filter(auction=auction,user__isnull=False).order_by('user__ip','user_id')
        time_now = int(time.time())
        need_refreshing_set = cache.get("need_refreshing_set")

        for player in player_list:
            key_p = player.user_id
            if need_refreshing_set:
                player.page_need_refreshing = (key_p in need_refreshing_set)
            else:
                player.page_need_refreshing = False
            # log.info("player.page_need_refreshing ",player.user_id,player.page_need_refreshing)
            key_p_last_refresh_date =   "{}last_alive".format(key_p)
            last_refresh_date = cache.get(key_p_last_refresh_date)
            if not last_refresh_date:
                last_refresh_date = time_now
                player.last_alive = 0
            else:
                last_alive = min(99, time_now - last_refresh_date)
                if last_alive > 90:
                    last_alive -= random.randint(10, 20)
                player.last_alive = last_alive

            if auction.app == Auction.DISTR:
                if player.page >= treatment.d_draws_needed:
                    player.state=3
                    # player.save(update_fields='state')
                    player.save()

        player_list_ser = sPlayerNestedSerializer(player_list, many=True)
        player_list_ser_data = player_list_ser.data
        # log.info(player_list_ser_data)
        # end = time.time() - start222
        # log_string = "sPlayerNestedSerializer" + str(round(end, 4))
        # log.info(log_string)
        # cache.set("player_list_ser_data", player_list_ser_data, max(cache_duration,5))
        if auction.auction_started:
            MasterMan.cache_it("player_list_ser_data", player_list_ser_data, max(cache_duration, 3))
        # log_string = "{} ajax_admin-11 (set cache): ".format(str)
    data['players'] = player_list_ser_data

    # log.info("auction.app:{}".format(auction.app))
    # log.info("auction.INSTR:{}".format(auction.INSTR))

    if auction.app == Auction.TESTING:
        if auction.app_testing_started:
            tt = Timer.cache_get()
            # log.info("cache_get():{}".format(tt))
            # log.info("Timer.objects.exists():{}".format(Timer.objects.exists()))
            if not tt:
                tt= Timer.objects.get_or_create(pk=1)[0]
                debug_logger.debug("SET CACHE")
                tt=tt.timer_set( time_length=treatment.time_for_testing)
                tt.cache_me()
            if tt.running:
                time_time = time.time()
                seconds_left = int(tt.end_time - time_time)
                tt.seconds_left=seconds_left
                # log.info('tt.seconds_left:{}'.format( tt.seconds_left))
                if tt.seconds_left <= 0:
                    # time is up!
                    auction.app_testing_ended = True
                    auction.app_testing_started = False
                    auction.save_and_cache()

                    
                    # MasterMan.cache_me('auction',auction)
                    # tt.running=False
                    tt.seconds_left=0
                    tt.save()
                tt.cache_me()
            tt_ser = sTimerSerializer(tt)
            tt_ser_data = tt_ser.data
            data['tt'] = tt_ser_data

    elif auction.app == Auction.INSTR:
        tt = Timer.cache_get()
        # log.info("tt:{}".format(tt))
        if not tt:
            tt = Timer.objects.get_or_create(pk=1)[0]
            debug_logger.debug("SET CACHE")
            # tt.cache_me()
            tt=tt.timer_set(time_length=treatment.time_for_instructions)
            tt.cache_me()
        if tt.running:
            time_time = time.time()
            seconds_left = int(tt.end_time - time_time)
            tt.seconds_left = seconds_left

            # log.info('tt.seconds_left:{}'.format( tt.seconds_left))
            if tt.seconds_left <= 0:
                # time is up!
                auction.instructions_finished = True
                # auction.instructions_started = False
                auction.save_and_cache()
                
                # MasterMan.cache_me('auction', auction)
                # tt.running=False
                tt.seconds_left = 0
                tt.save()
            tt.cache_me()
        tt_ser = sTimerSerializer(tt)
        tt_ser_data = tt_ser.data
        data['tt'] = tt_ser_data

    elif auction.app == Auction.DISTR:
        tt = Timer.cache_get()
        if not tt:
            tt = Timer.objects.get_or_create(pk=1)[0]
            debug_logger.debug("SET CACHE")
            # tt.cache_me()
            tt=tt.timer_set( time_length=treatment.time_for_distribution)
            tt.cache_me()
        if tt.running:
            time_time = time.time()
            seconds_left = int(tt.end_time - time_time)
            tt.seconds_left = seconds_left

            # log.info('tt.seconds_left:{}'.format(tt.seconds_left))
            if tt.seconds_left <= 0:
                # time is up!

                # tt.running=False
                tt.seconds_left = 0
                tt.save()
            tt.cache_me()
        tt_ser = sTimerSerializer(tt)
        tt_ser_data = tt_ser.data
        data['tt'] = tt_ser_data



    elif auction.app == Auction.FS:
        # print("auction_started:{}".format(auction.auction_started))
        # print("auction_app:{}".format(auction.app))
        if auction.auction_started:
            # phase = cache.get('phase')
            phase = Phase.cache_get()
            # log.info("log_phase: {} for admin".format(phase))

            # SVK: there is a good reason to do this already here (even if not needed if auct has not started yet - sets the phase in the cache
            if not phase:
                phase = Phase.objects.filter(auction=auction).select_related('period').last()
                # cache.set("phase", phase)
                phase.cache_me()
                # MasterMan.cache_me("phase", phase)
                debug_logger.debug("SET CACHE phase".format(phase))
                log.info("auction:".format(auction))

            period = Period.cache_get()
            if not period:
                period = phase.period
                period.cache_me()
                debug_logger.debug("SET CACHE period:".format(period))

            tt = Timer.cache_get()
            # log_stringd = "tt - ajax_admin: {}".format(tt)
            # debug_logger.debug(log_stringd)
            if not tt:
                tt= Timer.objects.get_or_create(pk=1)[0]
                debug_logger.debug("SET CACHE")
                tt.cache_me()

            if tt.running:
                time_time = time.time()
                seconds_left = int(tt.end_time - time_time)
                tt.seconds_left=seconds_left
                if tt.short_running:
                    tt.short_seconds_left=int(tt.short_end_time - time_time)
                tt.cache_me()
            wait_ten_seconds=cache.get('wait_ten_seconds')
            if not wait_ten_seconds:
                cache.set('wait_ten_seconds','True', 30)
                tt.save_and_cache()
                debug_logger.debug("tt.save() !!! {}, sec_left {},  ".format(tt, tt.seconds_left) )
                log_string = "tt.save() !!! {}, sec_left {},  ".format(tt, tt.seconds_left)
                log.info(log_string)

            if phase.question_page:
                # log.info(log_string)
                log.info("phase:{}".format(phase))
                log.info("phase.question_page:{}".format(phase.question_page))
                playerstats = Player_stats.objects.filter(auction=auction).filter( period=period)
                allready = True
                for playerstat in playerstats:
                    if playerstat.price_perfect_expectation < 0 or playerstat.price_real_expectation < 0 or playerstat.required_units_expectation < 0:
                        allready = False
                if allready:
                    tt.end_time = int(time.time() - 10)
                    tt.seconds_left = -10
                    tt.cache_me()
                    # cache.set('tt', tt)
                    # debug_logger.debug("tt " + str(tt) + ", sec_left:" + str(tt.seconds_left) + "for admin BEFORE save")
                    tt.save_and_cache()
                    # debug_logger.debug("tt " + str(tt) + ", sec_left:" + str(tt.seconds_left) + "for admin AFTER save")

            elif phase.active_state == Phase.PENALTY:
                is_short = False
                # log.info("phase.active_state == Phase.PENALTY")
                for group in group_list:
                    # update missing units
                    short_player_stats_list = Player_stats.objects.filter(auction=auction, group=group, period=period,units_missing__gt=0, role=Player.RE)
                    if short_player_stats_list:
                        is_short = True
                        # log.info("short_player_stats_list = true")
                    else:
                        is_short = is_short

                if is_short and auction.missing_stages!=0:
                    # if there is a shortage once, this switch is made once!
                    auction.missing_stages = 1
                    auction.save_and_cache()

                if not is_short:
                    if auction.missing_stages==0:
                        tt.end_time = int(time.time() - 10)
                        tt.seconds_left = -10
                    elif auction.missing_stages==1:
                        # so penalty phase started
                        # set timer to 6 seconds
                        tt.end_time = int(time.time() + 6)
                        tt.seconds_left = 6
                        auction.missing_stages = 2
                        # MasterMan.cache_me('auction', auction)
                        auction.cache_me()
                    # tt.cache_me()
                    # cache.set('tt', tt)
                    # debug_logger.debug("tt " + str(tt) + ", sec_left:" + str(tt.seconds_left) + "for admin BEFORE save")
                    tt.save_and_cache()
            buffer_time = -4
            if tt.seconds_left  <= buffer_time  or tt.short_seconds_left <= buffer_time  : # move players to a new state!
# FORWARD  -  FORWARD  -  FORWARD  -  FORWARD  -  FORWARD

                if phase.idd == Phase.FORWARD:
                    if phase.question_page:
                        # PHASE=1, question page  -> START WAITING
                        phase.question_page = False
                        phase.waiting_page = False
                        phase.save_and_cache()
                        # MasterMan.cache_me("phase", phase)
                        # phase.cache_me("phase")
                        tt=tt.timer_set(time_length= treatment.time_for_forward_1)
                        tt.cache_me()

                        lg_str = "period {}, phase {},  id {}, state {}, waiting {}, question_page {}, end {}, for admin BEFORE save ".format(
                            period.id,
                            phase, phase.idd, phase.active_state,
                            phase.waiting_page, phase.question_page, phase.end)
                        log.info(lg_str)
                    elif not phase.waiting_page:
                        # PHASE=1, ACTIVE
                        if phase.active_state== Phase.INITIAL:
                            # PHASE=1, ACTIVE_STATE 1 -> ACTIVE_STATE 2
                            phase.active_state = Phase.CONDITIONAL

                            tt=tt.timer_set( time_length=treatment.time_for_forward_2, short_time_length=treatment.time_conditional)
                            tt.cache_me()
                            phase.save_and_cache()

                            lg_str = "period {}, phase {},  id {}, state {}, waiting {}, question_page {}, end {}, for admin BEFORE save ".format(
                                period.id,
                                phase, phase.idd, phase.active_state,
                                phase.waiting_page, phase.question_page, phase.end)
                            log.info(lg_str)
                        elif phase.active_state == Phase.CONDITIONAL:
                            # we dont care if times's up because of timer or short_timer, we move on!
                            #go to next state
                            # PHASE=1, ACTIVE_STATE 2 -> START PHASE=1 WAITING
                            phase.waiting_page = True
                            # phase.active_state = Phase.INITIAL
                            phase.save_and_cache()
                            tt=tt.timer_set( time_length=treatment.time_for_forward_waiting)
                            tt.cache_me()
                            player_stats_list = Player_stats.objects.filter(auction=auction,period=period)
                            invalidate_ps(player_stats_list)

                    elif phase.waiting_page:
                        # PHASE=1, WAITING  -> NEXT PHASE (PHASE 2)
                        phase.active_state = Phase.INITIAL
                        phase.waiting_page = False
                        player_stats_list = Player_stats.objects.filter(auction=auction, period=period).select_related('player')
                        for playerstats in player_stats_list:
                            playerstats.vouchers_used_stage1 = playerstats.vouchers_used
                            playerstats.vouchers_negative_stage1 = playerstats.vouchers_negative
                            # playerstats.save()
                        bulk_update(player_stats_list, update_fields=['vouchers_used_stage1', 'vouchers_negative_stage1'])

                        phase = phase.next_phase_procedure(auction) # not much action inside this procedure anymore!!! (creates a new phase)
                        # phase.save_and_cache()


                        tt=tt.timer_set( time_length= treatment.time_for_spot_1)
                        tt.cache_me()

                        lg_str = "period {}, phase {},  id {}, state {}, waiting {}, question_page {}, end {}, for admin BEFORE save ".format(
                            period.id,
                            phase, phase.idd, phase.active_state,
                            phase.waiting_page, phase.question_page, phase.end)
                        log.info(lg_str)
                    else:
                        logger.debug("exception!!!!!!!!!!!!!!!!")

# SPOT  -  SPOT  -  SPOT  -  SPOT  -  SPOT  -  SPOT  -  SPOT  -  SPOT  -  SPOT  -  SPOT  -  SPOT  -  SPOT  -  SPOT
                elif phase.idd == Phase.SPOT:
                    if not phase.waiting_page:
                        # PHASE=2, ACTIVE -> START WAITING
                        # player_list = Player.objects.filter(auction=auction, user__isnull=False,group=group).order_by(
                        #     'pk')
                        if phase.active_state == Phase.INITIAL:
                            # go to conditional
                            tt=tt.timer_set( time_length=treatment.time_for_spot_2,
                                      short_time_length=treatment.time_conditional)
                            tt.cache_me()

                            phase.active_state = Phase.CONDITIONAL
                            phase.save_and_cache()
                            # phase.save()
                            # MasterMan.cache_me("phase", phase)

                            lg_str = "period {}, phase {},  id {}, state {}, waiting {}, question_page {}, end {}, for admin BEFORE save ".format(
                                period.id,
                                phase, phase.idd, phase.active_state,
                                phase.waiting_page, phase.question_page, phase.end)
                            log.info(lg_str)
                        elif phase.active_state == Phase.CONDITIONAL:
                            # we dont care if times's up because of timer or short_timer, we move on!
                            # go to next state (penalty)
                            tt=tt.timer_set( time_length=treatment.time_for_spot_3,
                                      short_time_length=treatment.time_conditional)
                            # tt.cache_me()

                            phase.active_state = Phase.PENALTY
                            phase.save_and_cache()
                            # phase.save()
                            # MasterMan.cache_me("phase", phase)
                            # timer_set(tt, time_length=treatment.time_for_spot_3)

                            lg_str = "period {}, phase {},  id {}, state {}, waiting {}, question_page {}, end {}, for admin BEFORE save ".format(period.id,
                                phase, phase.idd, phase.active_state,
                                phase.waiting_page, phase.question_page, phase.end)
                            log.info(lg_str)

                        elif phase.active_state == Phase.PENALTY:
                            if tt.seconds_left <= buffer_time  :
                                # give end_penalty and go to next state
                                # PHASE=1, ACTIVE_STATE 2 -> START PHASE=1 WAITING

                                phase.waiting_page = True
                                phase.active_state = Phase.INITIAL
                                phase.save_and_cache()
                                tt=tt.timer_set(time_length=treatment.time_for_spot_waiting)
                                print("is_short:{}".format(is_short))
                                if is_short:
                                    for group in group_list:
                                        # log.info("group_list", group_list)
                                        Penalty.give_penalty(treatment, auction, group, period,phase)
                                if period.idd >= treatment.total_periods:
                                    auction.end = True
                                else:
                                    auction.missing_stages=0
                                auction.save_and_cache()
                                cache.set("auction_ser_data", None)
                                lg_str = "period {}, phase {},  id {}, state {}, waiting {}, question_page {}, end {}, for admin BEFORE save ".format(
                                    period.id,
                                    phase, phase.idd, phase.active_state,
                                    phase.waiting_page, phase.question_page, phase.end)
                                log.info(lg_str)
                                player_stats_list = Player_stats.objects.filter(auction=auction,period=period).select_related('player')
                                to_update = []
                                for player_stats in player_stats_list:
                                    player = player_stats.player
                                    log.info("player.id:{}, player_stats.profit:{}".format(player.id,player_stats.profit))
                                    player_stats.profit_accuracy = player_stats.get_profit_accuracy(treatment)
                                    player.cumulative_earnings += round(player_stats.profit + player_stats.profit_accuracy)
                                    to_update.append(player)
                                    if player.pay_period == period.idd:
                                        player.payout_trade = player_stats.profit
                                        # to_update.append(player)
                                        # player.save()
                                    if player.pay_qs_period == period.idd:
                                        player.payout_qs = player_stats.profit_accuracy
                                        # to_update.append(player)
                                        # player.save()
                                    to_update.append(player)
                                bulk_update(to_update,
                                            update_fields=['payout_trade', 'payout_qs', 'cumulative_earnings'])
                                bulk_update(player_stats_list, update_fields=['profit_accuracy'])

                            elif tt.short_seconds_left <= buffer_time and tt.seconds_left > (buffer_time -0.001 + treatment.time_conditional/2):
                                # give intermediate penalty (and not to next state)
                                # log.info("I give penalty", treatment.penalty_perunit)

                                short_player_stats_list = Player_stats.get_short_player_stats_list(auction,group=None, period=period, treatment_require_units_demanded_on_PR=treatment.require_units_demanded_on_PR)
                                # if treatment.require_units_demanded_on_PR:
                                #     short_player_stats_list = Player_stats.objects.filter(auction=auction, period=period,units_missing__gt=0)
                                # else:
                                #     short_player_stats_list = Player_stats.objects.filter(auction=auction,period=period, role=Player.RE,units_missing__gt=0)
                                #     # pass
                                #     # .select_related('player')

                                if short_player_stats_list:
                                    for player_stats in short_player_stats_list:
                                        amounth = player_stats.units_missing * treatment.penalty_perunit
                                        player_stats.penalty_phase_total += amounth
                                        player_stats.profit -= amounth
                                        player_stats.save_and_cache()
                                        intermediate_penalty = Penalty(player_stats= player_stats,amounth=amounth, phase=phase, auction=auction)
                                        intermediate_penalty.save()
                                        MasterMan.cache_it("{}player_ser_data".format(player_stats.player_id), None)
                                    Penalty.make_penalty_list(phase)
                                    # log.info('penalty_list',penalty_list)
                                    invalidate_ps(short_player_stats_list)
                                    tt=tt.timer_set(time_length=None, short_time_length= treatment.time_conditional)
                                # tt.cache_me()

                            else: # tt.seconds_left>0 & tt.short_seconds>0
                                log.info("Exception! Error,tt.seconds_left>0 & tt.short_seconds>0")
                                log.debug("Exception! Error,tt.seconds_left>0 & tt.short_seconds>0")
                                # ToDO: this exception was fired while in questionnaire (?!!!)

                            # tt_short.delete()
                            # cache.set('tt_short', '')

                    elif phase.waiting_page:
                        lg_str = "PHASE: {}, START NEXT PERIOD - WITH QUESTIONS".format(phase.idd) + " "
                        log.info(lg_str)
                        MasterMan.cache_it('penalty_list_data', None)
                        period = phase.period
                        period.finished = True
                        period.save_and_cache()

                        #################



                        #################

                        # PHASE=2, WAITING-> NEXT PERIOD (PHASE 1, NOTHING)
                        if period.idd < treatment.total_periods:
                            # log.info("pp", phase.waiting_page)
                            period, phase,question_page = period.next_period_procedure(phase,auction, treatment)
                            # log.info("pp", phase.waiting_page)
                            # timer_set(tt, phase, False, auction)

                            if question_page:
                                # then next period questionpage
                                timet =treatment.time_for_question_page
                            else:
                                timet = treatment.time_for_forward_1
                            tt=tt.timer_set(timet)
                            # tt.cache_me()
                            # log.info("pp",phase.waiting_page)
                            # return redirect(tmpl)

                        elif period.idd >= treatment.total_periods:
                            # PHASE=2, WAITING -> GO TO NEXT PERIOD/ END AUCTION
                            auction.app =  Auction.QUEST
                            auction.auction_finished = True
                            
                            auction.save_and_cache()
                            cache.set("auction_ser_data", None)
                            Player.refresh_all_players()
            if phase:
                phase_ser = sPhaseSerializer(phase)
                phase_ser_data = phase_ser.data
                data['phase'] = phase_ser_data
                period_ser = sPeriodSerializer(period)
                period_ser_data = period_ser.data
                data['period'] = period_ser_data

            tt_ser = sTimerSerializer(tt)
            tt_ser_data = tt_ser.data
            data['tt']=tt_ser_data
    end = time.time() - start
    log.info(" ---TOTAL AJAX_ADMIN {:.3f}".format(end))
    # log.info(log_string)
    data['UNIQUEIZER'] = UNIQUEIZER
    return JsonResponse(data)

def invalidate_ps(player_stats_list ):
    for player_stat in player_stats_list:
        log.info("player_stats_ser_data".format(player_stat.player_id))
        MasterMan.cache_it("{}player_stats_ser_data".format(player_stat.player_id), None)