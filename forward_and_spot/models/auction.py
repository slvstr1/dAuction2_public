import logging, os
from django.db.models import StdDev
from django.db import models
from django.db.models import Avg, Max, Min
from django.core.cache import cache
from django.apps import apps
from django_bulk_update.helper import bulk_update
from dAuction2.models import BaseAuction
from master.models import MasterMan
from .treatment import Treatment
log = logging.getLogger(__name__)


class Auction(BaseAuction):
    RANDOM =1
    STRONGEST_TOGETHER =2
    NORMAL=0
    UNIFORM=1
    PARAMETERS = 1
    DATA = 3
    SHOW_EARNINGS = 5
    ANL = 4
    SANL = 6

    GROUP_ARRANGEMENT_CHOICES = (
        (RANDOM, 'RANDOM'),
        (STRONGEST_TOGETHER, 'STRONGEST_TOGETHER'),
        )

    SUMMARY_INSTR = 0
    FULL_INSTR = 1

    ITYPES = (
        (SUMMARY_INSTR,'SUMMARY INSTRUCTIONS'),
        (FULL_INSTR,'FULL INSTRUCTIONS' ),
    )
    WAIT=0
    INSTR = 1
    DISTR = 2
    TESTING = 3
    FS = 4
    QUEST = 5
    PAYOUT = 6
    APPTYPES = (
        (WAIT, 'WAITING'),
        (INSTR, 'INSTRUCTIONS'),
        (DISTR, 'DISTRIBUTION'),
        (TESTING, 'TESTING'),
        (FS, 'FORWARDANDSPOT'),
        (QUEST, 'QUESTIONNAIRE'),
        (PAYOUT, 'PAYOUT'),
    )

    MASTER_SCREEN_TYPES = (
        (PARAMETERS , 'PARAMETERS '),
        (DATA, 'DATA'),
        (SHOW_EARNINGS, 'SHOW_EARNINGS'),
        (ANL, 'ANL'),
        (SANL, 'SANL'),
    )

    # core
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    time_refresh_data = models.PositiveSmallIntegerField(default=1500)
    encountered_issues = models.TextField(default="",null=True)
##########################################################33333
    # non-treatment vars
    removing = models.BooleanField(default=False)
    kill_removed = models.BooleanField(default=False)
    instructions_created = models.BooleanField(default=False)

    ECU_per_CZK_PR = models.FloatField(default=.5)
    ECU_per_CZK_RE = models.FloatField(default=2)
    users_created = models.BooleanField(default=False)
    auction_created = models.BooleanField(default=False)

    app = models.PositiveSmallIntegerField(choices=APPTYPES, default=0)
    app_testing_started = models.BooleanField(default=False)
    app_testing_ended = models.BooleanField(default=False)

    allow_late_entry = models.BooleanField(default=True)
    testing_totalquestions = models.PositiveSmallIntegerField(default=0)  # can I lower the use of this one? delegate to Question?
    testing_questions_defined= models.BooleanField(default=False) # can I lower the use of this one? delegate to Question?
    testing_player_questions_defined= models.BooleanField(default=False) # can I lower the use of this one? delegate to Question?

    demand_avg = models.FloatField(default=-1)
    demand_sd = models.FloatField(default=-1)
    price_avg = models.FloatField(default=-1)
    price_sd = models.FloatField(default=-1)
    cov_DP = models.FloatField(default=-1)

    demand_curtailment_warning = models.BooleanField(default=False)
    players_endowed = models.BooleanField(default=False)


    # summ_instruction_totalPages = models.PositiveSmallIntegerField(default=0)
    itype=models.PositiveSmallIntegerField(choices=ITYPES,default=SUMMARY_INSTR)

    all_ready = models.BooleanField(default=False)
    players_one_logged = models.BooleanField(default=False)
    logging_requirement_overruled = models.BooleanField(default=True)
    auction_started= models.BooleanField(default=False)
    auction_finished= models.BooleanField(default=False)
    distribution_auction_created= models.BooleanField(default=False)
    end = models.BooleanField(default=False)
    av_paid_PR = models.IntegerField(default=-1)
    max_paid_PR= models.IntegerField(default=-1)
    min_paid_PR = models.IntegerField(default=-1)
    av_paid_PR_corr = models.IntegerField(default=-1)
    max_paid_PR_corr = models.IntegerField(default=-1)
    min_paid_PR_corr = models.IntegerField(default=-1)

    av_paid_RE = models.IntegerField(default=-1)
    max_paid_RE = models.IntegerField(default=-1)
    min_paid_RE= models.IntegerField(default=-1)
    av_paid_RE_corr = models.IntegerField(default=-1)
    max_paid_RE_corr = models.IntegerField(default=-1)
    min_paid_RE_corr = models.IntegerField(default=-1)

    multiplier_PR = models.FloatField(default=1)
    multiplier_RE = models.FloatField(default=1)
    fixed_uplift_PR = models.SmallIntegerField(default=0)
    fixed_uplift_RE = models.SmallIntegerField(default=0)
    missing_stages = models.PositiveSmallIntegerField(default=0)
    empty_fields_in_export=models.BooleanField(default=False)

    # display fields
    view = models.PositiveSmallIntegerField(choices=MASTER_SCREEN_TYPES, default=PARAMETERS) # ToDo: can go!
    show_table = models.BooleanField(default=True) # ToDo: can go!
    show_unselected = models.BooleanField(default=True) # ToDo: can go!
    show_payments = models.BooleanField(default=False) # ToDo: can go!


    def remove_all_objects_in_class(self,class_name_list):
        from django.apps import apps as django_apps
        log.info("remove_all_objects_in_class")
        if class_name_list:
            for class_name in class_name_list:
                # print("class_name:{}".format(class_name))
                cls2 = django_apps.get_model("{}".format(class_name))
                # print("cls2:{}".format(cls2))
                if hasattr(cls2, 'auction'):
                    # print("hasattr(cls2, 'auction'):{}".format(hasattr(cls2, 'auction')))
                    cls2.delete_all_objects(self)



    #sofar not used
    @classmethod
    def get_app_models_dict(cls):
        from dAuction2 import settings
        all_apps = cache.get("all_apps")
        if all_apps:
            app_models_dict = cache.get("app_models_dict")
            if app_models_dict:
                return all_apps, app_models_dict

        all_apps = list(settings.SESSION_STAGES_RELEVANT)
        app_models_dict = []
        for app in all_apps:
            if "contrib" in app:
                pass
                # print("contrib:{}".format(app))
            else:
                app_models = apps.all_models['{}'.format(app)]
                model_list = []
                for model in app_models:
                    model_list.append(model)
                # print("app:{}".format(app))
            app_models_dict.append({"{}".format(app): model_list})
        # print("app_models_pair:{}".format(app_models_dict))
        MasterMan.cache_it("all_apps", all_apps)
        MasterMan.cache_it("app_models_dict", app_models_dict)
        return all_apps, app_models_dict


    @classmethod
    def set_new_app_state(cls, auction):
        from forward_and_spot.models import Player
        draw_id = None
        if \
                auction.app == Auction.QUEST or \
                        auction.app == Auction.DISTR or \
                        auction.app == Auction.TESTING or \
                        auction.app == Auction.INSTR:
            page = 1
            state = 2
            # Player.objects.filter(auction=auction, user__isnull=False).update(page=1, state=2)
        elif \
                auction.app == Auction.PAYOUT:
            page = 0
            state = 0
            # Player.objects.filter(selected=True, auction=auction).update(app=Player.PAYOUT)
        elif \
                auction.app == Auction.FS:
            page = 0
            state = 2
            # Player.objects.filter(auction=self, user__isnull=False).update(page=0, state=2)

        elif \
                auction.app == Auction.WAIT:
            page = 1
            draw_id = 0
            state = 1
            # Player.objects.filter(auction=self, user__isnull=False).update(page=1, app=0)
        Player.init_for_present_app(auction, page, state, draw_id)


    @property
    def db_size(self):
        from .offer import Offer
        return Offer.objects.filter(auction=self).count()


    def new_player_stats(auction, treatment, randomarg):
        # import random
        from forward_and_spot.models import Player_stats, Group, Player

        needed_people_per_group = (treatment.PR_per_group + treatment.RE_per_group)
        # print("needed_people_per_group :{}".format(needed_people_per_group))
        needed_people = needed_people_per_group * treatment.total_groups
        Player_stats.delete_all_objects(auction)
        player_set = Player.fresh_players(auction, randomarg)

        player_set_selected = player_set[0:needed_people]
        # print("players_set_selected:{}".format(player_set_selected))
        from collections import deque
        player_set_selected_deq = deque(player_set_selected)
        groups = Group.get_groups(auction)
        # print("treatment.get_players_per_group:{}".format(treatment.get_players_per_group))
        # print("groups:{}".format(groups))
        for group in groups:
            for i in range(treatment.PR_per_group):
                # print("group:{}, role:{}".format(group, 0))
                try:
                    player = player_set_selected_deq.popleft()
                    player.page = 1
                    player.role = 0
                    player.group = group
                    player.selected = True
                    log.info("player:{}, selected:{}".format(player, player.selected))
                    player.save()
                    # print("player selected: {}".format(player))
                except IndexError:
                    pass
                    log.info("not enough players")
                    # print("not enough players")

            for i in range(treatment.RE_per_group):
                # print("group:{}, role:{}".format(group, 1))
                try:
                    player = player_set_selected_deq.popleft()
                    player.page = 1
                    player.role = 1
                    player.group = group
                    player.selected = True
                    log.info("player:{}, selected:{}".format(player, player.selected))
                    player.save()
                    # print("player selected: {}".format(player))
                except IndexError:
                    pass
                    log.info("not enough players")
                    # print("not enough players")
        auction.save_and_cache()
        treatment.save_and_cache()


    def strongest_together(auction, treatment):
        from .models import Player_stats, Player, Group
        log.info("strongest_together")
        MasterMan.invalidate_caches()
        auction.player_stats_created = False
        auction.save_and_cache()
        auction.new_player_stats(treatment,randomarg=False )
        # Note: False < True


    def questionnaire_start(auction):
        auction.app = Auction.QUEST
        Auction.set_new_app_state(auction)
        auction.save_and_cache()
        MasterMan.refresh_all_connected()
    #Player.refresh_all_players()


    def questionnaire_cancel(auction):
        auction.app = Auction.WAIT
        auction.save_and_cache()
        MasterMan.refresh_all_connected()


    @classmethod
    def session_new(cls,past_auction, treatment):
        from master.models import MasterMan
        mm =MasterMan.cache_or_create_mm()
        past_auction.active = False
        past_auction.save()
        log.info("call_invalidate_caches_outside")
        MasterMan.invalidate_caches()
        auction = Auction.create()


        auction.active=True
        mm.view = 3
        auction.file_name = "data_{}".format(auction.pk)
        log.info("new auction with pk-{}".format(auction.pk))
        mm.save_and_cache()
        auction.save_and_cache()
        return


    def distribution_start(auction, treatment):
        from forward_and_spot.models import Timer
        auction.app = Auction.DISTR
        auction.save_and_cache()
        Auction.set_new_app_state(auction)
        Timer.objects.all().delete()
        log.info("Timer.objects.exists():{}".format(Timer.objects.exists()))
        tt = Timer.objects.get_or_create(pk=1)[0]
        tt = tt.timer_set(time_length=treatment.time_for_distribution)
        tt.save_and_cache()
        MasterMan.refresh_all_connected()

    @staticmethod
    def make_sound(duration, freq):
        duration = duration  # seconds
        freq = freq  # Hz
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        return

    @classmethod
    def cache_or_create_auction(cls):

        auction = Auction.cache_get()
        if not auction:
            log.info("auction_not_exist_in_cache")
            if Auction.objects.exists():
                try:
                    auction = Auction.objects.get(active=True)
                except Auction.DoesNotExist:
                    # import os
                    auction = Auction.create()
                    log.info("auction.auction_created={}".format(auction.auction_created))
            else:
                auction = Auction.create()
                log.info("auction.auction_created={}".format(auction.auction_created))
            if auction:
                auction.save_and_cache()
                log.info("auction.save_and_cache()")
                log.info("auction:{}".format(auction))
        # else:
        #     # log.info("auction_from_cache")
        treatment = Treatment.cache_or_create_treatment(auction)

        if not auction.auction_created:
            from .models import Timer, Group
            log.info("not_auction.auction_created2")
            # print("not_auction.auction_created2")
            cache.set("player_list", None)
            log.info("auction:{}".format(auction))
            # log.info("MasterMan.invalidate_caches() in auction_create")
            auction.save_and_cache()
            log.info("call_invalidate_caches_outside")
            MasterMan.invalidate_caches()
            auction.save_and_cache()
            log.info("call_auction_init(treatment)")
            auction.auction_created = auction.auction_init(treatment)
            auction.save_and_cache()
            auction.instructions_created = auction.instructions_create()
            auction.save_and_cache()
            tt = Timer.objects.get_or_create(pk=1)[0]
            auction.save_and_cache()
            tt.cache_me()
            auction.save_and_cache()
            group_list = Group.get_groups(auction)
            MasterMan.cache_it("group_list", group_list)
            log.info("auction:{}".format(auction))
            auction.save_and_cache()
            MasterMan.refresh_all_connected()
            auction.save_and_cache()
            log.info("auction:{}".format(auction))
            log.info("auction newly saved!!!")
            tmpl = 'master-main'
        return auction, treatment


    def full_instructions_start_main(auction, treatment):
        from .models import Timer
        auction.instructions_start(treatment, Auction.FULL_INSTR)
        MasterMan.cache_it("page_list", None)
        tt = Timer.objects.get_or_create(pk=1)[0]
        tt = tt.timer_set(time_length=treatment.time_for_instructions)
        tt.cache_me()
        auction.save_and_cache()
        MasterMan.refresh_all_connected()


    # this belongs more with Distribution app!
    def demand_draws_delete(auction):
        log.info("call_invalidate_caches_outside")
        MasterMan.invalidate_caches()
        auction.remove_all_objects_in_class( [
            "distribution.Distribution",
            "forward_and_spot.Player_stats","forward_and_spot.Player","forward_and_spot.Voucher","forward_and_spot.VoucherRE","forward_and_spot.Penalty",
            "testing.Player_Questions", "testing.Question",
        ])

        auction.distribution_auction_created = False
        # print("auction.distribution_auction_created = False")
        log.info("auction.distribution_auction_created = False")
        # auction.save(update_fields=['distribution_auction_created'])
        auction.save_and_cache()


    # this belongs more with testing app!
    def testing_start(auction, treatment):
        from testing.models import Question, Player_Questions
        from forward_and_spot.models import Timer
        # initialize the questions
        # treatment = auction.treatment
        if Question.get_totalquestions(auction) == 0:
            auction.testing_totalquestions = Question.define_questions(treatment, auction)
            auction.save_and_cache()
            tt = Timer.objects.get_or_create(pk=1)[0]
            tt = tt.timer_set(time_length=treatment.time_for_testing)
            tt.save_and_cache()
        elif not auction.testing_player_questions_defined:
            auction = Player_Questions.define_player_questions(auction)

        auction.app = Auction.TESTING
        auction.app_testing_started = True
        # auction.save(update_fields=['app', 'app_testing_started'])
        log.info("auction.testing_totalquestions:{}".format(auction.testing_totalquestions))
        auction.save_and_cache()
        Auction.set_new_app_state(auction)
        # auction.testing_start()
        auction.save_and_cache()
        MasterMan.refresh_all_connected()
        tt = Timer.cache_get()
        tt = tt.timer_set(treatment.time_for_testing)
        tt.cache_me()


    # this belongs more with payout app!
    def payout_start(auction):
        auction.app = Auction.PAYOUT
        auction.save_and_cache()
        Auction.set_new_app_state(auction)
        MasterMan.refresh_all_connected()


    def make_instruction_pdf_func(self):
        # log.info("auction.distribution_auction_created:{}".format(self.distribution_auction_created))
        self.make_instruction_pdf = not self.make_instruction_pdf
        master_man = MasterMan.cache_or_create_mm()
        master_man.no_test =False
        master_man.save_and_cache()
        self.save_and_cache()
        MasterMan.refresh_all_connected()
        # log.info("auction.distribution_auction_created:{}".format(self.distribution_auction_created))

    def delete_playerstats_main(auction):
        MasterMan.invalidate_caches()
        auction.remove_all_objects_in_class([
            "forward_and_spot.Player_stats", "forward_and_spot.Period"
        ])
        auction.player_stats_created = False
        auction.save_and_cache()


    def  show_ids_toggle(self):
        self.show_ids= not self.show_ids
        self.save_and_cache()
        master_man = MasterMan.cache_or_create_mm()
        master_man.no_test = False
        master_man.save_and_cache()
        MasterMan.refresh_all_connected()


    def remove_userless_players(auction):
        print("remove_userless_players(auction)")
        # from forward_and_spot.models import Player
        # from dAuction2.models import User
        # user_list = User.objects.filter(logged_in=True).exclude(id=99)
        # for user in user_list:
        #     if not Player.objects.filter(auction=auction, user=user).exists():
        #         user.logged_in = False
        #         # print("self.logged_in = False__ in set_state")
        #         user.save()


    def demand_draws_create_main(auction, treatment):
        from distribution.models import Distribution
        from testing.models import Question,Player_Questions
        # print(f"auction.distribution_auction_created:{auction.distribution_auction_created}")
        if not auction.distribution_auction_created:
            Distribution.demand_draws_create(auction, treatment)
            # auction.create_sample_values()

            # START: These values should belong to Distribution object!
            auction.demand_avg = \
            list(Distribution.objects.filter(auction=auction).aggregate(Avg('demand_draw')).values())[
                0]
            auction.demand_sd = \
                list(Distribution.objects.filter(auction=auction).aggregate(StdDev('demand_draw')).values())[0]
            # log.info('auction.demand_avg:' ,auction.demand_avg )
            auction.price_avg = \
            list(Distribution.objects.filter(auction=auction).aggregate(Avg('price_draw')).values())[0]
            auction.price_sd = \
            list(Distribution.objects.filter(auction=auction).aggregate(StdDev('price_draw')).values())[
                0]
            auction.cov_DP = list(Distribution.objects.filter(auction=auction).aggregate(Avg('DP')).values())[0] - (
                    auction.price_avg * auction.demand_avg)
            log.info("auction.cov_DP___________:".format(auction.cov_DP))
            auction.distribution_auction_created = True
            auction.save_and_cache()

        if Question.get_totalquestions(auction) == 0:
            auction = Auction.cache_get()
            auction.testing_totalquestions = Question.define_questions(treatment, auction)
            auction.save_and_cache()
        elif not auction.testing_player_questions_defined:
            auction = Player_Questions.define_player_questions(auction)
        auction.save_and_cache()


    def reset_players(auction):
        from .models import Player, Group
        """
        Resets and creates new auction       
        """
        MasterMan.invalidate_caches()
        # print("reset_players3")
        player_to_remove_list = Player.objects.filter(auction=auction, user__isnull=True)
        log.info("player_to_remove_list:{}".format(player_to_remove_list))
        player_to_remove_list.delete()
        log.info("player_to_remove_list:{}".format(player_to_remove_list))
        player_list = Player.objects.filter(auction=auction, user__isnull=False)
        for player in player_list:
            user = player.user
            user.state = 2
            user.logged_in = True
            user.fail = False
            # print("user.fail:{}".format(user.fail ))
            user.save()
            # user.NO_PL()
            player.user = None
        bulk_update(player_list, update_fields=['user',])
        auction.auction_abort()
        log.info("call_demand_draws_delete_outside")
        auction.demand_draws_delete()
        cache.set("player_list", None)
        auction.remove_all_objects_in_class([
            # "instructions.Page",
            "distribution.Distribution",
            "testing.Player_Questions", "testing.Question",
            "forward_and_spot.Voucher","forward_and_spot.VoucherRE","forward_and_spot.Offer","forward_and_spot.Group","forward_and_spot.Phase","forward_and_spot.Period","forward_and_spot.Penalty"

        ])
        auction.testing_player_questions_defined = False
        auction.auction_created = False
        auction.app = Auction.WAIT
        auction.app_testing_started = False
        # auction.instructions_started = False
        auction.auction_started = False
        auction.end = False
        auction.players_one_logged = False
        auction.logging_requirement_overruled = True
        auction.app_waiting = False
        auction.start_next_period = False
        auction.first_period = True
        auction.demand_curtailment_warning = False
        auction.app_waiting = False
        auction.distribution_auction_created = False
        log.info("auction.distribution_auction_created = False")
        auction.save_and_cache()
        auction.remove_all_objects_in_class(["forward_and_spot.Player_stats",])
        Group.objects.filter(auction=auction).delete()


    def make_strongest_together(self):
        treatment = self.treatment
        self.strongest_together(treatment)
        MasterMan.refresh_all_connected()


    def make_kill_removed(self):
        self.kill_removed = True
        self.save_and_cache()
        MasterMan.refresh_all_connected()


    def         revive_removed(self):
        self.kill_removed = False
        self.save_and_cache()
        MasterMan.refresh_all_connected()


    def  make_removing(self):
        self.removing = True
        self.save_and_cache()
        # MasterMan.refresh_all_connected()
        from forward_and_spot.models import Player
        Player.refresh_all_players(only_unselected=True)


    def         make_random_together(self, treatment):
        self.strongest_together(treatment, random=True)
        MasterMan.refresh_all_connected()


    def  make_unremoving(self):
        self.removing = False
        self.save_and_cache()
        # MasterMan.refresh_all_connected()
        from forward_and_spot.models import Player
        Player.refresh_all_players(only_unselected=True)

    def make_shedding(auction, treatment):
        from forward_and_spot.models import Player, Group
        log.debug("shedding")
        # AuctionManager.remove_player_stats(auction)
        # remove from F&S Playerstats
        auction.remove_all_objects_in_class(["forward_and_spot.Player_stats"])
        auction.player_stats_created = False
        players_shed = Player.objects.select_related('user').filter(auction=auction, selected=False)
        i = 0
        for player in players_shed:
            i += 1
            player.selected = False
            log.info("shed: {}".format(i))
        bulk_update(players_shed, update_fields=['selected'])
        auction.save_and_cache()


    def summ_instructions_start_main(auction, treatment):
        from forward_and_spot.models import Player, Timer
        MasterMan.cache_it("page_list", None)
        auction.instructions_start(treatment, Auction.SUMMARY_INSTR)
        tt = Timer.objects.get_or_create(pk=1)[0]
        tt = tt.timer_set(time_length=treatment.time_for_instructions)
        tt.cache_me()
        auction.save_and_cache()
        MasterMan.refresh_all_connected()


    def auction_ready(self, treatment):
        from forward_and_spot.models import Phase, Period, Timer
        from .models import Player_stats
        treatment = self.treatment
        period = Period.objects.get(idd=1, auction=self)
        period.save()
        if treatment.only_spot:
            phase = Phase.objects.get_or_create(auction=self, period=period, idd=2)[0]
        else:
            phase = Phase.objects.get_or_create(auction=self, period=period, idd=1)[0]
        phase.save()
        self.app = Auction.FS
        self.end = False
        self.save(update_fields=['app', 'end'])
        player_stats_list = Player_stats.objects.filter(auction=self)
        for player_stats in player_stats_list:
            player_stats.units_missing = player_stats.get_units_missing_tot()
        bulk_update(player_stats_list, update_fields=['units_missing'])
        Auction.set_new_app_state(self)
        self.save_and_cache()
        tt = Timer.cache_get()
        if not tt:
            tt = Timer.objects.get_or_create(pk=1)[0]
        tt = tt.timer_set(time_length=treatment.time_for_question_page, short_time_length=None)
        tt.cache_me()
        tt.save_and_cache()
        # MasterMan.refresh_all_connected()
        from forward_and_spot.models import Player
        Player.refresh_all_players(only_selected=True)


    # this belongs more with Distribution app!
    def distribution_cancel(self):
        self.app = Auction.WAIT
        self.save_and_cache()
        Auction.set_new_app_state(self)
        MasterMan.refresh_all_connected()


    # this belongs more with Instructions app!
    def instructions_start(self, treatment,itype= SUMMARY_INSTR):
        from forward_and_spot.models import Timer
        self.app = Auction.INSTR
        self.itype = itype
        if not self.instructions_created:
            self.instructions_created = self.instructions_create()
        self.save(update_fields=['app', 'itype', 'instructions_created'])
        log.info("itype:{}".format(self.itype))
        Auction.set_new_app_state(self)
        Timer.objects.all().delete()
        log.info("Timer.objects.exists():{}".format(Timer.objects.exists()))

    # this belongs more with Instructions app!
    def instructions_cancel(self):
        self.app = Auction.WAIT
        Auction.set_new_app_state(self)
        self.instructions_created = False
        # self.save(update_fields=['app', 'instructions_created'])
        self.save_and_cache()
        MasterMan.refresh_all_connected()


    def auction_create_main(auction, treatment):
        from .models import Group, Timer
        log.info("----------------------auction NOT yet created")
        cache.set("player_list", None)
        log.info("MasterMan.invalidate_caches() in auction_create")
        log.info("call_invalidate_caches_outside")
        MasterMan.invalidate_caches()
        log.info("call_demand_draws_delete_outside")
        auction.demand_draws_delete()
        log.info("call_auction_init(treatment)")

        auction.auction_created = auction.auction_init(treatment)
        auction.instructions_created = auction.instructions_create()
        auction.save_and_cache()
        tt = Timer.objects.get_or_create(pk=1)[0]
        tt.cache_me()
        # group_list = Group.objects.filter(auction=auction)
        group_list = Group.get_groups(auction)
        MasterMan.cache_it("group_list", group_list)
        auction.save_and_cache()
        MasterMan.refresh_all_connected()


    # this belongs more with testing app!
    def testing_delete(self):
        from forward_and_spot.models import Player
        self.app = Auction.WAIT
        self.app_testing_started = False
        self.app_testing_ended = False
        self.testing_totalquestions = 0
        self.testing_questions_defined = False
        self.testing_player_questions_defined = False
        self.save(update_fields=['app_testing_ended', 'app', 'app_testing_started', 'testing_questions_defined','testing_player_questions_defined','testing_totalquestions'])

        self.remove_all_objects_in_class(["testing.Player_Question_Options",
            "testing.Player_Questions",
            "testing.Option_MC",
            "testing.Question",])

        Player.objects.all().update(testing_trials=0, testing_errors=0, testing_correct=0, page=1)
        MasterMan.cache_it('Timer', None)
        self.save_and_cache()
        MasterMan.refresh_all_connected()
        return self

    # this belongs more with testing app!
    def testing_cancel(auction):
        from forward_and_spot.models import Player
        auction.app = Auction.WAIT
        auction.app_testing_started = False
        auction.app_testing_ended = False
        # auction.save(update_fields=['app_testing_ended', 'app', 'app_testing_started'])
        auction.save_and_cache()
        MasterMan.cache_it('Timer', None)
        auction.save_and_cache()
        MasterMan.refresh_all_connected()
#Player.refresh_all_players()

    def         create_group_main(auction):
        from .models import Group
        lastgroup = Group.objects.filter(auction=auction).all().order_by('id').last()
        newid=lastgroup.idd+1
        group=Group(auction=auction,idd=newid)
        group.save_and_cache()

    def unstuck_all_in_payout(auction):
        from forward_and_spot.models import Player
        auction.payout_cancel()
        auction.save_and_cache()
        # ToDo: call masterman for unstuck connected
        # masterman asks Player to unstuck
        # Player unstucks player
        players_stuck = Player.objects.filter(app=Player.PAYOUT)
        for player in players_stuck:
            player.app = 0
            player.save()
        # back here?
        MasterMan.refresh_all_connected()


    # this belongs more with payout app!
    def payout_cancel(auction):
        auction.app = Auction.WAIT
        # print("in payout_cancel auction.app:{}".format(auction.app))
        log.info("auction.app:{}".format(auction.app))
        auction.save_and_cache()
        MasterMan.refresh_all_connected()


    def auction_init(auction, treatment):
        """
        Creates an auction by giving all players (logged in or not) voucher objects
        """
        from .models import Player, Group
        # log.info("auction_init2!!!")
        auction.remove_all_objects_in_class([
            "distribution.Distribution",
            "forward_and_spot.Player_stats","forward_and_spot.Group","forward_and_spot.Player","forward_and_spot.Penalty", "forward_and_spot.Period","forward_and_spot.Offer",
            "testing.Player_Questions", "testing.Question",
        ])
        auction.db_reset()
        auction.auction_started = False
        auction.auction_finished = False
        auction.removing = False
        auction.player_stats_created = False
        auction.app = Auction.WAIT
        auction.treatment = treatment
        auction.ECU_per_CZK_RE = treatment.ECU_per_CZK_RE
        auction.ECU_per_CZK_PR = treatment.ECU_per_CZK_PR
        auction.end = False
        auction.demand_curtailment_warning = False
        auction.first_period = True  # this is for auction initialization
        # log.info("auction.shedding= ",auction.shedding)
        # print("player_objects:{}".format(Player.objects.filter(auction=auction).count()))

        # if not treatment.groups_assignment_alternate:
        if False:
            # for group_count in range(1,treatment.total_groups + 1):
            #     group=Group.objects.get_or_create(auction=auction,idd=group_count)[0]
            #     group.save()
            #     j=1
            #     to_add_player=[]
            #     for i in range(1,treatment.PR_per_group + 1):
            #         p=Player(auction=auction,group=group,role=Player.PR, user=None)
            #         to_add_player.append(p)
            #         # p.save()
            #         log.info("i:{}".format(i))
            #     # msg = Player.objects.bulk_create(to_add_player)
            #     # to_add_player = []
            #     for i in range(j, treatment.RE_per_group + 1):
            #         p = Player(auction=auction, group=group, role=Player.RE, user=None)
            #         to_add_player.append(p)
            #         # p.save()
            #     msg = Player.objects.bulk_create(to_add_player)
            pass
        else:
            # print("before for_loop: for group_count in range(1, treatment.total_groups + 1):")
            # print("treatment.total_groups:{}".format(treatment.total_groups))
            for group_count in range(1, treatment.total_groups + 1):
                # print("before assigning group")
                # print("auction:{}".format(auction))
                log.info("auction:{}".format(auction))
                # print("all auctions:{}".format(Auction.objects.all()))
                # print("group_count:{}".format(group_count))
                # print("auction.get_uid(group_count):{}".format(auction.get_uid(group_count)))
                # print("Group.get_groups(auction):{}".format(Group.get_groups(auction)))
                # group = Group.objects.get_or_create(id=auction.get_uid(group_count), auction=auction, idd=group_count)[0] # this line comes up in test with DoesNotExist: Group matching query does not exist.
                group = Group.objects.create(id=auction.get_uid(group_count), auction=auction, idd=group_count)
                # print("before printing group")
                # print("group:{}".format(group))
                group.save()
                j = 1
                PR_per_group = treatment.PR_per_group
                RE_per_group = treatment.RE_per_group
                # to_add_player = []
                # p = Player(id=auction.get_uid(0),auction=auction, group=group, role=Player.PR, user=None)
                # p.save()
                # p.delete()
                # print("before for_loop: for i in range(1, treatment.get_total_players + 1)")
                for i in range(1, treatment.get_total_players + 1):
                    if PR_per_group > 0:
                        # p=Player(id=auction.get_uid((group_count -1) * treatment.get_total_players + (2*i-1)),auction=auction,group=group,role=Player.PR, user=None)
                        p = Player(auction=auction, group=group, role=Player.PR, user=None)
                        # to_add_player.append(p)
                        p.save()
                        PR_per_group -= 1
                        # log.info("___________pPR", p, " --", PR_per_group)
                    if RE_per_group > 0:
                        # p = Player(id=auction.get_uid((group_count -1) * treatment.get_total_players +  (2*i)),auction=auction, group=group, role=Player.RE, user=None)
                        p = Player(auction=auction, group=group, role=Player.RE, user=None)
                        # to_add_player.append(p)
                        p.save()
                        RE_per_group -= 1
                        log.info("___________pRE:{} ---RE_per_group:{}".format(p, RE_per_group))
                # log.info("to_add_player:{}".format(to_add_player))
                # msg = Player.objects.bulk_create(to_add_player)
        # to_add_player = []
        for i in range(1, treatment.shedding + 1):
            p = Player(auction=auction, group=group, role=0, user=None, selected=False)
            p.save()
            # to_add_player.append(p)
        # msg = Player.objects.bulk_create(to_add_player)
        return True


    def auction_start(self, treatment):
        from forward_and_spot.models import Phase, Period, Timer
        log.info("auction start")
        self.auction_started = True
        self.save(update_fields=['auction_started'])
        period = Period.objects.get(auction=self, idd=1)
        if treatment.only_spot:
            phase = Phase.objects.get(auction=self, period=period, waiting_page=False, idd=2)
            phase.question_page = False
        else:
            phase = Phase.objects.get(auction=self, period=period, waiting_page=False, idd=1)
            phase.question_page = True
        phase.save()
        Auction.set_new_app_state(self)
        tt = Timer.cache_get()
        if not tt:
            tt = Timer()
        tt = tt.timer_set(time_length=treatment.time_for_question_page, short_time_length=None)
        tt.save_and_cache()
        self.save_and_cache()


    def auction_clear(self):
        """
        Resets and creates new auction
        """
        log.info("call_invalidate_caches_outside")
        MasterMan.invalidate_caches()
        cache.set('voucher_list', '')
        cache.set('vouchers_ser', '')
        self.auction_started = False
        self.auction_finished = False
        self.app = Auction.WAIT
        Auction.set_new_app_state(self)
        # remove F&S
        self.remove_all_objects_in_class( [
            "forward_and_spot.Player_stats",
            "forward_and_spot.Penalty",
            "forward_and_spot.Offer",
            "forward_and_spot.Phase",
            "forward_and_spot.Period",
            "testing.Player_Questions", "testing.Question",
        ])
        self.player_stats_created = False
        self.save(update_fields=['auction_started', 'app', 'auction_finished'])
        self.save_and_cache()
        MasterMan.refresh_all_connected()


    def auction_abort(auction):
        log.info("auction_abort2!!!")
        auction.remove_all_objects_in_class( ["forward_and_spot.Player_stats", ])
        auction.player_stats_created = False
        auction.removing = False
        auction.app = Auction.WAIT
        auction.auction_started = False
        auction.auction_finished = True
        auction.save_and_cache()
        Auction.set_new_app_state(auction)
        MasterMan.refresh_all_connected()


    def determine_payment_statistics(self):
        from forward_and_spot.models import Player
        # hmmm, how to make this coupling looser?
        # print("determine_payment_statistics2!!!")

        all_for_RE = Player.objects.exclude(payout_CZK=-1).filter(auction=self, role=Player.RE,
                                                                  selected=True).aggregate(Avg('payout_CZK'),
                                                                                           Max('payout_CZK'),
                                                                                           Min('payout_CZK'))
        all_for_PR = Player.objects.exclude(payout_CZK=-1).filter(auction=self, role=Player.PR,selected=True).aggregate(Avg('payout_CZK'),Max('payout_CZK'),Min('payout_CZK'))
        all_for_RE_corr = Player.objects.exclude(payout_CZK=-1).filter(auction=self, role=Player.RE,selected=True).aggregate(Avg('payout_CZK'), Max('payout_CZK'), Min('payout_CZK'))
        all_for_PR_corr = Player.objects.exclude(payout_CZK=-1).filter(auction=self, role=Player.PR,selected=True).aggregate(Avg('payout_CZK'), Max('payout_CZK'), Min('payout_CZK'))
        corr_list_PR = Player.objects.exclude(payout_CZK=-1).filter(auction=self, role=Player.PR, selected=True)
        corr_list_RE = Player.objects.exclude(payout_CZK=-1).filter(auction=self, role=Player.RE, selected=True)
        # print("int(Player.objects.exclude(payout_CZK=-1).aggregate(Avg('payout_CZK'))['payout_CZK__avg']:{}".format(int(Player.objects.exclude(payout_CZK=-1).filter(auction=self).aggregate(Avg('payout_CZK'))['payout_CZK__avg'])))
        if all_for_RE['payout_CZK__avg']:
            self.av_paid_RE = int(all_for_RE['payout_CZK__avg'])
            # print("self.av_paid_RE:{}".format(self.av_paid_RE))
        if all_for_RE['payout_CZK__min']:
            self.min_paid_RE = int(all_for_RE['payout_CZK__min'])
        if all_for_RE['payout_CZK__max']:
            self.max_paid_RE = int(all_for_RE['payout_CZK__max'])
        # for obj in corr_list_PR:
            # print("obj for obj in corr_list_PR:{}".format(obj.payout_CZK_corr))
        self.av_paid_PR = int(all_for_PR['payout_CZK__avg'])
        self.min_paid_PR = int(all_for_PR['payout_CZK__min'])
        self.max_paid_PR = int(all_for_PR['payout_CZK__max'])
        if corr_list_PR:
            self.av_paid_PR_corr = int(sum(obj.payout_CZK_corr for obj in corr_list_PR) / len(corr_list_PR))
            self.min_paid_PR_corr = int(min(obj.payout_CZK_corr for obj in corr_list_PR))
            self.max_paid_PR_corr = int(max(obj.payout_CZK_corr for obj in corr_list_PR))
            # print("self.av_paid_PR_corr:{}".format(self.av_paid_PR_corr))
            # print("self.min_paid_PR_corr:{}".format(self.min_paid_PR_corr))
            # print("self.max_paid_PR_corr:{}".format(self.max_paid_PR_corr))

        if corr_list_RE:
            self.av_paid_RE_corr = int(sum(obj.payout_CZK_corr for obj in corr_list_RE) / len(corr_list_RE))
            # print("self.av_paid_RE:{}".format(self.av_paid_RE))
            self.min_paid_RE_corr = int(min(obj.payout_CZK_corr for obj in corr_list_RE))
            self.max_paid_RE_corr = int(max(obj.payout_CZK_corr for obj in corr_list_RE))
            # print("self.av_paid:{}".format(self.av_paid, ))
        # print("self.av_paid:{}".format(self.av_paid, ))
        return self

    # belongs more to INstructions!
    def instructions_create(self):
        log.info("instructions_create2!!!")
        # pname = "instructions/templates/instructions/pages"
        # summ_pname = "instructions/templates/instructions/pages_summary"
        from dAuction2.settings import INSTALLED_APPS
        if "testing" in INSTALLED_APPS:
            log.info("testing in INSTALLED_APPS!")
            from testing.models import Question
            self.testing_totalquestions = Question.get_totalquestions(self)
        # print("self.testing_totalquestions :{}".format(self.testing_totalquestions ))
        # print("type:{}".format(type(self.testing_totalquestions)))
        # summ_spname = "instructions/pages_summary"
        # spname = "instructions/pages"
        # idd = 1
        # to_add_page = []
        self.save()
        return True


    def make_logout_all(self):
        print("make_logout_all!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        log.info("make_logout_all!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        from dAuction2.models import User
        log.info("TRUE+++++++++++++++++++++++++++++++++++++++++++++++++++++")
        user_list = User.objects.exclude(id=99).all().order_by('id')
        log.info('user_list:{}'.format( user_list))
        for user in user_list:
            user.LOGGED_OUT(self)
            log.info("for user:{}, .logged_in:{}".format(user, user.logged_in))
            user.logged_in=False
            print("self.logged_in = False__ in  elif 'logout_all' in request.POST['name']")
            log.info("for user:{}, .logged_in:{}".format(user, user.logged_in))
            user.save()
        bulk_update(user_list,update_fields=['state','logged_in','fail'])
        MasterMan.refresh_all_connected()


    def auction_delete(self):
        self.remove_all_objects_in_class( [
            "forward_and_spot.Phase",
            "distribution.Distribution",

            "testing.Question", "testing.Player_Questions", "testing.Option_MC", "testing.Player_Question_Options",
            "forward_and_spot.Player_stats","forward_and_spot.Offer","forward_and_spot.Voucher","forward_and_spot.VoucherRE","forward_and_spot.Penalty","forward_and_spot.Period","forward_and_spot.Timer"
            ])
        cache.set('voucher_list', '')
        cache.set('vouchers_ser', '')
        log.info("call_invalidate_caches_outside")
        log.info("delete_in_requestpost")
        MasterMan.invalidate_caches()
        treatment_list = Treatment.objects.filter(au=self.id)
        for treatment in treatment_list:
            treatment.delete()
        # treatment=self.treatment
        # treatment.delete()
        self.delete()


    def get_uid(self,i):
        return 1000000 * self.pk + i

    @property
    def max_paid(self):
        return max(self.max_paid_RE, self.max_paid_PR)

    @property
    def min_paid(self):
        return min(self.min_paid_RE, self.min_paid_PR)

    @property
    def av_paid(self):
        return (self.treatment.RE_per_group * self.av_paid_RE + self.treatment.PR_per_group * self.av_paid_PR)/(self.treatment.RE_per_group + self.treatment.PR_per_group)

    @property
    def av_paid_corr(self):
        return (self.treatment.RE_per_group * self.av_paid_RE_corr + self.treatment.PR_per_group * self.av_paid_PR_corr)/(self.treatment.RE_per_group + self.treatment.PR_per_group)

    @property
    def get_average_uniform(self):
        return (self.uniform_min + self.uniform_max)/2

    @property
    def min_paid_corr(self):
        return min(self.min_paid_RE_corr, self.min_paid_PR_corr)

    @property
    def max_paid_corr(self):
        return max(self.max_paid_RE_corr, self.max_paid_PR_corr)