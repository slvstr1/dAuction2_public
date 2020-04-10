import time, math, random, logging, os, datetime, uuid, gzip
# from django.contrib.auth import  login, logout
# from django_bulk_update.helper import bulk_update
# from django.db.models import Avg, Sum, Max, Min, Func
from django.http import JsonResponse, HttpResponseRedirect
from io import StringIO
from django.db import connection, models, transaction
from django.apps import apps
from django.core.cache import cache
from datetime import date
from django.conf import settings
# from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
# from django.utils.functional import cached_property
from datetime import datetime
from django.core.management import call_command

from django.contrib.auth.models import UserManager
from django.core.cache import cache
log = logging.getLogger(__name__)

# dAuction -> BaseGame # has the modules:
# BaseAuction (BaseGame), BaseTreatment, BasePlayer, BasePeriod, BasePhase, BasePlayer_stats, BaseUser, (BasePage?), BaseTimer


class User(AbstractUser):
    ADMIN = 99
    LOGGED_OUT = 1
    NO_PL= 2
    FCRP_LATE = 3
    FCRP_MANY = 4
    SCRP = 5
    VIEW_STATES = \
        (
        (LOGGED_OUT, 'LOGGED_OUT'),
        (NO_PL, 'NO_PL'),
        (FCRP_LATE, 'Fcrp_2late'),
        (FCRP_MANY, 'Fcrp_2many'),
        (SCRP, 'SCRP:)'),
        )
    state = models.PositiveSmallIntegerField(choices=VIEW_STATES, default=LOGGED_OUT)
    page_need_refreshing = models.BooleanField(default=False)
    logged_in = models.BooleanField(default=False)
    last_player = models.BigIntegerField(default=None,null=True)
    fail= models.BooleanField(default=False)
    last_refresh_date = models.DateTimeField(default =date(2002, 12, 4))
    last_alive = models.SmallIntegerField(default=-1)
    ip=models.CharField(max_length=35, default="")


    # def logout_user(self, request):
    #     from forward_and_spot.models import Auction, Player
    #     from master.views import logout
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

    @classmethod
    def users_create(cls, auction):
        # print("users created in users_create(auction)")
        log.info("users created in users_create(auction)")
        cls.objects.all().delete()
        try:
            user = cls.objects.create_user(username="admin", is_staff=True, is_superuser=True, password="admin", pk=99)
            user.save()
        except:
            log.debug("Failure users_create")

        # generate and createusers 01 - 40
        for user_number in range(1, 41):
            # transform 2 to 02
            user_number = str(user_number).zfill(2)
            # create username and pass
            user_name = "u" + user_number
            user_password = user_name
            # create user object itself and save it to db
            user = cls.objects.create_user(pk=user_number, username=user_name, password=user_password)
            user.save()
        return True

    def LOGGED_OUT(self, auction):
        self.state = 1
        self.logged_in = False
        # print("self.logged_in = False__ in LOGGED_OUT")
        self.fail = False
        self.save()

    def NO_PL(self):
        self.state = 2
        self.logged_in = True
        self.fail = False
        self.save()

    def FCRP_LATE(self):
        self.state = 3
        self.fail = True
        self.logged_in = True
        # self.has_player = False
        self.save()

    def FCRP_MANY(self):
        self.state = 4
        self.fail = True
        # self.has_player = False
        self.save()

    def SCRP(self):
        self.state = 5
        self.fail = False
        # self.has_player = True
        self.save()

class BaseMethods(object):

    # def un_uniqueizer(self, auction_id):
    #     self.id



    @classmethod
    def cache_get(self):
        name = self.__name__
        # print("name:{}".format(name))
        return cache.get(name)

    def cache_me(self, object_to_cache_name=None,  timeout=None, cache_set_name="cache_set"):

        if not object_to_cache_name:
            object_to_cache_name = self.__class__.__name__
        # log.info("object_to_cache_name:{}".format(object_to_cache_name))
        cache.set(object_to_cache_name, self, timeout)
        cache_set = cache.get(cache_set_name)
        if cache_set:
            cache_set.add(object_to_cache_name)
        else:
            cache_set = {object_to_cache_name, }
        cache.set(cache_set_name, cache_set)

    @classmethod
    def delete_all_objects(cls, auction=None):
        """
        Removes all objects with fk=auction
        """
        log.info("delete_all_objects!")
        log.info("auction:{}".format(auction))
        log.info("cls:{}".format(cls))
        if auction:
            cls.objects.filter(auction=auction).delete()
        else:
            cls.objects.all().delete()
            pass
            # print("nothing deleted")


class BaseMasterMan(BaseMethods, models.Model):
    class Meta:
        abstract = True

    #ToDo: repetitious! How to make this DRY???
    def save_and_cache(self):
        self.save()
        self.cache_me()
        return

    @classmethod
    def get_time_stamp(cls):
        import datetime
        now = datetime.datetime.now()
        return f"{now.isoformat()}"

    @classmethod
    def cache_or_create_mm(cls):
        mm = cls.cache_get()
        # mm=None
        # log.info("in cache_or_create_mm(cls)")
        if not mm:
            log.info("not mm")
            if cls.objects.exists():
                log.info("object exist")
                try:
                    mm = cls.objects.get(pk=1)
                    mm.save_and_cache()
                except cls.DoesNotExist:
                    log.info("except cls.DoesNotExist")
                    mm = cls(pk=1)
                    mm.save_and_cache()
            else:
                log.error("ERROR: mm does not exist!")
                log.info("ERROR: mm does not exist!")
                mm = cls(pk=1)
                mm.save_and_cache()
            log.info("before cache_me mm")
            # mm.cache_me()
            log.info("mm cached and saved:{}".format(mm))
        return mm

    @classmethod
    def uncache_me_bool(cls, uncache_set_name, object_to_uncache_name, timeout=None):
        # log.info("uncache_me!_ uncache_set_name ={}".format(uncache_set_name))
        uncache_set = cache.get(uncache_set_name)
        log.info("object_to_uncache_name:{}".format(object_to_uncache_name))
        # log.info("uncache_set ",uncache_set )
        if uncache_set:
            # log.info("KNOWS cache set with name {}".format(uncache_set_name))
            if object_to_uncache_name in uncache_set:
                # log.info("object in cache set  {}".format(object_to_uncache_name))
                uncache_set.remove(object_to_uncache_name)
                cache.set(uncache_set_name, uncache_set, timeout)

    @classmethod
    def cache_it(cls,object_to_cache_name, object_to_cache, timeout=None, cache_set_name="cache_set"):
        # log.info("object_to_cache_name:{}".format(object_to_cache_name))
        cache.set(object_to_cache_name, object_to_cache, timeout)
        cache_set = cache.get(cache_set_name)
        if cache_set:
            cache_set.add(object_to_cache_name)
        else:
            cache_set = {object_to_cache_name, }
        cache.set(cache_set_name, cache_set)

    @classmethod
    def invalidate_caches(cls):
        log.info("call_invalidate_caches")
        caches_set = cache.get("cache_set")
        log.info("caches_set:{}".format(caches_set))
        if caches_set:
            for cache_name in caches_set:
                cache.set(cache_name, None)
        cache.set("cache_set", None)
        cache.set('treatment', None)


    def toggle_no_test(self):
        from forward_and_spot.models import Auction
        auction, treatment = Auction.cache_or_create_auction()
        treatment.allow_automatic_login = False
        treatment.allow_multiple_offers = False
        treatment.test_mode= False
        auction.make_instruction_pdf = False
        auction.show_ids = False
        treatment.only_spot = False
        treatment.pay_one_random_period = True
        treatment.test_players = False
        treatment.test_script = False
        treatment.educational = False
        treatment.save_and_cache()
        auction.save_and_cache()
        self.no_test=True
        self.save_and_cache()




    @classmethod
    def cache_or_create_options(MasterMan):
        # from django.core.cache import cache
        options = cache.get("options")
        if not options:
            options = {
                "PARAMETERS": MasterMan.PARAMETERS,
                "DATA": MasterMan.DATA,
                "SHOW_EARNINGS": MasterMan.SHOW_EARNINGS,
                "SANL": MasterMan.SANL,
                'ANL': MasterMan.ANL
            }
        return options

    @classmethod
    def cache_or_create_options_view_redirect(MasterMan):
        options_view_redirect = cache.get("options_view_redirect")
        if not options_view_redirect:
            options_view_redirect = {
                MasterMan.PARAMETERS: "master-main",
                MasterMan.DATA: "master_data_main",
                MasterMan.SHOW_EARNINGS: "master_earnings",
                MasterMan.SANL: "master_sanl",
                MasterMan.ANL: '/anl/results'}
        return options_view_redirect



    @classmethod
    def translate_navlinknames_mmparameters(MasterMan, request_post):
        options = MasterMan.cache_or_create_options()
        # print(f"options:{options}")
        if request_post in options:
            return options[request_post]


    @classmethod
    def get_screen_view_value(MasterMan, master_man_view):
        options_view_redirect = MasterMan.cache_or_create_options_view_redirect()
        if master_man_view in options_view_redirect:
            return_redirect = options_view_redirect[master_man_view]
            log.info(f"redirect now to {return_redirect}")
            return return_redirect


    # @classmethod
    # def get_screen_view_value(MasterMan,masterman_view):
    #     # master_man = MasterMan.cache_or_create_mm()
    #     options_view_redirect = MasterMan.cache_or_create_options_view_redirect()
    #     print(f"options_view_redirect:{options_view_redirect}")
    #     if masterman_view in options_view_redirect:
    #         return_redirect = options_view_redirect[masterman_view]
    #         log.info(f"redirect now to {return_redirect}")
    #         return return_redirect



def myround(x, base=20.):
    return base * round(float(x) / base)


class Experiment(BaseMethods, models.Model):
    id = models.UUIDField(primary_key=True,null=False, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=125, default="auction, forward, Bessembinder and Lemmon (2002)")


class BasePlayer_stats(BaseMethods, models.Model):
    """ Player_stats give the basic attributes of a player for each round
    """
    id = models.BigAutoField(primary_key=True, null=False)
    profit = models.FloatField(default=0)
    class Meta:
        abstract = True

    # ToDo: repetitious! How to make this DRY???
    def save_and_cache(self):
        self.save()
        self.cache_me()
        return

    def __str__(self):  # For Python 2, use __str__ on Python 3
       return "{}".format(self.id)


# dAuction app classes
class BaseTreatment(BaseMethods, models.Model):
    RANDOM =1
    STRONGEST_TOGETHER =2

    GROUP_ARRANGEMENT_CHOICES = (
        (RANDOM, 'RANDOM'),
        (STRONGEST_TOGETHER, 'STRONGEST_TOGETHER'),
        )

    experiment = models.ForeignKey(Experiment, default=1,on_delete=models.CASCADE)
    au = models.BigIntegerField(default=0, null=True) # treatment should be child of auction... ToBe implemented as FK after experiments
    educational = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    groups_assignment_alternate = models.BooleanField(default=True)
    total_groups = models.PositiveSmallIntegerField(default=1)
    total_periods = models.PositiveSmallIntegerField(default=10)
    showupfee_fixed = models.PositiveSmallIntegerField(default=50)
    start_capital_in_CZK = models.PositiveSmallIntegerField(default=300)
    group_arrangements = models.PositiveSmallIntegerField(choices=GROUP_ARRANGEMENT_CHOICES, default=RANDOM)
    pay_one_random_period = models.BooleanField(default=True)
    allow_automatic_login = models.BooleanField(default=True)
    promised_avg_earnings = models.PositiveSmallIntegerField(default=350, null=True)

    class Meta:
        abstract = True

    # ToDo: repetitious! How to make this DRY???
    def save_and_cache(self):
        self.save()
        self.cache_me()
        return

    @classmethod
    def treatments_delete(cls, auction_list, treatment_list):
        for auction in auction_list:
            auction.delete()
        for treatment in treatment_list:
            treatment.delete()
        log.info("{} treatment delete".format("!" * 10))
        BaseMasterMan.invalidate_caches()


    # def treatments_delete(self):
    #     # for auction in auction_list:
    #     #     auction.delete()
    #     # for treatment in treatment_list:
    #     #     treatment.delete()
    #     treatment = self.treatment
    #     self.delete()
    #     treatment.delete()
    #     log.info("{} treatment delete".format("!" * 10))
    #     BaseMasterMan.invalidate_caches()


    def __str__(self):
          # return "Auction {0} created on {1}".format(self.id, self.created)
          return "{0}".format(self.id)


class BaseAuction(models.Model,BaseMethods):
    PARAMETERS = 1
    AUCTION = 2
    DATA = 3

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    make_instruction_pdf = models.BooleanField(default=False)
    player_stats_created = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    show_ids = models.BooleanField(default=False)
    players_all_logged = models.BooleanField(default=True)
    instructions_finished = models.BooleanField(default=False)
    multiplier = models.FloatField(default=1)
    fixed_uplift = models.SmallIntegerField(default=0)
    pagerefresh_toggle = models.BooleanField(default=False)
    particular_info = models.TextField(default="", null=True,blank=True)
    is_part_experiment = models.BooleanField(default=True)

    class Meta:
        abstract = True

    # ToDo: repetitious! How to make this DRY???
    def save_and_cache(self):
        # log.info("self:{}".format(self))
        self.save()
        self.cache_me()
        # log.info("self:{}".format(self))
        return

    @classmethod
    def create(cls):
        from forward_and_spot.models import Treatment
        today = datetime.today()  # Get timezone naive now
        seconds = today.timestamp()
        dt = int((date(2017, 10, 1) - date(1970, 1, 1)).total_seconds())
        seconds = int((seconds - dt) / 10)
        auction = cls(pk=seconds, created=date.today(), treatment=None, auction_created=True)
        # random.seed(auction.id)
        Treatment.treatment_create(auction.id)
        treatment = Treatment.objects.filter(au=auction.id).order_by('idd').first()
        auction.treatment=treatment
        auction.save_and_cache()
        treatment.save_and_cache()
        log.info("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        log.info("new auction created with pk={}, random.seed set as well!".format(seconds))
        # print("new auction created with pk={}, random.seed set as well!".format(seconds))
        # do something with the book

        return auction

    def add_au_id_to_treatment(self):
        treatment = self.treatment
        treatment.au = self.id
        treatment.save()

    @transaction.atomic
    def db_save(self):
        filename = "auction_{}_ Data".format(self.id)
        filename_json = os.path.join('dbs_saved_json', "{}.json".format(filename))
        log.info("filename_json:{}".format(filename_json))
        self.add_au_id_to_treatment()

        with gzip.open('{}.gz'.format(filename_json), 'wt') as f:
            call_command('dumpdata', stdout=f, exclude=['contenttypes', 'auth'])

    def db_reset(self):
        # first reset db - clears and cleans all!
        log.info("db_reset2!!!")
        os.environ['DJANGO_COLORS'] = 'nocolor'
        commands = StringIO()
        cursor = connection.cursor()
        for app in apps.get_app_configs():
            label = app.label
            call_command('sqlsequencereset', label, stdout=commands)
            # log.info("label:{}".format(label))
        cursor.execute(commands.getvalue())

        # reset db start value at self.id * M
        seq_list = ["distribution_distribution_id_seq",

                    "forward_and_spot_group_id_seq",
                    "forward_and_spot_offer_id_seq",
                    "forward_and_spot_penalty_id_seq",
                    "forward_and_spot_period_id_seq",
                    "forward_and_spot_phase_id_seq",
                    "forward_and_spot_player_id_seq",
                    "forward_and_spot_player_stats_id_seq",
                    "forward_and_spot_voucher_id_seq",
                    "forward_and_spot_voucherre_id_seq",

                    "testing_player_questions_id_seq",
                    "testing_player_question_options_id_seq",
                    "testing_question_id_seq",
                    "testing_option_mc_id_seq",
                    ]
        for seq in seq_list:
            cursor.execute('ALTER SEQUENCE "{}" RESTART WITH {}'.format(seq, (1000000 * self.id) +1))
        log.info("end of db_reset")
        return

    def __str__(self):
          return f"{self.id}"


class BaseTimer(BaseMethods, models.Model):
    running = models.BooleanField(default=True)
    end_time = models.PositiveIntegerField(default=0)
    seconds_left = models.IntegerField(default=0)
    class Meta:
        abstract = True

    def save_and_cache(self):
        self.save()
        self.cache_me()
        return

    def timer_set(self, time_length=None, short_time_length=None):
        time_time = time.time()
        if time_length:
            self.end_time = int(time_time + time_length)
            self.seconds_left = time_length
            log.info("seconds_left:{}".format(self.seconds_left))
        else:
            pass
            # time_length = self.seconds_left
        if short_time_length:
            cycles = round((self.end_time - time_time) / short_time_length)
            self.short_end_time = self.end_time - (cycles - 1) * short_time_length
            self.short_seconds_left = self.short_end_time - time_time
            self.short_running = self.running
        else:
            self.short_running = False
            self.short_seconds_left = 999
        # log.info(self.short_end_time ,)
        self.save_and_cache()
        return self

    def timer_cut(self):
        self.end_time = 0
        self.seconds_left = -10
        self.save_and_cache()
        return self

    def __str__(self):
        return "Timer {0}".format(self.id)


class PlayerType:
    PRODUCER = 1
    RETAILER = 2

    CHOICES = (
        (PRODUCER, 'producer'),
        (RETAILER, 'retailer'),
    )


class BaseGroup(BaseMethods, models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    idd=models.PositiveSmallIntegerField(default=1)
    class Meta:
        abstract = True

    # ToDo: repetitious! How to make this DRY???
    def save_and_cache(self):
        self.save()

        self.cache_me()
        # BaseMasterMan.cache_me(name, self)
        return

    def __str__(self):
      return "{}".format(self.idd)


class BasePeriod(BaseMethods, models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    id = models.BigAutoField(primary_key=True, null=False)
    idd = models.PositiveSmallIntegerField(default= 0, db_index=True)
    finished = models.BooleanField(default=False)

    class Meta:
        abstract = True

    # ToDo: repetitious! How to make this DRY???
    def save_and_cache(self):
        self.save()
        self.cache_me()
        return

    def __str__(self):
      return "{}".format(self.idd)


####################################################################################
# F&S app classes
####################################################################################
def random_int():
    return random.randint(1, 9999)


class BasePlayer(BaseMethods, models.Model):
    """ A player is one of the subjects. (S)he is a member of a group and has an id in the group.
    """
    WAIT = 1
    WORKING = 2
    FINISHED = 3
    VIEW_STATES = \
        (
            (WAIT, 'WAIT'),
            (WORKING, 'WORK'),
            (FINISHED, 'FIN'),
        )

    NOTNEEDREFRESHING=0
    NEEDREFRESHING = 1
    VIEW_PAGEREF = \
        (
            (NOTNEEDREFRESHING, 'NEED REFRESHING'),
            (NOTNEEDREFRESHING, 'OK'),
        )

    id = models.BigAutoField(primary_key=True, null=False)


    state = models.PositiveSmallIntegerField(choices=VIEW_STATES, default=WAIT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='player', on_delete=models.CASCADE,null=True, default=None)
    period=models.PositiveSmallIntegerField(default=1)
    page_need_refreshing = models.BooleanField(default=False)
    page= models.SmallIntegerField(default=1)
    last_refresh_date = models.DateTimeField(default =date(2002, 12, 4))
    last_alive=models.SmallIntegerField(default=99)
    payout_ECU = models.IntegerField(default=0)
    payout_CZK = models.IntegerField(default=0)
    cumulative_earnings = models.FloatField(default=0)
    # the money that a player has
    earnings_CZK =models.IntegerField(default=0)
    earnings_CZK_corrected = models.IntegerField(default=0)
    # Questionnaire elements
    first_name = models.CharField(max_length=224, default="")  # two roles: PRoducer and REtailer
    last_name = models.CharField(max_length=224, default="")  # two roles: PRoducer and REtailer
    id_or_birth_number = models.CharField(max_length=60, default="")
    male = models.BooleanField(default=True)
    age = models.PositiveSmallIntegerField(default=0)
    done_before= models.BooleanField(default=False)
    difficult_rating = models.PositiveSmallIntegerField(default=0)
    interesting_rating = models.PositiveSmallIntegerField(default=0)
    income_monthly_CZK = models.PositiveIntegerField(default=0)
    comments = models.TextField(default="")
    do_better_what = models.TextField(default="")
    payout_CZK_corr = models.PositiveSmallIntegerField(default=0)
    #
    # class Meta:

    class Meta:
        ordering = ['pk']
        abstract = True

    # ToDo: repetitious! How to make this DRY???
    def save_and_cache(self):
        self.save()

        self.cache_me()
        # BaseMasterMan.cache_me(name, self)
        return

    @classmethod
    def init_for_present_app(cls, auction, page, state,draw_id=None):
        if draw_id:
            cls.objects.filter(auction=auction, user__isnull=False).update(page=page, state=state, app=auction.app, draw_id=draw_id)
        else:
            cls.objects.filter(auction=auction, user__isnull=False).update(page=page, state=state, app=auction.app)

    def get_payout_CZK_corr(self):
        from forward_and_spot.models import Player
        if self.selected:
            if self.role==Player.PR:
                return 10 * int(math.ceil(((self.payout_CZK + self.auction.fixed_uplift + self.auction.fixed_uplift_PR) * self.auction.multiplier * self.auction.multiplier_PR)/10))
            else:
                return 10 * int(math.ceil(((
                   self.payout_CZK + self.auction.fixed_uplift + self.auction.fixed_uplift_RE) * self.auction.multiplier * self.auction.multiplier_RE)/10))
        else:
            return self.payout_CZK

    def get_group_cache(self):
        pass


    def __str__(self):
      return "{}".format(self.id)

    def get_pay_period(self, last_round_idd,pay_qs_period):
        log.info("old round for pay_period: {}".format(self.pay_period))
        # log.info("inside:pay_qs_period:{}".format(pay_qs_period))
        # print("old round for pay_period: {}".format(self.pay_period))
        if last_round_idd==1:
            r=[1,]
            log.info("r=[1,]:{}".format(r))
            # print("r=[1,]:{}".format(r))
        else:
            log.info("self.pay_qs_period:{}".format(self.pay_qs_period))
            # print("self.pay_qs_period:{}".format(self.pay_qs_period))
            # print("last_round_idd:{}".format(last_round_idd))
            r = [i for i in range(1, last_round_idd+1) if i != pay_qs_period]
            log.info("r:{}".format(r))
        log.info("new round for pay_period: {}".format(r))
        # print("new round for pay_period: {}".format(r))
        return random.choice(r)