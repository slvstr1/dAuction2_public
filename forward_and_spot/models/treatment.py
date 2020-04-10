import logging, os, uuid
from django.db import models
# from dAuction2.models import Experiment
from django.core.cache import cache
from dAuction2.models import  BaseTreatment

from master.models import MasterMan
log = logging.getLogger(__name__)


class Treatment(BaseTreatment):
    UNIFORM=0
    NORMAL=1
    DISTRIBUTION_CHOICES = (
        (UNIFORM, 'uniform'),
        (NORMAL, 'normal'),
    )
    idd = models.IntegerField(default=1)
    id = models.UUIDField(primary_key=True,null=False,default=uuid.uuid4)
    PR_per_group = models.PositiveSmallIntegerField(default=4)
    RE_per_group = models.PositiveSmallIntegerField(default=4)
    require_units_demanded_on_PR =  models.BooleanField(default=True)
    convexity_parameter = models.IntegerField(default=4)
    a = models.FloatField(default=0.017777777777)
    F = models.FloatField(default=0)
    distribution_used = models.PositiveSmallIntegerField(choices=DISTRIBUTION_CHOICES, default=UNIFORM)
    mu = models.FloatField(default=60)
    sigma = models.FloatField(default=20)
    uniform_min = models.PositiveSmallIntegerField(default=20)
    uniform_max = models.PositiveSmallIntegerField(default=100)
    retail_price = models.PositiveSmallIntegerField(default=197)
    demand_avg_theory = models.FloatField(default=60)
    demand_sd_theory = models.FloatField(default=23.38)
    price_avg_theory = models.FloatField(default=87)
    price_sd_theory = models.FloatField(default=-1)

    # organizational - core
    register_cancelled = models.BooleanField(default=True)
    time_for_forward_1 = models.PositiveSmallIntegerField(default=None, null=True)
    time_for_forward_2 = models.PositiveSmallIntegerField(default=None, null=True)  # conditional (on a deal)
    time_conditional = models.PositiveSmallIntegerField(
        default=20)  # length of period in conditional state (same for all stages and states
    time_for_forward_waiting = models.PositiveSmallIntegerField(default=30)
    time_for_spot_1 = models.PositiveSmallIntegerField(default=None, null=True)  # initial
    time_for_spot_2 = models.PositiveSmallIntegerField(default=None, null=True)  # conditional (on a deal)
    time_for_spot_3 = models.PositiveSmallIntegerField(default=None, null=True)  # penalty phase
    time_for_spot_waiting = models.PositiveSmallIntegerField(default=None, null=True)
    time_for_question_page = models.PositiveSmallIntegerField(default=25)

    time_refresh_check = models.PositiveSmallIntegerField(default=8000)
    # time_refresh_data = models.PositiveSmallIntegerField(default=1500)
    time_for_testing = models.PositiveSmallIntegerField(default=900)  # initial
    time_for_instructions = models.PositiveSmallIntegerField(default=600)
    time_for_distribution = models.PositiveSmallIntegerField(default=180)
    time_for_succession = models.PositiveSmallIntegerField(default=2)  # initial
    error_max = models.PositiveSmallIntegerField(default=16)

    ECU_per_CZK_PR = models.FloatField(default=.5)
    ECU_per_CZK_RE = models.FloatField(default=2)
    showupfee_desel = models.PositiveSmallIntegerField(default=200)
    showupfee_desel_error_max = models.PositiveSmallIntegerField(default=50)
    qp_accuracy_fee= models.PositiveSmallIntegerField(default=100)
    max_vouchers = models.PositiveSmallIntegerField(default=35)
    d_draws_needed = models.PositiveSmallIntegerField(default=400)
    short_maximum = models.PositiveSmallIntegerField(default=15)
    # voucher_number = models.PositiveSmallIntegerField(default=35)
    penalty_perunit = models.PositiveSmallIntegerField(default=10)
    qp_every = models.PositiveSmallIntegerField(default=3)
    # organizational - test and etc
    test_players = models.BooleanField(default=False)
    test_script = models.BooleanField(default=False)
    allow_multiple_offers = models.BooleanField(default=False)
    test_mode = models.BooleanField(default=False)
    only_spot = models.BooleanField(default=False)
    shedding = models.PositiveSmallIntegerField(default=8)

    def set_test_script(self):
        self.test_script = not self.test_script
        self.save_and_cache()
        master_man = MasterMan.cache_or_create_mm()
        master_man.no_test = False
        master_man.save_and_cache()
        self.save_and_cache()

    def set_test_players(self):
        self.test_players = not self.test_players
        self.save_and_cache()
        master_man = MasterMan.cache_or_create_mm()
        master_man.no_test = False
        master_man.save_and_cache()
        self.save_and_cache()

    def test_mode_toggle(self):
        self.test_mode = not self.test_mode
        self.save_and_cache()
        master_man = MasterMan.cache_or_create_mm()
        master_man.no_test = False
        master_man.save_and_cache()
        self.save_and_cache()

    def  allow_multiple_offers_toggle(self):
        self.allow_multiple_offers = not self.allow_multiple_offers
        self.save_and_cache()
        master_man = MasterMan.cache_or_create_mm()
        master_man.no_test = False
        master_man.save_and_cache()
        self.save_and_cache()


    def toggle_eductional(treatment ):
        MasterMan.cache_it("page_list", None)
        treatment.educational = not treatment.educational
        treatment.save_and_cache()
        master_man = MasterMan.cache_or_create_mm()
        master_man.no_test = False
        master_man.save_and_cache()


    def automatic_login_toggle(treatment):
        # from .models import Player
        treatment.allow_automatic_login = not treatment.allow_automatic_login
        treatment.save_and_cache()
        MasterMan.refresh_all_connected()
        # Player.refresh_all_players()

    def pay_one_random_period_toggle(treatment):
        treatment.pay_one_random_period = not treatment.pay_one_random_period
        treatment.save_and_cache()
        master_man = MasterMan.cache_or_create_mm()
        master_man.no_test = False
        master_man.save_and_cache()

    def only_spot_toggle(treatment):
        # treatment = Treatment.cache_get()
        MasterMan.cache_it("page_list", None)
        treatment.only_spot = not treatment.only_spot
        treatment.save_and_cache()
        master_man = MasterMan.cache_or_create_mm()
        master_man.no_test = False
        master_man.save_and_cache()



    @property
    def get_average_uniform(self):
        return (self.uniform_min + self.uniform_max) / 2

    @property
    def get_length_uniform(self):
        return (self.uniform_max - self.uniform_min)

    @property
    def get_total_players(self):
        return self.PR_per_group + self.RE_per_group

    @property
    def total_PR(self):
        return self.PR_per_group * self.total_groups

    @property
    def total_RE(self):
        return self.RE_per_group * self.total_groups

    @property
    def get_players_per_group(self):
        return (self.PR_per_group + self.RE_per_group)

    @property
    def hardcoded_pics(self):
        src_file02b = "/staticfiles/images/instructions_fig_02b_{}_{}_{}.png".format(self.distribution_used,self.uniform_min,self.uniform_max)
        src_file18 = "/staticfiles/images/instructions_fig_18_{}_{}_{}.png".format(self.distribution_used,self.uniform_min,self.uniform_max)
        src_file19 = "/staticfiles/images/instructions_fig_19_{}_{}_{}.png".format(self.distribution_used,self.uniform_min,self.uniform_max)
        # log.info("src_file02b:{}".format(src_file02b))

        src_file02b_exists = os.path.isfile(src_file02b[1:])
        src_file18_exists = os.path.isfile(src_file18[1:])
        src_file19_exists = os.path.isfile(src_file19[1:])
        # log.info("src_file02b_exists:{}, name:{}".format(src_file02b_exists, src_file02b))
        # log.info("src_file18_exists:{}, name:{}".format(src_file18_exists, src_file18))
        # log.info("src_file19_exists:{}, name:{}".format(src_file19_exists, src_file19))

        src_file_exists = src_file02b_exists and src_file18_exists and src_file19_exists
        a= [src_file02b, src_file18, src_file19]
        return src_file_exists, a

    @classmethod
    def cache_or_create_treatment(cls,auction=None):
        # print("cache_or_create_treatment2")
        # experiment= cache.get('experiment')
        from forward_and_spot.models import Auction

        treatment = cls.cache_get()
        if not treatment:
            if cls.objects.exists():
                if not auction:
                    auction = Auction.cache_get()
                if not auction:
                    auction = Auction.objects.filter(active=True).last()
                    cache.set('auction', auction)
                if auction:
                    try:
                        print("try to get treatment")
                        treatment = cls.objects.get(active=True, au=auction.id)
                    except cls.DoesNotExist:
                        log.error("ERROR: treatment does not exist!")
                        try:
                            treatment = auction.treatment
                        except cls.DoesNotExist:
                            treatment = cls.objects.all().order_by('id').first()
                            treatment.active = True

                    except cls.MultipleObjectsReturned:
                        log.error("ERROR: too many active treatments!")
                        cls.objects.update(active=False)
                        treatment = cls.objects.all().order_by('id').first()
                        treatment.active = True
                else:
                    treatment = cls.objects.all().last()
                    treatment.active = True

            else:
                treatment = cls.treatment_create()
            treatment.save_and_cache()
            # BaseMasterMan.cache_me("treatment", treatment)
            log.info("treatment cached and saved!!!:{}".format(treatment))
        return treatment


    # def cache_or_create_treatment(cls,auction=None):
    #     # print("cache_or_create_treatment2")
    #     # experiment= cache.get('experiment')
    #     from forward_and_spot.models import Auction
    #
    #     treatment = cls.cache_get()
    #     if not treatment:
    #         if cls.objects.exists():
    #             if auction:
    #                 try:
    #                     treatment = cls.objects.get(active=True, au=auction.id)
    #                 except cls.DoesNotExist:
    #                     log.error("ERROR: treatment does not exist!")
    #                     # auction = Auction.cache_get()
    #                     if auction:
    #                         treatment = auction.treatment
    #                     else:
    #                         auction = Auction.cache_get()
    #                         if auction:
    #                             auction = Auction.objects.filter(active=True).last()
    #                             if auction:
    #                                 treatment = auction.treatment
    #                                 cache.set('auction', auction)
    #                             else:
    #                                 treatment = cls.objects.all().last()
    #                                 treatment.active = True
    #                     treatment.active = True
    #                 except cls.MultipleObjectsReturned:
    #                     log.error("ERROR: too many active treatments!")
    #                     cls.objects.update(active=False)
    #                     treatment = cls.objects.all().order_by('id').last()
    #                     treatment.active = True
    #             else:
    #                 treatment = cls.objects.all().last()
    #                 treatment.active = True
    #         else:
    #             # treatment = treatment_create()
    #             treatment = cls.treatment_create()
    #             # treatment.active = True
    #         treatment.save_and_cache()
    #
    #         # BaseMasterMan.cache_me("treatment", treatment)
    #         log.info("treatment cached and saved!!!:{}".format(treatment))
    #     return treatment

    @classmethod
    def treatment_create(cls,auctionid=0):
        def same_assign(tr):
            log.info("treatment_create2")
            tr.groups_assignment_alternate = True
            tr.time_for_succession = 2
            # tr.au = auctionid
            tr.time_for_instructions = 10 * 60
            tr.time_for_distribution = 3 * 60
            tr.time_for_forward_1 = 45  # initial
            tr.time_for_forward_2 = 3 * 60  # conditional (on a deal)
            tr.time_conditional = 30  # length of period in conditional state (same for all stages and states
            tr.time_for_testing = 16 * 60
            tr.time_for_forward_waiting = 20
            tr.time_for_spot_1 = 45  # initial
            tr.time_for_spot_2 = 3 * 60  # conditional (on a deal)
            tr.time_for_spot_3 = 2 * 60  # penalty phase
            tr.time_for_spot_waiting = 45
            tr.time_for_question_page = 60
            tr.time_refresh_check = 2000
            tr.total_periods = 10
            tr.error_max = 16
            tr.test_players = False
            tr.test_script = False
            # tr.make_instruction_pdf = False
            tr.allow_multiple_offers = False
            tr.test_mode = False
            tr.group_arrangements = Treatment.RANDOM
            tr.only_spot = False
            tr.allow_automatic_login = True
            tr.showupfee_desel = 200
            tr.showupfee_desel_error_max = 50
            tr.max_vouchers = 35
            tr.d_draws_needed = 400
            tr.short_maximum = 15
            tr.penalty_perunit = 10
            tr.shedding = 8
            tr.groups_assignment_alternate = True
            tr.qp_every = 2
            tr.promised_avg_earnings = 700
            # print("tr.promised_avg_earnings:{}".format(tr.promised_avg_earnings ))
            tr.pay_one_random_period = True
            tr.active=False

        log.info("create treatment !!!!!!")
        from dAuction2.models import Experiment
        experiment = Experiment.cache_get()
        if not experiment:
            experiment = Experiment.objects.all().last() # Todo: think about this - this is messy Need more clarity about how to choose an experiment object (especiall wehnt there will be more experiments :)
            if not experiment:
                experiment = Experiment.objects.get_or_create()[0]


        tr =cls.objects.get_or_create(idd=1,experiment=experiment,au=auctionid)[0]
        same_assign(tr)
        tr.active = True
        tr.start_capital_in_CZK = 300
        tr.total_groups = 2
        tr.shedding = 8
        # tr.myseed = 1 # unused
        tr.PR_per_group = 4
        tr.RE_per_group = 4
        tr.convexity_parameter =4
        tr.a = 0.017777777777
        tr.F = 0
        tr.mu = 60
        tr.sigma = 0.01
        tr.uniform_min = 20
        tr.uniform_max = 100
        tr.retail_price = 139
        tr.demand_avg_theory = 60
        tr.demand_sd_theory = 23.09
        tr.price_avg_theory = 87
        tr.price_sd_theory = 79
        tr.ECU_per_CZK_PR = 1.5
        tr.ECU_per_CZK_RE = 4.5
        tr.distribution_used=Treatment.UNIFORM
        tr.save()

        del tr
        tr =cls.objects.get_or_create(idd=2,experiment=experiment,au=auctionid)[0]
        same_assign(tr)
        tr.start_capital_in_CZK = 0
        tr.total_groups = 2
        # tr.myseed = 1 # unused
        tr.PR_per_group = 4
        tr.RE_per_group = 4
        tr.convexity_parameter =4
        tr.a = 0.017777777777
        tr.F = 0
        tr.mu = 60
        tr.sigma =0.02
        tr.uniform_min = 55
        tr.uniform_max = 65
        tr.retail_price = 73
        tr.demand_avg_theory = 60
        tr.demand_sd_theory = 2.9
        tr.price_avg_theory = 60.4
        tr.price_sd_theory = 8.7
        tr.ECU_per_CZK_PR = 1.2
        tr.ECU_per_CZK_RE = .3

        tr.distribution_used=Treatment.UNIFORM
        tr.save()

        del tr
        tr = cls.objects.get_or_create(idd=3, experiment=experiment,au=auctionid)[0]
        same_assign(tr)
        tr.start_capital_in_CZK = 100
        tr.total_groups = 2
        # tr.myseed = 1 # unused
        tr.PR_per_group = 4
        tr.RE_per_group = 4
        tr.convexity_parameter = 4
        tr.a = 0.017777777777
        tr.F = 0
        tr.mu = 60
        tr.sigma = 0.03
        tr.uniform_min = 40
        tr.uniform_max = 80
        tr.retail_price = 88
        tr.demand_avg_theory = 60
        tr.demand_sd_theory = 11.6
        tr.price_avg_theory = 67
        tr.price_sd_theory = 36
        tr.ECU_per_CZK_PR = 1.4
        tr.ECU_per_CZK_RE = .4
        tr.distribution_used = Treatment.UNIFORM
        tr.save()

        del tr
        # VSE, Ocean University 2018.02.02
        tr = cls.objects.get_or_create(idd=11, experiment=experiment,au=auctionid)[0]
        same_assign(tr)
        tr.active = False
        tr.start_capital_in_CZK = 300
        tr.total_groups = 2
        tr.shedding = 8
        tr.PR_per_group = 4
        tr.RE_per_group = 4
        tr.convexity_parameter = 4
        tr.a = 0.017777777777
        tr.F = 0
        tr.mu = 60
        tr.sigma = 0.01
        tr.uniform_min = 20
        tr.uniform_max = 100
        tr.retail_price = 139
        tr.demand_avg_theory = 60
        tr.demand_sd_theory = 23.09
        tr.price_avg_theory = 87
        tr.price_sd_theory = 79
        tr.ECU_per_CZK_PR = 1
        tr.ECU_per_CZK_RE = 1
        tr.distribution_used=Treatment.UNIFORM
        tr.educational = True
        tr.save()


        del tr
        # cerge exhib 2018.03.13
        tr = cls.objects.get_or_create(idd=12, experiment=experiment,au=auctionid)[0]
        same_assign(tr)
        tr.active = False
        tr.start_capital_in_CZK = 300
        tr.total_groups = 1
        tr.shedding = 4
        tr.PR_per_group = 2
        tr.RE_per_group = 2
        tr.convexity_parameter = 4
        tr.a = 0.017777777777
        tr.F = 0
        tr.mu = 0
        tr.sigma = 0
        tr.uniform_min = 10
        tr.uniform_max = 50
        tr.retail_price = 139
        tr.demand_avg_theory = 30
        tr.demand_sd_theory = 11.5
        tr.price_avg_theory = 87
        tr.price_sd_theory = 79
        tr.ECU_per_CZK_PR = 1.5
        tr.ECU_per_CZK_RE = 4.5
        tr.distribution_used=Treatment.UNIFORM
        tr.educational = True
        tr.save()


        del tr
        tr = cls.objects.get_or_create(idd=21, experiment=experiment, au=auctionid)[0]
        same_assign(tr)
        # tr.active = True
        tr.require_units_demanded_on_PR = False
        tr.start_capital_in_CZK = 300
        tr.total_groups = 2
        tr.shedding = 8
        # tr.myseed = 1 # unused
        tr.PR_per_group = 4
        tr.RE_per_group = 4
        tr.convexity_parameter = 4
        tr.a = 0.017777777777
        tr.F = 0
        tr.mu = 60
        tr.sigma = 0.01
        tr.uniform_min = 20
        tr.uniform_max = 100
        tr.retail_price = 139
        tr.demand_avg_theory = 60
        tr.demand_sd_theory = 23.09
        tr.price_avg_theory = 87
        tr.price_sd_theory = 79
        tr.ECU_per_CZK_PR = 1.5
        tr.ECU_per_CZK_RE = 4.5
        tr.distribution_used = Treatment.UNIFORM
        tr.save()

        del tr
        tr = cls.objects.get_or_create(idd=22, experiment=experiment, au=auctionid)[0]
        same_assign(tr)
        tr.require_units_demanded_on_PR = False
        tr.start_capital_in_CZK = 0
        tr.total_groups = 2
        # tr.myseed = 1 # unused
        tr.PR_per_group = 4
        tr.RE_per_group = 4
        tr.convexity_parameter = 4
        tr.a = 0.017777777777
        tr.F = 0
        tr.mu = 60
        tr.sigma = 0.02
        tr.uniform_min = 55
        tr.uniform_max = 65
        tr.retail_price = 73
        tr.demand_avg_theory = 60
        tr.demand_sd_theory = 2.9
        tr.price_avg_theory = 60.4
        tr.price_sd_theory = 8.7
        tr.ECU_per_CZK_PR = 1.2
        tr.ECU_per_CZK_RE = .3

        tr.distribution_used = Treatment.UNIFORM
        tr.save()

        del tr
        tr = cls.objects.get_or_create(idd=23, experiment=experiment, au=auctionid)[0]
        same_assign(tr)
        tr.require_units_demanded_on_PR = False
        tr.start_capital_in_CZK = 100
        tr.total_groups = 2
        # tr.myseed = 1 # unused
        tr.PR_per_group = 4
        tr.RE_per_group = 4
        tr.convexity_parameter = 4
        tr.a = 0.017777777777
        tr.F = 0
        tr.mu = 60
        tr.sigma = 0.03
        tr.uniform_min = 40
        tr.uniform_max = 80
        tr.retail_price = 88
        tr.demand_avg_theory = 60
        tr.demand_sd_theory = 11.6
        tr.price_avg_theory = 67
        tr.price_sd_theory = 36
        tr.ECU_per_CZK_PR = 1.4
        tr.ECU_per_CZK_RE = .4
        tr.distribution_used = Treatment.UNIFORM
        tr.save()


        active_treatment_list = Treatment.objects.filter(active=True,au=auctionid)
        log.info("active_treatment_list:{}".format(active_treatment_list ))
        if active_treatment_list.count()==1:
            log.info("only one active treatment:{}".format(active_treatment_list.count()))
        else:
            raise Exception("incorrect no of active treatments:{}".format(active_treatment_list.count()))
        return active_treatment_list.last()