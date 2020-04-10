import logging, time, random
from forward_and_spot.views import set_offer
from django.http import JsonResponse
from .serializers import sTimerSerializer, sPeriodSerializer, sPhaseSerializer, sTreatmentSerializer, sAuctionSerializer,sPlayer_statsSerializer, sOfferSerializer, sPlayerDrawSerializer, sDistribSerializer,sVSerializer, sPlayerSerializer, sPlayer_statsSerializer_with
from distribution.models import Distribution
from forward_and_spot.models import  Treatment, Offer, Voucher, Player_stats,Phase, Timer, Auction, Player, Period
# from forward_and_spot.models import
from dAuction2.models import User
from master.functions import merge_dicts
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from master.models import MasterMan
from django.core.cache import cache

debug_logger = logging.getLogger('debug_logger')
log = logging.getLogger(__name__)


# API serving auction interface by AJAX

def set_last_refresh_date(user_id):
    last_refresh_date = int(time.time())- random.randint(0,3)
    key_p_last_refresh_date =  '{}last_alive'.format(user_id)
    cache.set(key_p_last_refresh_date, last_refresh_date)

def determine_refreshment_need(user_id, need_refreshing_set):
    pagerefresh_now = False
    if need_refreshing_set:
        pagerefresh_now = (user_id in need_refreshing_set)
    return pagerefresh_now


@csrf_exempt
def get_timer(request):
    tt = Timer.cache_get()
    if not tt:
        try:
            tt = Timer.objects.get(pk=1)
        except Timer.DoesNotExist:
            log.debug("timer does not exist")
            return JsonResponse("timer does not exist", safe=False)
        tt.cache_me()
    tt_ser = sTimerSerializer(tt)
    data = {"timer": tt_ser.data,}
    return JsonResponse(data)


@csrf_exempt
def auction_data(request):
    # how about this:
    # auction_data should calculate for EVERYBODY, then store it in a cache that is valid for 2 seconds. During the validity time, it serves everybody from cache. When not valid anymore, it calculates again for EVERYBODY.
    start = time.time()
    if request.method == 'POST' :
        user_id = int(request.POST.get('user_id'))
        need_refreshing_set = cache.get("need_refreshing_set")
        pagerefresh_now = determine_refreshment_need(user_id, need_refreshing_set)
        if pagerefresh_now:
            data = {}
            data['pagerefresh_now'] = pagerefresh_now
            return JsonResponse(data)

        set_last_refresh_date(user_id)
        # MAY NOT COME BACK
        auction_id = int(request.POST.get('auction_id'))
        player_id = int(request.POST.get('player_id'))

        # player_str = str(player_id)
        group_id = int(request.POST.get('group_id'))
        # group_str = str(group_id)
        # log_string = "USER ID {}".format(user_id)
        phase = Phase.cache_get()

        # print("player_id:{}".format(player_id))

        # debug_logger.debug("phase:{}, for player:{}".format(phase , player_id))

        if not phase:
            try:
                phase = Phase.objects.filter(auction=auction_id).select_related('period').last()
                # phase.un_uniqueize(auction_id)
            except Phase.DoesNotExist:
                missing_object = "Phase"
                log.debug("{} does not exist".format(missing_object))
                data = {}
                # data['pagerefresh_now'] = pagerefresh_now
                return JsonResponse(data)
                # return JsonResponse("{} does not exist".format(missing_object))
            if not phase:
                data = {}
                data['pagerefresh_now'] = pagerefresh_now
                return JsonResponse(data)
            log.info("Created phase: {}".format(phase ))
            phase.save_and_cache()
        period = Period.cache_get()

        # if I comment this out, the auction interface cannot startup!!!
        # debug_logger.debug("period: {} for player:{}".format(period,player_id))
        if not period:
            if phase:
                period = phase.period
            # debug_logger.debug("period NONE!!!" + str(period) + "for player:" + str(player_id))
            # pass
        data = cache.get('{}data'.format(group_id))
        # print("player_id:{}".format(player_id))
        # print("group_id:{}".format(player_id))
        # print("phase.idd:{}".format(phase.idd))
        if data:
            # log_string="OLD_DATA from memcached"
            pass
        else:
            start22 = time.time()
            auction, treatment = Auction.cache_or_create_auction()
            if not auction:
                return JsonResponse("Auction does not exist", safe=False)
            if not (auction.app == Auction.FS):
                return JsonResponse("Not in FS", safe=False)
            cache_duration = cache.get("cache_duration")
            if not cache_duration:
                cache_duration = auction.time_refresh_data * 0.00099
            tt = Timer.cache_get()

            if not tt:
                tt= Timer.objects.get(pk=1)
                tt.cache_me()
            tt_ser = sTimerSerializer(tt)
            phase_ser = sPhaseSerializer(phase)
            # 2. present period object, send single object containing present period
            period_ser = sPeriodSerializer(period)
            # 3. current auction object,  send single object containing present  auction
            auction_ser = sAuctionSerializer(auction)

            treatment_ser_data = cache.get("treatment_ser_data")
            if not treatment_ser_data:
                # treatment = Treatment.cache_or_create_treatment()

                if treatment:
                    treatment_ser = sTreatmentSerializer(treatment)
                    treatment_ser_data = treatment_ser.data
                    MasterMan.cache_it("treatment_ser_data", treatment_ser_data)
            merged_auction_ser_data = merge_dicts(auction_ser.data, treatment_ser_data)

            # 6. my offers in present phase (filtered in React to Cleared - My Trading Account and Noncleared - My Standing offers), array
            all_offers = Offer.objects.filter(canceled=False, auction=auction_id,phase=phase , group_id=group_id)
            all_offers_ser = sOfferSerializer(all_offers, many=True)

            #  7. my vouchers object, array of vouchers for present period
            penalty_list_data = cache.get('penalty_list_data')

            data= {
                        # "timer": timer_seconds_left,
                        "timer": tt_ser.data,
                        "phase": phase_ser.data,
                        "period": period_ser.data,
                        "auction": merged_auction_ser_data,
                        "all_offers_ser":all_offers_ser.data,
                        "penalty_list_data":penalty_list_data
                        }

            MasterMan.cache_it('{}data'.format(group_id), data, cache_duration)
            end22 = time.time() - start22
            # end2 = time.time() - start2
            if end22 > 0.040:
                # cache.set("cache_duration", min(cache_duration * 1.5,10),30)
                MasterMan.cache_it("cache_duration", min(cache_duration * 1.5,10),30)
            else:
                # cache.set("cache_duration", max(cache_duration / 2, auction.time_refresh_data * 0.0011),30)
                MasterMan.cache_it("cache_duration", max(cache_duration / 2, auction.time_refresh_data * 0.00099),30)
            # log_string = "NEW data: {} ___ cache_duration: {}".format(round(end22, 3),cache_duration)
            # log_string = "auction_data: 22 - set refresh" + "for" + str(user_id) + " " + str(round(end22, 3))

        role = cache.get("{}role".format(player_id))
        if not role:
            try:
                player = Player.objects.get(auction_id=auction_id, pk=player_id)
            except Player.DoesNotExist:
                return JsonResponse("Player does not exist", safe=False)
            role = player.role
            # log.info("++++++++++ player taken from id={},{},  role:{}".format(player_id,player.pk, player.role))

            # MasterMan.cache_it(player_str + "role", player.role)
            cache.set("{}role",format(player_id), player.role)
        if role == Player.PR:
            my_vouchers_ser_data = cache.get('my_vouchers_ser')
            if not my_vouchers_ser_data:
                voucher_list = cache.get('voucher_list')
                if not voucher_list:
                    auction = Auction.cache_get()
                    try:
                        voucher_list = Voucher.objects.filter(auction=auction)
                    except Voucher.DoesNotExist:
                        return JsonResponse("Voucher does not exist")

                    cache.set('voucher_list', voucher_list)
                    # MasterMan.cache_it('voucher_list', voucher_list)
                # my_vouchers_ser = vserializer(voucher_list, many=True)
                my_vouchers_ser = sVSerializer(voucher_list, many=True)
                my_vouchers_ser_data = my_vouchers_ser.data
                # cache.set('my_vouchers_ser', my_vouchers_ser_data)
                MasterMan.cache_it('my_vouchers_ser', my_vouchers_ser_data,4)
            data.update({"vouchers": my_vouchers_ser_data, })

        # start3 = time.time()
        player_ser_data = cache.get("{}player_ser_data".format(player_id))
        if not player_ser_data:
            player=Player.objects.get(auction_id=auction_id,pk=player_id)
            player_ser = sPlayerSerializer(player)
            player_ser_data = player_ser.data
            MasterMan.cache_it("{}player_ser_data".format(player_id), player_ser_data, 4)
        player_stats_ser_data = cache.get("{}player_stats_ser_data".format(player_id))

        if not player_stats_ser_data:
            # log.info("NEW PS_DATA")
            player_stats = Player_stats.objects.filter(auction=auction_id, period=period, player=player_id)
            player_stats_ser_data = Player_stats.get_stats_ser_data(player_stats, phase)
            # MasterMan.cache_it("{}player_stats_ser_data".format(player_id), player_stats_ser_data, 15)
            cache.set("{}player_stats_ser_data".format(player_id), player_stats_ser_data, 4)
        # else:
        #     log.info("OLD PS_DATA")
        data.update({"player": player_ser_data,"player_stats": player_stats_ser_data,})
        auction, treatment = Auction.cache_or_create_auction()
        if not auction:
            auction = Auction.objects.get(pk=auction_id)
            auction.cache_me()
        if treatment.test_players and (not phase.waiting_page) and (not phase.question_page):
            log_string = "TEST PLAYERS ON for:{}".format(user_id)
            # log.info(log_string)
            # log.info("auction.test_players")
            if auction.auction_started:
                phase = Phase.objects.filter(auction_id=auction_id).last()
                if (not phase.waiting_page) or (not phase.question_page):
                    if random.randint(1,10)<3:
                        request.POST._mutable = True
                        request.method = "POST"
                        request.POST['priceOriginal'] = str(15 + random.randint(0, 20))
                        request.POST['unitsOriginal'] = str(random.randint(1, 15))
                        request.POST['Type'] = str(random.choice([Offer.BUY, Offer.SELL]))
                        set_offer(request)
                        request.method = "GET"
        # log_string = "auction_data: data" + str(data)
        end = time.time() - start
        log.info("{:.3f} TOTAL_AUCTION_DATA for {}".format(end,user_id))
        # log.info(log_string)
        # if player.role == player_id%2:
        #     print("ERROR!!!: player_id:{},{} player.role:".format(player_id, player.pk,player.role))
        # else:
        #     print("OK: {}".format(player_id%2))

        # role = cache.get("{}role".format(player_id))
        # if player.role == player_id % 2:
        #     print("ERROR!!!: player_id:{},{} player.role:".format(player_id, player.pk, player.role))
        # else:
        #     print("OK")
        # print("group_id:{}".format(player_id))
        # print("phase.idd:{}".format(phase.idd))
        # log.info("+" * 20 + "player_ser_data:{}".format(player_ser_data))
        # if "role" in player_ser_data:
        #     log.info("+" * 20 + " "+"player:{}  ".format(player.id) + "player_ser_data['role']:{}".format(player_ser_data['role']))


            # if player_id==1468833000002:
            #     print("player_id:{}".format(player_id))
            #     print("player_ser_data['id']:{}".format(player_ser_data['id']))
            #     print("role:{}".format(player_ser_data['role']))
            #     assert (player_ser_data['role']==1)
            # elif player_id==1468833000001:
            #     print("player_id:{}".format(player_id))
            #     print("player_ser_data['id']:{}".format(player_ser_data['id']))
            #     print("role:{}".format(player_ser_data['role']))
            #     # print("player_id:{}".format(player_id))
            #     assert (player_ser_data['role']==0)
            # else:
            #     print("impossinle")
            #     print("player_id:{}".format(player_id))
            #     print("player_ser_data['id']:{}".format(player_ser_data['id']))
            #     print("role:{}".format(player_ser_data['role']))
            #     print(player_id == 1468833000002)
            #     print(type(player_id))
            #     raise Exception
        # log.info("+" * 20 + "role:{}".format(player_stats.role))

        return JsonResponse(data)


@csrf_exempt
# get answers for questions in new round
def round_questions(request):
    start = time.time()
    if request.method == 'POST':
        auction, treatment = Auction.cache_or_create_auction()
        if not auction:
            try:
                auction = Auction.objects.get(active=True)
            except Auction.DoesNotExist:
                missing_object = "Auction"
                log.debug("{} does not exist".format(missing_object))
                return JsonResponse("{} does not exist".format(missing_object))

        a1 = request.POST.get("a1")
        a2 = request.POST.get("a2")
        a3 = request.POST.get("a3")
        user = request.user
        user_id=user.id
        player = user.player.get(auction=auction)
        player_id = player.id
        # phase = cache.get("phase")
        phase = Phase.cache_get()
        period = phase.period
        debug_logger.debug("phase: {}, for player{}".format(phase, user_id))
        player_st_filtered = Player_stats.objects.filter(auction=auction).filter( period=period, player_id=player_id)
        player_stats = player_st_filtered.last()
        player_stats.required_units_expectation = a1
        player_stats.price_perfect_expectation = a2
        player_stats.price_real_expectation = a3
        player_stats.save()
        # log.info (a1, a2, a3)
        end = time.time()
        log_string = "def round_questions:{}, for user:{}".format(round(end, 4), user.id)
        log.info(log_string)

        return HttpResponse("")

# API FOR POST
# check if page should be refreshed, if so, refresh, change value in db
@csrf_exempt
def refresh(request):
    ######################
    # Refresh check logic:
    #   Ask every few sec by GET AJAX call, should I refresh ? (get user object and check if pagerefresh_now is true)
    #       TRUE: make POST AJAX call that page will be refreshed,  refresh the page and ask again in few sec
    #       FALSE: ask again in few sec....
    #############
    # this will be changed and the cache will be used to write the refresh status in
    # get the logger for performance
    # write the time to it
    # start timer here
    # do some calls
    # stop the timer, write to log

    start = time.time()
    if request.method =='POST':
        refreshed=int(request.POST.get('refreshed'))
        if request.POST.get('user_id')=='NaN':
            log.info("USER NOT CONNECTED")
            log.info("request.POST:{}".format(request.POST))
            return JsonResponse(False, safe=False)
        else:
            user_id = int(request.POST.get('user_id'))
            # log.info("CONNECTED: {} {}".format(user_id, request.POST ))
            # log.info("request.POST:{}".format(request.POST))
            connected_set = cache.get("connected_set")
            # print("connected_set:{}".format(connected_set))
            if not connected_set:
                connected_set=set()
            connected_set.add(user_id )
            # print("connected_set:{}".format(connected_set))
            MasterMan.cache_me(connected_set,"connected_set",2)
        user_id = int(request.POST.get('user_id'))
        if refreshed==1:
            MasterMan.uncache_me_bool("need_refreshing_set",user_id,45)
            # log_string = "++++ set need refreshing to False for:{}".format(user_id)
            # log.info(log_string)
            return JsonResponse(False, safe=False)

        else:
            need_refreshing_set = cache.get("need_refreshing_set")
            if need_refreshing_set:
                # log.info("need_refreshing_set for user_id: {}".format(user_id))
                if user_id in need_refreshing_set:
                    return JsonResponse(True, safe=False)
            set_last_refresh_date(user_id)
            return JsonResponse(False, safe=False)

    end = time.time() -start
    log_string = "def refresh: {}, for user:{}, request.method:{}".format(round(end, 4), request.user.id, request.method)
    log.info(log_string)
    return HttpResponse('')

@csrf_exempt
def cancel_offer(request):
    # start = time.time()
    # cancel offer with id from post request done by button on auction page
    if request.method =='POST':
        canceled_offer_id = int(request.POST.get("offer_id"))
        group_id = int(request.POST.get('group_id'))
        # log.info("canceled_offer_id: {}".format(canceled_offer_id ))
        # auction=Auction.cache_get()
        treatment = Treatment.cache_or_create_treatment()
        if treatment.register_cancelled:
            Offer.objects.filter(id=canceled_offer_id).update(canceled=True)
        else:
            Offer.objects.filter(id=canceled_offer_id).delete()
        MasterMan.cache_it('{}data'.format(group_id),None)
        return HttpResponse('')

def player_ready(request):
    if request.method == 'GET':
        auction = Auction.cache_get()
        if not auction:
            try:
                auction = Auction.objects.get(active=True)
            except Auction.DoesNotExist:
                missing_object = "Auction"
                log.debug("{} does not exist".format(missing_object))
                return JsonResponse("{} does not exist".format(missing_object))
            auction.save_and_cache()
        player = request.user.player.get(auction=auction)
        player.player_ready = True
        player.save()
    return JsonResponse("", safe=False)


# api call for distribution 1 - get draws from db
def distrib(request):
    if request.method == 'GET':
        # get draws
        auction = Auction.cache_get()
        # auction_f = auction
        if not auction:
            try:
                auction = Auction.objects.get(active=True)
            except Auction.DoesNotExist:
                missing_object = "Auction"
                log.debug("{} does not exist".format(missing_object))
                return JsonResponse("{} does not exist".format(missing_object))

        distr=Distribution.objects.filter(auction=auction).filter(test=True)
        distr_ser=sDistribSerializer(distr, many=True)
        auction_ser = sAuctionSerializer(auction)
        auction_ser_data = auction_ser.data
        treatment_ser_data = cache.get("treatment_ser_data")
        if not treatment_ser_data:
            treatment = Treatment.cache_or_create_treatment(auction)
            # MasterMan.cache_me("treatment", treatment)
            log.info("treatment cached and saved:{}".format(treatment))
            treatment_ser = sTreatmentSerializer(treatment)
            treatment_ser_data = treatment_ser.data
            MasterMan.cache_it("treatment_ser_data", treatment_ser_data)
        merged_auction_ser_data = merge_dicts(auction_ser_data, treatment_ser_data)
        data = {'distr_draws': distr_ser.data}
        data.update({'auction_f': merged_auction_ser_data})
        # get auction
        return JsonResponse(data)


# api call for distribution 2 - get/save my number of draws
@csrf_exempt
def draw(request):
    # get number of player draws
    user_id= request.user.id
    user = User.objects.prefetch_related('player').get(id=user_id)
    auction = Auction.cache_get()
    # Auction.objects.get(active=True)
    if not auction:
        try:
            auction = Auction.objects.get(active=True)
        except Auction.DoesNotExist:
            missing_object = "Auction"
            log.debug("{} does not exist".format(missing_object))
            return JsonResponse("{} does not exist".format(missing_object))
    try:
        player = user.player.get(auction=auction)
    except Player.DoesNotExist:
        missing_object = "player"
        log.debug("{} does not exist".format(missing_object))
        return JsonResponse("{} does not exist".format(missing_object))

    if request.method == 'GET':
        # player_id = player.id
        # log.info player_id
        cur_player= Player.objects.select_related('auction').get(auction=auction,user_id=user_id)
        #cur_player = Player.objects.filter(auction=auction).filter(player=player)
        cur_player_ser=sPlayerDrawSerializer(cur_player)
        # log.debug(cur_player_ser.data)
        data = {'cur_draw': cur_player_ser.data}
        return JsonResponse(data)
    # POST player draws from distrib app
    if request.method =='POST':
        auction, treatment = Auction.cache_or_create_auction()
        if auction.app == Auction.DISTR:
            new_draw_n = request.POST.get("new_draw_n")
            # player=request.user.player
            if new_draw_n=="done":
                # player.FINISHED()
                player.state=3
                player.save()
                # FINISHED=3
            else:
                player.draw_id=new_draw_n
                player.page=player.draw_id
                player.save()
            return HttpResponse('')


@csrf_exempt
def history_data(request):
    if request.method == 'POST' :
        ## ids returned from React with POST request
        auction_id = int(request.POST.get('auction_id'))
        player_id = int(request.POST.get('player_id'))
        phase = Phase.cache_get()
        if not phase:
            try:
                phase = Phase.objects.last()
            except Phase.DoesNotExist:
                missing_object="phase"
                log.debug("{} does not exist".format(missing_object))
                return JsonResponse("{} does not exist".format(missing_object))

        #     cache.set("phase", phase)
        period = Period.cache_get()
        if not period:
            period = phase.period
        # player_str=str(player_id)
        try:
            player_stats = Player_stats.objects.filter(auction=auction_id, player=player_id,period_id__lte=phase.period_id)
        except Player_stats.DoesNotExist:
            missing_object = "Player_stats"
            log.debug("{} does not exist".format(missing_object))
            return JsonResponse("{} does not exist".format(missing_object))

        player_stats_ser = sPlayer_statsSerializer_with(player_stats, many=True)
        data = {'history': player_stats_ser.data}
        return JsonResponse(data)