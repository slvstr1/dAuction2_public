#!python3
import time, random
import logging
log = logging.getLogger(__name__)
from django.db import transaction
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import  login, logout
from .forms import TreatmentFormParameterValues_uniform, TreatmentFormParameterValues_normal, TimerForm, PlayerForm, TreatmentFormInstanceOnly,TreatmentFormTheoreticalValues,AuctionFormTimeRefreshOnly,AuctionFormRealizedAndSampleValues
from .models import MasterMan
from dAuction2.models import User
from forward_and_spot.models import Player,Phase, Penalty,  Period, Timer, Group, Player_stats, Auction, Treatment
from .functions import get_options
logger = logging.getLogger(__name__)
debug_logger = logging.getLogger('debug_logger')


@login_required(redirect_field_name="login", login_url='master-login_user')
def main(request, tmpl='', data={}):

    start = time.time()
    user = request.user
    # print("request:{}".format(request))
    # print("request.POST:{}".format(request.POST))
    # print("request.GET:{}".format(request.GET))
    # print("request.COOKIES:{}".format(request.COOKIES))
    # print("request.user:{}".format(request.user))
    # log.info("sub_on_main_1")

    # need_refreshing_set = cache.get('need_refreshing_set')
    if not user.logged_in:
        log.info("&" * 20)
        log.info("user {} logged out".format(user))
        log.info("&" * 20)
        # user.logout_user(request)
        logout_user(request)
    # log.info("sub_on_main2")
    # print("sub_on_main2")
    admin = cache.get("admin")
    if not admin:
        admin = User.objects.get(pk=User.ADMIN)
        cache.set("admin",admin)
    auction, treatment = Auction.cache_or_create_auction()

    # if user.pk != 99: # thus not admin
    if user.pk != User.ADMIN:
        if user.last_player:
            log.info("user.last_player:{}".format(user.last_player))
            id = user.last_player
            player = Player.objects.filter(auction=auction, id=id,user__isnull=True).order_by('id').last()
            if player:
                player.user=user
                player.save()
                log.info("player.user:{}".format(player.user))
        if auction.player_stats_created:
            try:
                player = user.player.get(auction=auction)
                log.info("auction:".format(auction))
            except Player.DoesNotExist:
                # you cant create player now, as distributions have been created already!
                log.info("sub on main 5")
                log.info("player does not exist for user:{}".format(user))
                user.FCRP_LATE()
                data = {"auction": auction,
                        "message": "The auction parameters have been set already. Solution: either exclude participant, or recreate the auction parameters"}
                tmpl = 'master/failed_to_create_player.html'
                return render(request, tmpl, context=data)
        try:
            player = user.player.get(auction=auction)
        except Player.DoesNotExist:
            log.info("Player.DoesNotExist")
            player = Player.createPlayer(user, auction)
            if not player:
                data = {"auction": auction,
                        "message": "<h2>There is are no free spots anymore.</h2> <h2> Solution: either exclude participants, or recreate the auction with more participants </h2>"}
                tmpl = 'master/failed_to_create_player.html'
                # admin = cache.get("admin")
                return render(request, tmpl, context=data)
        tmpl='instructions-main'
        end = time.time() - start
        log_string = "def master.main: {}, for user_id:{}".format(round(end, 4),request.user.id)
        log.info(log_string)
        # print(log_string)
        return redirect(tmpl)

    # beyond this point only Admin dwells (subjects have been redirected to Instructions-main)
    master_man = MasterMan.cache_or_create_mm()
    # print("master_man:{}".format(master_man ))
    # print("master_man.view:{}".format(master_man.view))
    auction, treatment = Auction.cache_or_create_auction()
    log.info("no of treatments:{}".format(Treatment.objects.count()))
    log.info("master_man = MasterMan.cache_or_create_mm()")

    log.info(f"master_man.view:{master_man.view}")

    if master_man.view != MasterMan.PARAMETERS:
        # print("redirect")
        return_redirect = MasterMan.get_screen_view_value(master_man.view)
        log.info("redirect now to {}, {}".format(return_redirect,master_man.view))
        return redirect('master_earnings')

    # log.info("src_file_exists, src_name_list = treatment.hardcoded_pics")
    src_file_exists, src_name_list = treatment.hardcoded_pics
    # print("master_man:{}".format(master_man))
    # print("master_man.show_unselected:{}".format(master_man.show_unselected))
    player_list = master_man.get_selection(auction)
    # if master_man.show_unselected:
    #     player_list = Player.objects.filter(auction=auction,selected=True).order_by('user__ip','user_id', 'group_id')
    # else:
    #     player_list = Player.objects.filter(auction=auction).order_by('-selected','user__ip','user_id', 'group_id')
    pa_group_num = player_list.order_by('group').distinct('group').count()
    pa_RE_total_num = player_list.filter(role=Player.RE).count()
    pa_PR_total_num = player_list.filter(role=Player.PR).count()
    luser_list= User.objects.filter(fail=True)

    if player_list and not auction.players_one_logged:
        auction.players_one_logged=True
        auction.save()
        auction.save_and_cache()
    auction.players_all_logged= (player_list.count() == treatment.PR_per_group + treatment.RE_per_group)
    auction.save_and_cache()

    if treatment.distribution_used == Treatment.UNIFORM:
        TreatmentFormParameterValues = TreatmentFormParameterValues_uniform
    else:
        TreatmentFormParameterValues = TreatmentFormParameterValues_normal

    treatmentFormParameterValues = TreatmentFormParameterValues(initial={'total_groups':treatment.total_groups,
                               "PR_per_group":treatment.PR_per_group,
                               "RE_per_group":treatment.RE_per_group,
                               'shedding': treatment.shedding,
                               'groups_assignment_alternate':treatment.groups_assignment_alternate,
                               'a':treatment.a,
                               'd_draws_needed':treatment.d_draws_needed,
                               'distribution_used': treatment.distribution_used,
                               'uniform_min': treatment.uniform_min,
                               'uniform_max': treatment.uniform_max,
                               'mu':treatment.mu, 'sigma':treatment.sigma, 'retail_price':treatment.retail_price, 'ECU_per_CZK_PR':treatment.ECU_per_CZK_PR,'ECU_per_CZK_RE':treatment.ECU_per_CZK_RE,'start_capital_in_CZK':treatment.start_capital_in_CZK,
                              })
    auctionFormTimeRefreshOnly= AuctionFormTimeRefreshOnly(initial={
        'time_refresh_data': auction.time_refresh_data})
    auctionFormRealizedAndSampleValues = AuctionFormRealizedAndSampleValues(initial={
        # 'instruction_totalPages': auction.instruction_totalPages,
        'testing_totalquestions': auction.testing_totalquestions,
        'demand_avg': auction.demand_avg,
        'price_avg': auction.price_avg,
        'demand_sd': auction.demand_sd,
        'price_sd': auction.price_sd,
        'cov_DP': auction.cov_DP})
    treatmentFormInstanceOnly = TreatmentFormInstanceOnly(initial={'treatment': treatment.idd}, instance=treatment, auctionid=auction.id)
    treatmentFormTheoreticalValues = TreatmentFormTheoreticalValues(initial={
        'demand_avg_theory': treatment.demand_avg_theory,
        'price_avg_theory': treatment.price_avg_theory,
        'demand_sd_theory': treatment.demand_sd_theory,
        'price_sd_theory': treatment.price_sd_theory,
    })
    timerForm = TimerForm(initial={
                                 'time_for_instructions':treatment.time_for_instructions,
                                 'time_for_distribution':treatment.time_for_distribution,
                                 'time_for_forward_waiting': treatment.time_for_forward_waiting,
                                 'time_for_spot_1': treatment.time_for_spot_1,
                                 'time_for_spot_2': treatment.time_for_spot_2,
                                 'time_for_spot_3': treatment.time_for_spot_3,
                                 'time_for_forward_1': treatment.time_for_forward_1,
                                 'time_for_forward_2': treatment.time_for_forward_2,
                                 'time_for_spot_waiting': treatment.time_for_spot_waiting,
                                 'time_for_question_page': treatment.time_for_question_page,
                                 'time_for_testing': treatment.time_for_testing,
                                 'total_periods': treatment.total_periods,
                                 'time_conditional': treatment.time_conditional,
                                 'qp_every': treatment.qp_every,
                                 'time_refresh_check': treatment.time_refresh_check,
                                 })

    player=player_list.last()
    group= Group.cache_get()
    if not (group) and Group.objects.exists():
        group= Group.objects.filter(auction=auction).last()     # why idd=1???
        # MasterMan.cache_me("group", group)
        if group:
            group.save_and_cache()
        else:
            group = None
    else:
        group=None
    form_player = PlayerForm(initial={'player':player,'group':group})
    tmpl='master/master.html'
    need_refreshing_set = cache.get("need_refreshing_set")
    time_now = int(time.time())
    player_list_users = player_list.filter(user__isnull=False)
    for player in player_list_users:
        key_p = player.user_id
        if need_refreshing_set:
            player.page_need_refreshing = (key_p in need_refreshing_set)
        else:
            player.page_need_refreshing = False
        key_p_last_refresh_date = "{}last_alive".format(key_p)
        last_refresh_date = cache.get(key_p_last_refresh_date)
        if not last_refresh_date:
            last_refresh_date = time_now
            player.last_alive = 0
        else:
            last_alive = min(99, time_now - last_refresh_date)
            if last_alive > 90:
                last_alive -= random.randint(10, 20)
            player.last_alive = last_alive
        player.save()

    data={'src_file_exists':src_file_exists,'failed_users':luser_list,'players':player_list,"auction":auction,"treatmentFormInstanceOnly":treatmentFormInstanceOnly,"treatmentFormTheoreticalValues":treatmentFormTheoreticalValues, "treatmentFormParameterValues":treatmentFormParameterValues,"timerForm":timerForm,'form_player':form_player, 'treatment':treatment, 'auctionFormTimeRefreshOnly':auctionFormTimeRefreshOnly,'auctionFormRealizedAndSampleValues':auctionFormRealizedAndSampleValues,"pa_group_num":pa_group_num,"pa_RE_total_num":pa_RE_total_num,"pa_PR_total_num":pa_PR_total_num,'view':master_man.view,'show_table': master_man.show_table, 'show_unselected':master_man.show_unselected, 'master_man':master_man}


##########################################
    # only for testing the new timers!!!
    # ToDo: can go?
    tt= Timer.cache_get()
    if not tt:
        tt = Timer.objects.get_or_create(pk=1)[0]
        tt.cache_me()
    new_data={'tt':tt}
    player1=player_list.first()

    period= Period.cache_get()
    if not period:
        period=Period.objects.filter(auction=auction).order_by('id').last()
    player_stats = Player_stats.objects.filter(auction=auction, player=player1).filter(period=period)
    new_data['player_stats']=player_stats
    data.update(new_data)
    # ToDo: can go?
    # only for testing the new timers!!!
###########################################

    return render(request, tmpl, context=data)


def login_user(request):
    # Dangerous for internet!!! start
    log.info("login_user")
    # start = time.time()
    auction, treatment = Auction.cache_or_create_auction()

    if not auction.users_created:
        # log.info('users_create(auction)')
        auction.users_created = User.users_create(auction)
        auction.save_and_cache()
    user = request.user
    if user:
        if not user.is_anonymous:
            log.info("user RECOGNIZED rrrrrrrrrrrrrrrrrrrr".format(request.user))
            tmpl = 'master-main'
            return redirect(tmpl)

    logout(request)
    master_man = MasterMan.cache_or_create_mm()
    if master_man.ip_login:
        pass
    print("before requestPost")
    # master_man.ip_login = True
    # master_man.save_and_cache()


    if request.POST:
        user_ip = request.POST['ip'][-3:]
        print("request.POST: {}".format(request.POST))
        if 'login_to_existing_account' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            print("user:{}".format(user))
            if not user:
                logout(request)
                return HttpResponseRedirect("/login")

            user.ip = request.POST['ip'][-3:]
            log.info("user.ip:{}".format(user.ip))
            request.session['username'] = user.username
        elif 'ip_login_to_new_account' in request.POST:

            user_ip1 = request.POST['ip'][-2:]
            # if not isinstance(user_ip1, int):
            #     log.info("IP is not an integer")
            if user_ip1.isdigit():
                user_ip1 = int(user_ip1)
            else:
                log.info("IP is not an integer")
            if not 0< user_ip1 < 40:
                log.info("IP out of range")


            print("iplogin: u{}".format(user_ip1))
            print("ip: {}".format(user_ip))
            if user_ip1 <10:
                username = "u0{}".format(user_ip1)
            else:
                username = "u{}".format(user_ip1)
            user = authenticate(username=username, password=username)
            print()
            if user:
                user.ip = user_ip
            else:
                log.error("no user created")
        elif 'login_to_new_account' in request.POST:
            # log.info("TRUE+++++++++++++++++++++++++++++++++++++++++++++++++++++")
            if 'username' in request.session and False:
                username = request.session['username']
                log.info('RECOGNIZED............')
            else:
                user_list= User.objects.filter(logged_in=False).exclude(username='admin').order_by('username')
                new_user = user_list.first()
                username=new_user.username
            # log.info("new_user:", new_user)

            user = authenticate(username=username, password=username)
            user.ip=user_ip
            log.info("user.ip:{}".format(user.ip))
            request.session['username']=user.username
            log.info("request:{}".format(request))
            log.info("request.POST:{}".format(request.POST))
            log.info("request.POST['ip']:{}".format(request.POST['ip']))
            log.info("request.META:{}".format(request.META))
            # log.info(request.session)
            # log.info("user:",user)

        if user is not None and user.is_active:
            login(request, user)
            user.logged_in=True
            user.save()
            log.info("logged in user:{}".format(user))
            auth.login(request, user)
            return HttpResponseRedirect('/')

    # ToDo: can go?
    if not Auction.objects.exists():
        auction = Auction(pk=1)
        auction.save()
        # create_auction(auction)
    auction, treatment = Auction.cache_or_create_auction()
    # treatment = Treatment.cache_or_create_treatment(auction)
    # auction = Auction.objects.get(active=True)
    # ToDo: can go?

    context = {'auction':auction, 'treatment':treatment, 'master_man':master_man}
    # end = time.time() - start
    return render(request, 'master/login.html', context)


def logout_user(request):
    start = time.time()
    # auction = cache.get("auction")
    # treatment = Treatment.cache_or_create_treatment()
    auction, treatment = Auction.cache_or_create_auction()
    if not auction:
        auction = Auction.objects.get(active=True)
        auction.save_and_cache()

    user = request.user
    try:
        player = user.player.get(auction=auction)

    except Player.DoesNotExist:
        log.info("Player with user {} does not exist".format(user)) # also admin can get here
        logout(request)
        return HttpResponseRedirect("/login")
    except AttributeError:
        log.info("'AnonymousUser' object has no attribute 'player' with user {}".format(user))
        logout(request)
        return HttpResponseRedirect("/login")

    player.user = None
    player.save()
    user.logged_in = False
    log.info("self.logged_in = False__ in logout_user")
    user.fail = False
    user.save()
    logout(request)
    end = time.time() - start
    log_string = "def logout_user:{}, for user_id: {}".format(round(end, 4), request.user.id)
    log.info(log_string)
    return HttpResponseRedirect("/login")


def parameters_set(request, tmpl='master-main', data={}):
    start = time.time()
    cache.set("cache_duration",None)
     # if this is a POST request we need to process the form data
    auction, treatment = Auction.cache_or_create_auction()
    # auction = Auction.cache_get()
    # treatment = Treatment.cache_or_create_treatment(auction)
    if not auction:
        auction=Auction.objects.get(active=True)
        # auction.save()
        auction.save_and_cache()
    if treatment.distribution_used==Treatment.NORMAL:
        form = TreatmentFormParameterValues_normal(request.POST or None, instance=treatment)
    else:
        form = TreatmentFormParameterValues_uniform(request.POST or None, instance=treatment)

    if form.is_valid():
        form.save()
        log.info("saved form of treatmentFormParameterValues:{}".format(form))
    # print("treatment:{}".format(treatment))
    # print("treatment.idd:{}".format(treatment.idd))
    # print("request.POST:{}".format(request.POST))
    form = TreatmentFormInstanceOnly(request.POST or None, instance=treatment, auctionid=auction.id)
    # log.info("form:{}".format(form))
    # log.info("request.POST:{}".format(request.POST))
    log.info("before form is valid check")
    log.info("form:{}".format(form))

    if form.is_valid():
        # DONT DO form.save(): that would edit treament idd!!! :D :D :D
        log.info("treatment:{}, active:{}".format(treatment.id,treatment.active))
        log.info("request.POST:{}".format(request.POST))
        treatment_selected_idd = int (request.POST['idd'])
        Treatment.objects.exclude(idd=treatment_selected_idd,au=auction.id).update(active=False)
        log.info("treatment_selected_idd:{}".format(treatment_selected_idd))
        # Treatment.objects.filter(idd=treatment_selected_idd,au=auction.id).order_by('id').last().update(active=True)
        treatment = Treatment.objects.filter(idd=treatment_selected_idd,au=auction.id).order_by('id').last()
        treatment.active=True
        # ToDo: clean this nasty nasty hack! ;(
        auction.treatment =treatment
        auction.save_and_cache()
        treatment.save_and_cache()

    form = TreatmentFormTheoreticalValues(request.POST or None, instance=treatment)
    if form.is_valid():
        form.save()
        log.info("saved form of TreatmentForm2:{}".format(form))

    timer_form = TimerForm(request.POST or None, instance=treatment)
    if timer_form.is_valid():
        timer_form.save()
    if treatment.qp_every > treatment.total_periods:
        treatment.qp_every = treatment.total_periods
        treatment.save_and_cache()
    auctionFormTimeRefreshOnly = AuctionFormTimeRefreshOnly(request.POST or None, instance=auction)
    # log.info("form_a2:{}".format(auction_form1))
    if auctionFormTimeRefreshOnly.is_valid():
        auctionFormTimeRefreshOnly.save()
        log.info("saved a2. auction 1")
    # auction.time_refresh_data=treatment.time_refresh_data
    auction.save(update_fields=['time_refresh_data'])
    auction.cache_me()
    treatment.save_and_cache()
    end = time.time() - start
    log_string = "def parameters_set: {}".format(round(end, 4))
    log.info(log_string)
    return redirect(tmpl)


@login_required(redirect_field_name="login", login_url='master-login_user')
@transaction.atomic
def set_state(request, tmpl='master-main', data={}):
    log.info("SETSTATE----------------------------------------------")
    start = time.time()
    # postcount = 0

    if request.POST:
        log.info("POST---{}".format(request.POST))
        # log.info('demand_draws_create' in request.POST )
        # log.info('demand_draws_create' in request.POST['name'])
        # print('demand_draws_delete' in request.POST['name'])
        auction, treatment = Auction.cache_or_create_auction()
        # log.info("auction.distribution_auction_created:{}".format(auction.distribution_auction_created))
        tt = Timer.cache_or_create_timer()
        if "name" in request.POST:
            request_POST_name = request.POST["name"]
            if request_POST_name:
                # log.info("auction.distribution_auction_created:{}".format(auction.distribution_auction_created))
                # print("auction_in_name:{}".format(auction))
                options_set_state_request, options_set_state_treatment, options_set_state= get_options(treatment,auction,tt)
                # options_set_state_auction
                # log.info("auction.distribution_auction_created:{}".format(auction.distribution_auction_created))
                # if request_POST_name in options_set_state_auction:
                #     options_set_state_auction[request_POST_name](auction)
                if request_POST_name in options_set_state:
                    options_set_state[request_POST_name]()
                elif request_POST_name in options_set_state_request:
                    options_set_state_request[request_POST_name](request)
                elif request_POST_name in options_set_state_treatment:
                    options_set_state_treatment[request_POST_name](treatment)
                    # options_set_state_treatment[request_POST_name]
                elif "delete_treatments_keep_data" in request.POST['name']:
                    auction_list = [auction,]
                    treatment_list = [treatment, ]
                    Treatment.treatments_delete(auction_list, treatment_list)
                elif "delete_treatments" in request.POST['name']:
                    auction_list = Auction.objects.all()
                    treatment_list = Treatment.objects.all()
                    Treatment.treatments_delete(auction_list, treatment_list )
            # log.info("auction.distribution_auction_created:{}".format(auction.distribution_auction_created))
    end = time.time() - start
    log_string = "set_state_time:{}".format(round(end, 4))
    log.info(log_string)
    return redirect(tmpl)


@login_required(redirect_field_name="login", login_url='master-login_user')
def master_screen_select(request, tmpl='master-main', data={}):
    # start = time.time()
    if request.POST:
        # print(f"request.POST:{request.POST}")
        if "master_view" in request.POST:
            request_post = request.POST['master_view']
            master_man = MasterMan.cache_or_create_mm()
            master_man_view = MasterMan.translate_navlinknames_mmparameters(request_post)
            # log.info(f"master_man_view:{master_man_view, type(master_man_view) }")
            master_man.view =master_man_view
            return_redirect = MasterMan.get_screen_view_value(master_man_view)
            master_man.save_and_cache()
            log.info(f"redirect now to {return_redirect}")
            return redirect(return_redirect)
    return redirect(tmpl)


def subject_select(request, tmpl='master-main', data={}):
    start = time.time()
    if request.POST:
        # print("request.POST:{}".format(request.POST))
        log.info("request.POST:{}".format(request.POST))
        # print('show_selection_toggle' in request.POST)
        # auction= Auction.cache_get()
        master_man = MasterMan.cache_or_create_mm()
        if 'q' in request.POST:
            # print("qinreq")
            try:
                pk = int(request.POST['q'])
                selected_user = User.objects.get(pk=pk)
            except:
                selected_user=None
                # log.info("NONE")
        else:
            selected_user =None
        # master_man.save_and_cache()

        # does all toggling of master_man object
        master_man.toggler(request.POST)

        if 'logout' in request.POST and selected_user:
            log.info("logout, selected_user.pk:{}".format(selected_user.pk))

            if not (selected_user.id == 99):
                selected_user.logged_in = False
                log.info("self.logged_in = False__ in subject_select")
                selected_user.fail = False
                selected_user.ip = ""
                selected_user.last_player = None

            selected_user.save()
            key_user = str(selected_user.id)
            need_refreshing_set = cache.get("need_refreshing_set")
            if not need_refreshing_set:
                need_refreshing_set = set()
            need_refreshing_set.add(key_user)
            cache.set('need_refreshing_set', need_refreshing_set, 35)
            master_man.save_and_cache()

            # master_man.show_selection = (master_man.show_selection +1 )//2
            # master_man.show_unselected = not master_man.show_unselected
        elif 'name' in request.POST:

            if 'show_selection_toggle' in request.POST['name']:
                master_man = MasterMan.cache_or_create_mm()
                master_man.show_selection_toggle()
                # print("toggle_")

    end = time.time() - start
    log_string = "def subject_select: " + str(round(end, 4)) + "for user_id: " + str(request.user.id)
    log.info(log_string)
    return redirect(tmpl)


def custom_error_view(request, error_code, *args, **kwargs):
    user = request.user
    tmpl = 'master/errors/{}.html'.format(error_code)
    data = {'user': user}
    return render(request, tmpl, data)