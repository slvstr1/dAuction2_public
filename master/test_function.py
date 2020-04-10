import json
from django.core.cache import cache
from django.test import TestCase, RequestFactory, TransactionTestCase
from forward_and_spot.models import VoucherRE,Voucher,Offer, Auction, Player, Group, Player_stats, Period, Phase, Timer, Treatment
from testing.models import Player_Questions, Question
from distribution.models import Distribution
from dAuction2.models import Experiment
from dAuction2.models import User
from forward_and_spot.test_views_set_offer import function_in_FS_views_with_auction_setup, delete_all
# from testing.functions import define_questions
# from master.functions_main import  cache_me, invalidate_caches
# from .functions import treatment_create, instructions_cancel,distribution_start,distribution_cancel,testing_start,testing_cancel,testing_delete,auction_start,auction_abort,auction_clear, questionnaire_start,questionnaire_cancel,payout_start,payout_cancel,
from .functions import *
import time

from django.http import *
from master.models import MasterMan

class test_demand_draws_create(TransactionTestCase):

    def setUp(self):
        log.info("**********************")
        log.info("setUp")
        log.info("**********************")
        print("+" * 40)
        print("")
        # self.delete_all()
        delete_all(self)
        function_in_FS_views_with_auction_setup.setUp(self)

    def tearDown(self):
        # self.delete_all()
        delete_all(self)
        # Clean up run after every test method.
        # from forward_and_spot.models import Voucher
        # from distribution.models import Distribution
        # MasterMan.invalidate_caches()
        # Offer.objects.all().delete()
        # Player.objects.all().delete()
        # Player_stats.objects.all().delete()
        # Auction.objects.all().delete()
        # Period.objects.all().delete()
        # Phase.objects.all().delete()
        # Group.objects.all().delete()
        # Voucher.objects.all().delete()
        # Timer.objects.all().delete()
        # Distribution.objects.all().delete()
        # User.objects.all().delete()
        # Treatment.objects.all().delete()
        log.info("**********************")
        log.info("tearDown --- DELETED")
        log.info("**********************")

    def test_demand_draws_create(self):
        # treatment = Treatment.cache_or_create_treatment()
        # treatment.save
        # auction = Auction.create(treatment)
        # auction.save
        # treatment=cache.get("treatment")
        # auction=cache.get("auction")
        auction, treatment = Auction.cache_or_create_auction()
        log.info("auction:{}".format(auction))
        # treatment.d_draws_needed=100
        # treatment.save_and_cache()
        
        # MasterMan.cache_me("treatment",treatment)
        start=time.time()
        # auction = Distribution.demand_draws_create(auction, treatment)
        end=time.time()
        log.info("total time: {}".format(end-start,3))
        n_draws=Distribution.objects.all().count()
        log.info("n_draws:{}".format(n_draws))
        self.assertEqual (n_draws,treatment.d_draws_needed*5 + treatment.total_groups * treatment.total_periods)

        n_vouchers=Voucher.objects.all().count()
        log.info("n_vouchers:{}".format( n_vouchers))
        self.assertEqual(n_vouchers, treatment.max_vouchers)

        n_vouchersRE= VoucherRE.objects.all().count()
        print("n_vouchersRE:", n_vouchersRE)
        self.assertEqual (n_vouchersRE , 11)

    def test_PlayerStats_create(self):
        # Player.objects.all().delete()
        # User.objects.all().delete()
        # Distribution.objects.all().delete()
        # treatment = Treatment.cache_or_create_treatment()
        # treatment.save
        # auction = Auction.create(treatment)
        # auction.save
        auction, treatment = Auction.cache_or_create_auction()
        # group1 = Group(idd=1,auction=auction)
        # group1.save()
        # group2 = Group(idd=2,auction=auction)
        # group2.save()
        # user=User()
        # user.save()
        # player=Player(user=user,selected=True,auction=auction,group=group1)
        # player.save()
        # player=createPlayer(user,auction)


        # treatment=cache.get("treatment")
        # auction=cache.get("auction")
        # print("auction:",auction)
        # treatment.d_draws_needed=100
        
        # MasterMan.cache_me("treatment",treatment)
        # start=time.time()
        # Player_stats.playerStats_create(auction, treatment)

        # end=time.time()
        # print("total time: {}".format(end-start,3))
        n_PS=Player_stats.objects.all().count()
        # print("n_PS:",n_PS)
        self.assertEqual (n_PS,treatment.total_groups * ( treatment.RE_per_group + treatment.PR_per_group) * treatment.total_periods)
        #
        # n_vouchers=Voucher.objects.all().count()
        # print("n_vouchers:", n_vouchers)
        # assert(n_vouchers==treatment.max_vouchers)
        #
        # n_vouchersRE= VoucherRE.objects.all().count()
        # print("n_vouchersRE:", n_vouchersRE)
        # assert (n_vouchersRE == 11)
        # assert (False)

    def test_instructions_cancel(self):
        auction, treatment = Auction.cache_or_create_auction()

        # Player.objects.all().delete()
        # treatment = Treatment.cache_or_create_treatment()
        # treatment.save
        # auction = Auction.create(treatment)
        # auction.save
        group_list=Group.objects.filter(auction=auction)
        group1 = group_list.last()
        # group1.save()
        group2 = group1 = group_list.first()
        # group2.save()
        user = User()
        user.save()
        player = Player(user=user, selected=True, auction=auction, group=group1,page=99,app=99)
        player.save()
        player_list = Player.objects.filter(auction=auction, user__isnull=False)
        for player in player_list:
            # print("app:",             player.app)
            # print("player.page:", player.page)
            assert(player.page==99)
            assert (player.app == 99)
        # auction.instructions_started = True
        auction.save()
        auction.instructions_cancel()
        # MasterMan.cache_me('auction', auction)
        auction.save_and_cache()
        player_list = Player.objects.filter(auction=auction, user__isnull=False)
        for player in player_list:
            assert (player.page == 1)
            assert (player.app == 0)

        # log.info("distribution_start(auction)")
        auction.distribution_start(treatment)
        tt = Timer.objects.get_or_create(pk=1)[0]
        tt = tt.timer_set(time_length=treatment.time_for_distribution)
        tt.cache_me()

        player_list = Player.objects.filter(auction=auction, user__isnull=False)
        for player in player_list:
            # print("player.page:",player.page)
            # print("app:",player.app)
            # self.assertEqual(player.app, 0)
            self.assertEqual (player.state , 2)
            # WORKINGv=2
            # print("state:", player.state)



        # print("distribution_cancel(auction)")
        auction.distribution_cancel()
        player_list = Player.objects.filter(auction=auction, user__isnull=False)
        for player in player_list:
            # print("player.page:",player.page)
            # print("app:",player.app)
            self.assertEqual(player.app,0)
            self.assertEqual (player.draw_id , 0)
            self.assertEqual (player.page , 1)
            self.assertEqual (player.state , 1)
            # WAIT =1
            # print("state:", player.state)

        # print("testing_start(auction)")
        # testing_start(treatment, auction)
        if not auction.testing_questions_defined:
            auction.testing_totalquestions = Question.define_questions(treatment, auction)
        elif not auction.testing_player_questions_defined:
            auction = Player_Questions.define_player_questions(auction)

        auction.testing_start(treatment)
        auction.save_and_cache()
        player_list = Player.objects.filter(auction=auction, user__isnull=False)
        for player in player_list:
            # print("player.page:",player.page)
            # print("app:", player.app)
            # self.assertEqual (player.app , 0)
            self.assertEqual (player.draw_id , 0)
            self.assertEqual (player.page , 1)
            self.assertEqual (player.state , 2)
            # WORKINGv=2
            # print("state:", player.state)

        print("testing_cancel(auction)")
        auction.testing_cancel()
        auction.cache_me()
        # MasterMan.cache_me('auction', auction)
        MasterMan.cache_it('Timer', None)
        print("testing_delete(auction)")
        auction.testing_delete()
        MasterMan.cache_me('Timer', None)
        # MasterMan.cache_me('auction', auction)
        auction.cache_me()
        print("auction_ready(auction, treatment)")
        auction.auction_ready( treatment)
        auction.save_and_cache()
        tt = Timer.cache_get()
        if not tt:
            tt = Timer.objects.get_or_create(pk=1)[0]
        tt = tt.timer_set(time_length=treatment.time_for_question_page, short_time_length=None)
        tt.cache_me()
        # state = Player.WAITv
        Player.refresh_all_players()


        print("auction_start(treatment, auction)")
        # auction = auction.auction_start(treatment)
        # auction.save_and_cache()

        auction.auction_start(treatment)
        tt = Timer.cache_get()
        tt = tt.timer_set( time_length=treatment.time_for_question_page, short_time_length=None)
        tt.cache_me()

        print("auction_abort(auction):")

        auction.auction_abort()
        auction.save_and_cache()
        MasterMan.invalidate_caches()
        cache.set('voucher_list', '')
        cache.set('vouchers_ser', '')
        auction.auction_clear()
        auction.save_and_cache()
        tt=Timer(id=1)
        # print("tt:", tt)
        tt.save()
        # print("tt:",tt)
        tt= tt.timer_set( time_length=33)
        # tt.cache_me()
        tt=tt.timer_cut()
        tt.cache_me()

        tt = Timer.cache_get()
        tt.timer_toggle()
        tt.cache_me()

        auction.questionnaire_start()
        auction.questionnaire_cancel()
        # payout_start(auction)
        auction.payout_start()
        auction.payout_cancel()
        Player.refresh_all_players()
        auction.instructions_create()
        # instructions_create(auction)
        player= Player.createPlayer(user, auction)

        # auction_init(auction, treatment)
        period=Period(id=1)
        last_phase=Phase(id=1, period=period)
        # last_phase.next_phase_procedure(auction)
        #
        # auction = auction.instructions_start(treatment,Auction.FULL_INSTR)
        # auction.cache_me()
        # MasterMan.cache_it("Timer", None)
        # tt = Timer.cache_get()
        # # log.info("cache.set('tt'):{}".format(tt))
        # tt = Timer.objects.get_or_create(pk=1)[0]
        # # log.info("SET CACHE")
        #
        # tt = tt.timer_set(time_length=treatment.time_for_instructions)
        # tt.cache_me()
        #
        # # demand_draws_delete(auction)
        # MasterMan.invalidate_caches()
        # auction = auction.demand_draws_delete()
        # auction.save_and_cache()
        # MasterMan.invalidate_caches()
        # auction=auction.reset_players()
        # auction.save_and_cache()
        # auction=auction.shedding(treatment)

        # assert (False)


    # def test_auction_ready(self):
    #     Player.objects.all().delete()
    #     User.objects.all().delete()
    #     Distribution.objects.all().delete()
    #
    #     auction_ready(auction, treatment)
    #     assert (False)
    # def test_treatment_apply(self):
    #     treatment = cache_or_create_treatment()
    #     treatment.save
    #     auction = Auction.create(treatment)
    #     auction.save
    #     group1 = Group(idd=1, auction=auction)
    #     group1.save()
    #     group2 = Group(idd=2, auction=auction)
    #     group2.save()
    #     user = User()
    #     user.save()
    #     player = Player(user=user, selected=True, auction=auction, group=group1, page=99, app=99)
    #     player.save()
    #     treatment_apply(auction,treatment)
