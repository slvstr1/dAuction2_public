import logging, time, random
# import  os, uuid
log = logging.getLogger(__name__)
logger = logging.getLogger(__name__)
from datetime import date
from .vouchers import Voucher
from django.db import models
from django.contrib.auth import  login, logout
from django.utils.functional import cached_property
from django.db.models import Sum
from django.http import  HttpResponseRedirect
# should run from /home/vagrant/venv/bin/python
# run manage.py loaddata deployment/db_users.json
from django.core.cache import cache
from master.models import MasterMan

# from dAuction2.models import bulk_update
from django_bulk_update.helper import bulk_update
from dAuction2.models import BaseMethods, BaseTimer, BasePeriod, BasePlayer, BaseGroup, BasePlayer_stats, User
from django.contrib.auth.models import AbstractUser
# from forward_and_spot.functions import assign_leftover
# using this completely breaks the app! (import errors - cyclical imp errors I think)

from .auction import Auction
log = logging.getLogger(__name__)


class Group(BaseGroup):
    auction = models.ForeignKey(Auction,on_delete=models.CASCADE)

    @classmethod
    def get_groups(cls, auction):
        # print("get_groups used!")
        # from forward_and_spot.models import Group
        return Group.objects.filter(auction=auction).all()


class Period(BasePeriod):
    auction = models.ForeignKey(Auction,on_delete=models.CASCADE)

    def next_period_procedure(period, last_phase, auction, treatment):
        # from forward_and_spot.models import Phase, Player
        # period = last_phase.period
        new_period_id = period.idd
        new_period_id += 1
        if (new_period_id - 1) % treatment.qp_every == 0 and not treatment.only_spot:
            log.info("question_page=True")
            # log.info('treatment.qp_every:{}'.format(treatment.qp_every))
            # log.info('(new_period_id-1):{}'.format(new_period_id - 1))
            # log.info('(new_period_id-1) % treatment.qp_every: {}'.format((new_period_id - 1) % treatment.qp_every))
            question_page = True
        else:
            # log.info("treatment:{}".format(treatment))
            log.info("question_page=False")
            # log.info('treatment.qp_every:{}'.format(treatment.qp_every))
            # log.info('(new_period_id-1):{}'.format(new_period_id - 1))
            # log.info('(new_period_id-1) % treatment.qp_every:{}'.format((new_period_id - 1) % treatment.qp_every))
            question_page = False
        period = Period.objects.get_or_create(auction=auction, idd=new_period_id)[0]
        if treatment.only_spot:
            phase = \
            Phase.objects.get_or_create(auction=auction, period=period, idd=2, waiting_page=False)[0]
            phase.question_page = False
        else:
            phase = \
            Phase.objects.get_or_create(auction=auction, period=period, idd=1, waiting_page=False)[0]
            phase.question_page = question_page
        # log.info("pp", phase.waiting_page)
        # period.save()
        phase.save_and_cache()
        # cache.set("phase", phase)
        # MasterMan.cache_me("phase", phase)
        period.save_and_cache()
        # cache.set("period", period)
        # MasterMan.cache_me("period", period)
        lg_str = "phase: {}, idd:{}, waiting:{}, question_page:{}, time:{}, for Admin after save".format(
            phase, phase.idd, phase.waiting_page, phase.question_page,
            phase.end)
        log.info(lg_str)
        player_list = Player.objects.filter(auction=auction, user__isnull=False)
        for player in player_list:
            # player.into_cache()
            player_str = str(player.id)
            cache.set("{}player_ser_data".format(player_str ), None)
            cache.set("{}player_stats_ser_data".format(player_str ), None)
        return period, phase, question_page


class Player(BasePlayer):
    """ A player is one of the subjects. (S)he is a member of a group and has an id in the group.
    """

    NO=0
    INSTR = 1
    DISTR = 2
    TEST = 3
    FS = 4
    QUEST = 5
    PAYOUT=6
    VIEW_APPS = \
        (
            (NO, 'NONE'),
            (INSTR, 'INSTR'),
            (DISTR, 'DISTR'),
            (TEST, 'TEST'),
            (FS, 'FS'),
            (QUEST, 'QUEST'),
            (PAYOUT, 'PAYOUT'),
        )

    PR = 0
    RE = 1

    ROLES = \
        (
            (PR, 'PR'),
            (RE, 'RE'),
        )

    auction = models.ForeignKey(Auction, null=True, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
    app = models.PositiveSmallIntegerField(choices=VIEW_APPS, default=NO)
    test_page= models.PositiveSmallIntegerField(default=1) # this can go!
    testing_finished= models.BooleanField(default=False)
    testing_trials = models.PositiveSmallIntegerField(default=0)
    testing_errors = models.PositiveSmallIntegerField(default=0)
    testing_correct = models.PositiveSmallIntegerField(default=0)
    selected = models.BooleanField(default=True)
    # pageurl= models.CharField(max_length=1, default="")
    draw_id = models.PositiveSmallIntegerField(default=0)
    role = models.PositiveSmallIntegerField(choices=ROLES,default=PR)  # two roles: PRoducer and REtailer
    payout_qs = models.IntegerField(default=0)
    payout_trade = models.IntegerField(default=0)
    pay_period = models.PositiveSmallIntegerField(default=0)
    pay_qs_period =  models.PositiveSmallIntegerField(default=0)
    accuracy = models.FloatField(default=0)
    total_cost = models.IntegerField(default=0)
    total_values = models.IntegerField(default=0)
    player_ready= models.BooleanField(default=False)
    time_spend_reading = models.PositiveSmallIntegerField(default=0)

    @classmethod
    def refresh_all_players(cls, also_not_logged_in=False, only_selected=False, only_unselected=False):
        # from forward_and_spot.models import Player
        # from dAuction2.models import User
        log.info("refresh_all_players3")
        auction = Auction.cache_get()
        # log.info("auction.distribution_auction_created:{}".format(auction.distribution_auction_created))
        #get a list with ids of the user ids to be refreshed
        if also_not_logged_in:
            # get me user_list
            user_list = set(User.objects.exclude(id=99).only("id").order_by('pk').values_list('id',flat=True))
        elif only_selected:
            user_list = set(Player.objects.filter(user__isnull=False,selected=True).order_by('pk').values_list('user_id',flat=True))
            # print("user_list:{}".format(user_list))
            log.info("user_list:{}".format(user_list))
        elif only_unselected:
            user_list = set(
                Player.objects.filter(user__isnull=False, selected=False).order_by('pk').values_list('user_id',
                                                                                                    flat=True))
        else:
            user_list = set(User.objects.filter(logged_in=True).exclude(id=99).only("id").order_by('pk').values_list('id',flat=True))
        need_refreshing_set = user_list
        # for elt in need_refreshing_set:
        #     print("need_refreshing_set elt:{}, type:{}".format(elt, type(elt)))
        cache.set('need_refreshing_set', need_refreshing_set , 35)
        # cache.set('need_refreshing_set', None, 35)

        # lo("need_refresh")
        return


    @classmethod
    def fresh_players(cls, auction, randomarg=False):
        log.info("fresh_players used!!!")
        log.info("random:{}".format(randomarg))
        player_set = Player.fresh_list(auction, randomarg)

        return player_set

    @classmethod
    def init_for_present_app(cls, auction, page, state,draw_id=None):
        if draw_id:
            # cls.objects.filter(auction=auction, selected=True,user__isnull=False).update(page=page, state=state, app=auction.app, draw_id=draw_id)
            cls.objects.filter(auction=auction, user__isnull=False).update(page=page, state=state,
                                                                                          app=auction.app,
                                                                                          draw_id=draw_id)
        else:
            # cls.objects.filter(auction=auction, selected=True, user__isnull=False).update(page=page, state=state, app=auction.app)
            cls.objects.filter(auction=auction, user__isnull=False).update(page=page, state=state,
                                                                                          app=auction.app)

    @classmethod
    def fresh_list(cls, auction, randomarg):
        player_list = cls.objects.filter(auction=auction).all()
        player_list.update(selected=False)
        # player_list = Player.unselect_all(auction)
        if not randomarg:
            player_set = player_list.filter(user__isnull=False).order_by('-testing_finished', 'testing_errors','user_id')
            log.info("player_set:{}".format(player_set))
            print("player_set:{}".format(player_set))
        else:
            log.info("randomarg player_set")
            player_set = player_list.filter(user__isnull=False).order_by('?')
        # player_list = Player.objects.filter(auction=auction).all()
        return player_set

    @classmethod
    def createPlayer(cls, user, auction):
        p_list = cls.objects.filter(auction=auction, user=None).order_by('-selected', 'group_id', 'pk')
        # p_list = Player.objects.annotate(odd=F('pk') % 2).filter(auction=auction, user=None).order_by('-selected', 'group_id', 'odd', 'pk')
        from dAuction2.settings import UNIQUEIZER
        try:
            p = p_list.get(id=(auction.id * UNIQUEIZER) + user.id)
        except cls.DoesNotExist:
            # sorting ok
            log.info("p doesnt exist:{} not in {}".format((auction.id * UNIQUEIZER) + user.id,p_list ))
            p = p_list.first()
        if not p:
            log_string = "more try to connect than planned!"
            log.info(log_string)
            user.FCRP_MANY()
            return None
        # from instructions.models import Page
        # page = Page.objects.all().first()
        # p.pageurl=page.url
        p.user = user
        # log.info("userr", user)
        p.username = user.username  # I know: denormalization for speed
        user.last_player = p.id
        user.SCRP()
        p.save()
        return p

    @property
    def ECU_per_CZK(self):
        treatment = self.auction.treatment
        if self.role == Player.PR:
            return treatment.ECU_per_CZK_PR
        else:
            return treatment.ECU_per_CZK_RE

    def INSTR_app(self):
        self.app = Player.INSTR
        self.page = 1
        self.save()

    def DISTR_app(self):
        self.app = Player.DISTR
        self.page = 0
        # player.app = Player.DISTR
        self.state = 2
        self.save_and_cache()

    def TEST_app(self):
        self.app = Player.TEST
        self.page = 1
        self.save_and_cache()

    def FS_app(self):
        self.app = Player.FS
        self.page = 0
        self.save()

    def QUEST_app(self):
        self.app = Player.QUEST
        self.page = 0
        self.save()

    def PAYOUT_app(self):
        self.app = Player.PAYOUT
        self.page = 0
        self.save()

    def get_pay_qs_period(self, last_round_idd,treatment_qp_every):
        log.info("old round for pay_qs_period: {}".format(self.pay_qs_period))
        r=1 + (treatment_qp_every * (random.randint(0, int((last_round_idd / treatment_qp_every) - .001))))
        log.info("new round for pay_period: {}".format(r))
        return r


class Player_stats(BasePlayer_stats):
    """ Player_stats give the basic attributes of a player for each round
    """
    PR = 0
    RE = 1
    ROLES = \
        (
            (PR, 'PR'),
            (RE, 'RE'),
        )
    auction = models.ForeignKey(Auction,default=None,on_delete=models.CASCADE, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    player = models.ForeignKey(Player,on_delete=models.CASCADE, db_index=True)
    period = models.ForeignKey(Period,on_delete=models.CASCADE, db_index=True)
    role = models.PositiveSmallIntegerField(choices=ROLES, default=PR)  # two roles: PRoducer and REtailer
    group = models.ForeignKey(Group,on_delete=models.CASCADE) #why is this here?
    player_demand = models.PositiveSmallIntegerField(default= 0)
    trading_result = models.IntegerField(default=0)
    trading_result_stage1 = models.IntegerField(default=0)
    total_cost = models.FloatField(default=0)
    total_values = models.FloatField(default=0)
    # the total of the values of the units a retailer purchased
    #nnnn
    profit_accuracy = models.FloatField(default=0)
    end_penalty= models.FloatField(default=0) # endpenalty
    penalty_perunit= models.FloatField(default=0) # penalty per unit - Penalty phase
    penalty_phase_total = models.FloatField(default=0) # total penalty per unit - Penalty phase
    required_units_expectation = models.IntegerField(default=-1)
    price_perfect_expectation = models.IntegerField(default=-1)
    price_real_expectation = models.IntegerField(default=-1)
    question = models.PositiveSmallIntegerField(default=1)
    units_missing = models.SmallIntegerField(default=-1)
    vouchers_used = models.SmallIntegerField(default=0)
    vouchers_negative = models.SmallIntegerField(default=0)
    vouchers_used_stage1 = models.SmallIntegerField(default=0)
    vouchers_negative_stage1 = models.SmallIntegerField(default=0)

    def get_profit_accuracy(player_stats, treatment):
        price_real_accuracy = max(0, 1 - abs(
            (player_stats.price_real_expectation - treatment.price_avg_theory) / treatment.price_avg_theory))
        price_perfect_accuracy = max(0, 1 - abs(
            (player_stats.price_perfect_expectation - treatment.price_avg_theory) / treatment.price_avg_theory))
        # price_accuracy = max(price_perfect_accuracy, price_real_accuracy)
        demand_accuracy = max(0, 1 - abs(
            (player_stats.required_units_expectation - treatment.demand_avg_theory) / treatment.demand_avg_theory))
        accuracy = (price_real_accuracy + price_perfect_accuracy + demand_accuracy) / 3
        return accuracy * treatment.qp_accuracy_fee


    @classmethod
    def get_stats_ser_data(cls, stats, phase):
        from api.serializers import sPlayer_statsSerializer_with, sPlayer_statsSerializer
        # print("before_if")
        # log.info("phase.active_state:{}".format(phase.active_state))
        if phase.idd == Phase.SPOT or phase.waiting_page:
            # stats_ser = sPlayer_statsSerializer_with(stats)
            stats_ser = sPlayer_statsSerializer_with(stats, many=True)
        else:
            # stats_ser = sPlayer_statsSerializer(stats)
            stats_ser = sPlayer_statsSerializer(stats, many=True)
        # print("after_if")
        # print("stats:{}".format(stats))
        # print("stats_ser:{}".format(stats_ser ))
        stats_ser_data = stats_ser.data
        # print("before_return")
        return stats_ser_data

    @classmethod
    def playerStats_create(cls):
        auction, treatment = Auction.cache_or_create_auction()
        from forward_and_spot.functions import assign_leftover, divideTotal, checkMaxObey


        from distribution.models import Distribution
        def demand_share_assing(cls, max_vouchers, auction, player_RE_list, demand_share_list_RE, group, period):
            for player in player_RE_list:
                player_stats = cls.objects.create(auction=auction, group=group, player=player, period=period, role=player.role)
                demand_share_elt_RE = demand_share_list_RE.pop()
                demand_curtailment_warning = False
                player_stats.player_demand, demand_curtailment_warning = checkMaxObey(demand_share_elt_RE, max_vouchers, demand_curtailment_warning)
                player_stats.save_and_cache()
            auction.demand_curtailment_warning =demand_curtailment_warning
            auction.save_and_cache()

        log.info("playerStats_create_called")
        groups = Group.objects.all()
        start = time.time()
        random.seed(auction.id)

        period_list = []
        log.info("periods in auction:{}, {}".format(auction,Period.objects.filter(auction=auction).all().count()))
        log.info("all periods in all auctions:{}".format( Period.objects.all().count()))
        for x in range(1, treatment.total_periods + 1):
            period = Period(idd=x, auction=auction)
            period_list.append(period)
        msg = Period.objects.bulk_create(period_list)

        for group in groups:
            player_list = Player.objects.filter(auction=auction, group=group, selected=True)
            # player_list = Player.objects.filter(auction=auction, group=group)
            # print("player_list:{}".format(player_list))
            # print("auction:{}".format(auction))
            # print("treatment:{}".format(treatment))
            player_RE_list = player_list.filter(role=Player.RE, group=group)
            player_PR_list = player_list.filter(role=Player.PR, group=group)

            log.info('group.id:{}'.format(group.id))
            log.info('player_PR_list:{}'.format(player_PR_list))

            log.info('player_RE_list:{}'.format(player_RE_list ))
            log.info('player_PR_list:{}'.format( player_PR_list))
            to_insert_draw = []
            for period in period_list:
                draw, price_draw = Distribution.get_draws(auction, treatment, x)
                to_insert_draw.append(draw)
                for player_list in (player_RE_list, player_PR_list):
                    len_player_list = len(player_list)
                    if len_player_list>0:
                        demand_share, leftover = divideTotal(draw.demand_draw, len_player_list )
                        demand_share_list = assign_leftover(len_player_list, leftover, demand_share)
                        demand_share_assing(cls, treatment.max_vouchers, auction, player_list, demand_share_list,group, period)
                    else:
                        log.debug("len_player_list_empty!!!")
            msg = Distribution.objects.bulk_create(to_insert_draw)

            player_list2 = Player.objects.filter(auction=auction, group=group)
            # print("player_list2")
            # player_list2 = Player.objects.filter(auction=auction, group=group, selected=True)
            for player in player_list2:
                player.pay_qs_period = player.get_pay_qs_period(treatment.total_periods, treatment.qp_every)
                # print("for player:{}, pay_qs_period:{}, role:{}".format(player, player.pay_qs_period, player.role ))
                player.pay_period = player.get_pay_period(treatment.total_periods, player.pay_qs_period)
                # if player.role==1:
                #     print("Apay_period:{}".format(player.pay_period))
                # if player.pay_period ==0:
                #     print("0forplayer")
                # print("for player:{}, pay_qs_period:{}, pay_period:{}".format(player, player.pay_qs_period,player.pay_period))
                player.save()
            # bulk_update(player_list2, update_fields=['pay_qs_period', 'pay_period'])

        end = time.time()
        log.info("total time:{}".format(end - start, 3))
        auction.player_stats_created = True
        auction.save_and_cache()

    @classmethod
    def get_short_player_stats_list(cls, auction, group, period, treatment_require_units_demanded_on_PR):
        if group:
            if treatment_require_units_demanded_on_PR:
                short_player_stats_list = cls.objects.filter(auction=auction, period=period, group=group, units_missing__gt=0)
            else:
                short_player_stats_list = cls.objects.filter(auction=auction, period=period, group=group,role=Player.RE,
                                                                      units_missing__gt=0)
        else:
            if treatment_require_units_demanded_on_PR:
                short_player_stats_list = cls.objects.filter(auction=auction, period=period,  units_missing__gt=0)
            else:
                short_player_stats_list = cls.objects.filter(auction=auction, period=period, role=Player.RE,
                                                                      units_missing__gt=0)
        return short_player_stats_list


    # @classmethod
    # def get_short_player_stats_list(cls, auction, group, period):
    #     short_player_stats_list = cls.objects.filter(auction=auction, group=group, period=period,units_missing__gt=0).select_related('player')
    #     return short_player_stats_list

    # @cached_property
    def get_units_missing_tot(self):
        return max(0, self.player_demand - self.vouchers_used + self.vouchers_negative)

    @cached_property
    def get_vouchers_used_net(self):
        return self.vouchers_used - self.vouchers_negative

    def __str__(self):  # For Python 2, use __str__ on Python 3
       return "id:{} player:{} period:{}; vouchers(used/neg):({}/{}) trading_res:{} profit:{} pen:{}".format(self.id, self.player_id,self.period_id ,self.vouchers_used,self.vouchers_negative,self.trading_result,self.profit,self.penalty_phase_total)


class Phase(BaseMethods, models.Model):
    FORWARD = 1
    SPOT = 2
    INITIAL = 1
    CONDITIONAL = 2
    PENALTY = 3
    STAGE_CHOICES = (
        (FORWARD, 'Forward Market'),
        (SPOT, 'Spot Market'),)
    STATE_CHOICES = (
        (INITIAL, 'Forward Market'),
        (CONDITIONAL, 'Spot Market'),
        (PENALTY, 'Spot Market'),
    )
    id = models.BigAutoField(primary_key=True, null=False)
    auction = models.ForeignKey(Auction, default=None,on_delete=models.CASCADE)
    period = models.ForeignKey(Period, default=None,on_delete=models.CASCADE)
    idd= models.PositiveSmallIntegerField(choices=STAGE_CHOICES, default=FORWARD, db_index=True)
    waiting_page = models.BooleanField(default=False)
    active_state = models.PositiveSmallIntegerField(choices=STATE_CHOICES, default=INITIAL)
    question_page = models.BooleanField(default=True)
    end = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def save_and_cache(self):
        self.save()
        self.cache_me()

        # self.cache_me()
        return

    def next_phase_procedure(last_phase, auction):
        # log.info('NEXT PHASE PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
        # last_phase=Phase.objects.last()
        period = last_phase.period
        last_phase.end = True  # becomes true as there are only 2 phases # ???

        phase = Phase(auction=auction, period=period, idd=2, waiting_page=False,question_page=False)  # set phase to spot (idd=2)

        # ToDo: check if used at all - SVK: yes, it is... (I could have used if phase.id==2, but I like to keep the option to add more phases)
        phase.save_and_cache()
        last_phase.save()
        player_stats_list = Player_stats.objects.filter(auction=auction, period=period)
        for player_stats in player_stats_list:
            player_stats.trading_result_stage1 = player_stats.trading_result
        bulk_update(player_stats_list, update_fields=['trading_result_stage1'])
        return phase

    def __str__(self):
          # return "Auction {0} created on {1}".format(self.id, self.created)
          return "Phase {0}".format(self.id)


class Timer(BaseTimer):
    waiting_page = models.BooleanField(default=False)
    short_running = models.BooleanField(default=False)
    short_end_time = models.PositiveIntegerField(default=0)
    short_seconds_left = models.IntegerField(default=0)
    # class Meta:
    #     abstract = True
    @classmethod
    def cache_or_create_timer(cls):
        tt = cls.cache_get()
        if not tt:
            tt=Timer()
            tt.save_and_cache()
        return tt


    def short_timer_set(self, short_time_length):
        # time_time = time.time()
        short_time_length = min(self.seconds_left, short_time_length)
        self.short_end_time = int(time.time() + short_time_length)
        self.short_seconds_left = short_time_length
        self.cache_me()
        return self

    def timer_toggle(tt):
        tt.running = not tt.running
        phase = Phase.cache_get()
        if tt.running:
            now = time.time()
            tt.end_time = int(now + tt.seconds_left)
            if phase:
                if phase.CONDITIONAL:
                    tt.short_running = True
                    tt.short_end_time = int(now + tt.short_seconds_left)
        else:
            tt.short_running = False
        tt.save_and_cache()
        # log.info("tt - timer_toggle, tt.sl:", tt.seconds_left)
        return tt


class Penalty(BaseMethods, models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    player_stats = models.ForeignKey(Player_stats, default=None,on_delete=models.CASCADE)
    phase = models.ForeignKey(Phase, default=None,on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, null=True,default=None,on_delete=models.CASCADE)
    amounth = models.PositiveIntegerField(default=0)

    @classmethod
    def make_penalty_list(cls, phase):
        from api.serializers import sPenaltySerializer
        penalty_list = cls.objects.filter(phase=phase)
        log.info('penalty_list:{}'.format(penalty_list))
        penalty_list_ser = sPenaltySerializer(penalty_list, many=True)
        MasterMan.cache_it('penalty_list_data', penalty_list_ser.data)

    @classmethod
    def give_penalty(cls, treatment, auction, group, period, phase):
        from api.serializers import sPlayer_statsSerializer_with

        short_player_stats_list = Player_stats.get_short_player_stats_list(auction, group, period, treatment.require_units_demanded_on_PR)
        # short_player_stats_list = Player_stats.get_short_player_stats_list(auction, group, period)
        if short_player_stats_list:
            units_missing_agg = Player_stats.objects.filter(auction=auction, group=group, period=period, role=Player.RE).aggregate(
                Sum('units_missing'))['units_missing__sum']
            # log.info("units_missing_agg",units_missing_agg)
            units_soldbyPR = Player_stats.objects.filter(auction=auction, group=group, period=period,
                                                         role=Player.PR).first()
            # log.info("units_soldbyPR.vouchers_used ", units_soldbyPR.vouchers_used)
            units_soldbyPR_agg = Player_stats.objects.filter(auction=auction, group=group, period=period, role=Player.PR).aggregate(
                Sum('vouchers_used'))['vouchers_used__sum']
            # log.info("units_soldbyPR_agg ", units_soldbyPR_agg )
            units_negativePR_agg = \
            Player_stats.objects.filter(auction=auction, group=group, period=period, role=Player.PR).aggregate(
                Sum('vouchers_negative'))['vouchers_negative__sum']
            marginal_unit = int(
                0.999 + ((units_soldbyPR_agg - units_negativePR_agg + units_missing_agg) / treatment.PR_per_group))
            # log.info("marginal_unit",marginal_unit)
            # voucher_list= Voucher.objects.all()
            # log.info("voucher_list:", voucher_list)
            # for voucher in voucher_list:
            # log.info("voucher:",voucher)
            marginal_price = Voucher.objects.filter(idd=marginal_unit).values_list('value', flat=True)[0]
            log.info("marginal_price:{}".format(marginal_price))
            penalty_perunit = round(marginal_price * 1.5, 1)
            log.info("penalty_perunit:{}".format(penalty_perunit))

            # units_missing_agg =0
            to_add_player_stats = []
            to_add_intermediate_penalty = []
            for player_stats in short_player_stats_list:
                player_stats.penalty_perunit = penalty_perunit
                player_stats.end_penalty = round(penalty_perunit * player_stats.get_units_missing_tot(), 0)
                player_stats.profit -= player_stats.end_penalty
                player_stats.penalty_phase_total += player_stats.end_penalty
                intermediate_penalty = cls(player_stats=player_stats, amounth=player_stats.end_penalty, phase=phase,
                                               auction=auction)
                intermediate_penalty.save()
                cls.make_penalty_list(phase)
                to_add_player_stats.append(player_stats)
                player_str = str(player_stats.player_id)

                player_stats_ser = sPlayer_statsSerializer_with({player_stats}, many=True)
                player_stats_ser_data = player_stats_ser.data
                # MasterMan.cache_it("{}player_stats_ser_data".format(player_str), player_stats_ser_data, 15)
                cache.set("{}player_stats_ser_data".format(player_str), player_stats_ser_data, 15)
                MasterMan.cache_it("{}player_ser_data".format(player_str), None)
            msg = cls.objects.bulk_create(to_add_intermediate_penalty)
            bulk_update(short_player_stats_list,
                        update_fields=['penalty_perunit', 'end_penalty', 'profit', 'penalty_phase_total'])
        return


# class User(BaseUser, BaseMethods):
    # def logout_user(self, request):
    #     start = time.time()
    #     auction, treatment = Auction.cache_or_create_auction()
    #     if not auction:
    #         auction = Auction.objects.get(active=True)
    #         auction.save_and_cache()
    #     # user = request.user
    #
    #     try:
    #         player = self.player.get(auction=auction)
    #         player.self = None
    #         player.save()
    #     except Player.DoesNotExist:
    #         log.info("Player with user {} does not exist".format(self))
    #
    #     self.logged_in = False
    #     print("self.logged_in = False__ in logout_user")
    #     self.fail = False
    #     self.save()
    #     logout(request)
    #     end = time.time() - start
    #     log_string = "def logout_user:{}, for user_id: {}".format(round(end, 4), self.id)
    #     log.info(log_string)
    #     return HttpResponseRedirect("/login")
    #
    # @classmethod
    # def users_create(cls, auction):
    #     print("users created in users_create(auction)")
    #     log.info("users created in users_create(auction)")
    #     cls.objects.all().delete()
    #     try:
    #         user = cls.objects.create_user(username="admin", is_staff=True, is_superuser=True, password="admin", pk=99)
    #         user.save()
    #     except:
    #         log.debug("Failure users_create")
    #
    #     # generate and createusers 01 - 40
    #     for user_number in range(1, 41):
    #         # transform 2 to 02
    #         user_number = str(user_number).zfill(2)
    #         # create username and pass
    #         user_name = "u" + user_number
    #         user_password = user_name
    #         # create user object itself and save it to db
    #         user = cls.objects.create_user(pk=user_number, username=user_name, password=user_password)
    #         user.save()
    #     return True
    #
    # def LOGGED_OUT(self, auction):
    #     self.state = 1
    #     self.logged_in = False
    #     print("self.logged_in = False__ in LOGGED_OUT")
    #     self.fail = False
    #     self.save()
    #
    # def NO_PL(self):
    #     self.state = 2
    #     self.logged_in = True
    #     self.fail = False
    #     self.save()
    #
    # def FCRP_LATE(self):
    #     self.state = 3
    #     self.fail = True
    #     self.logged_in = True
    #     # self.has_player = False
    #     self.save()
    #
    # def FCRP_MANY(self):
    #     self.state = 4
    #     self.fail = True
    #     # self.has_player = False
    #     self.save()
    #
    # def SCRP(self):
    #     self.state = 5
    #     self.fail = False
    #     # self.has_player = True
    #     self.save()