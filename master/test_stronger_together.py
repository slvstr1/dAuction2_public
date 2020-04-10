from dAuction2.settings import UNIQUEIZER
import json
from django.core.cache import cache
# import mock
from django_bulk_update.helper import bulk_update
from django.test import Client
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
from master.views import main
from django.http import *
from master.models import MasterMan

class test_stronger_together(TransactionTestCase):


    def setUp(self):
        log.info("**********************")
        log.info("setUp")
        log.info("**********************")
        print("+" * 40)
        print("")
        delete_all(self)
        function_in_FS_views_with_auction_setup.setUp(self)
        auction, treatment = Auction.cache_or_create_auction()
        auction.auction_create_main(treatment)
        User.users_create(auction)
        user_list = User.objects.order_by("id").all()
        for user in user_list:
            user.logged_in=True
        bulk_update(user_list, update_fields=['logged_in'])



    def tearDown(self):
        delete_all(self)
        log.info("**********************")
        log.info("tearDown --- DELETED")
        log.info("**********************")

    def test_stronger_together(self):

        print("create 24 players from the users by logging them in")
        auction, treatment = Auction.cache_or_create_auction()

        user_list=User.objects.exclude(id=99)[0:24]
        print("user_list:{}".format(user_list))
        # user=user_list.pop()
        for user in user_list:
            print("user.logged_in:{}".format(user.logged_in))
            self.factory = RequestFactory()
            request = self.factory.get('/')
            request.session = {}
            request.user = user
            response = main(request)
            print("response:", response)
            print("response.content:", response.content)
            player = user.player.get(auction=auction)
            print("player:{}".format(player))
            self.assertEqual(player.id, (auction.id * UNIQUEIZER) + user.id)
            print("SUCCES+++++++++++++++++++++++++++++++:self.assertEqual(player.id,(auction.id * UNIQUEIZER)+ user.id)")

        player_list = Player.objects.filter(auction=auction, user__isnull=False)
        self.assertEqual(player_list.count(), 24)
        print("SUCCES+++++++++++++++++++++++++++++++: self.assertEqual(player_list.count() ,24")

        print("")
        print("")
        print("")

        print("test stronger_together")

        for player in player_list:
            player.testing_errors = player.user_id //2
            player.testing_correct = player.user_id
            player.testing_finished = (player.user_id % 6 != 0)
            player.save()

        print("treatment.shedding:{}".format(treatment.shedding))
        strongest_together = True
        highest_error = 0
        highest_error_selected = 0
        for player in player_list:
            highest_error = max(highest_error, player.testing_errors)
            if player.testing_finished:
                highest_error_selected = max(highest_error, player.testing_errors)
        print("highest_error_selected:{}".format(highest_error_selected))


        for player in player_list:
            if player.selected:
                if player.testing_errors > highest_error_selected:
                    strongest_together = False
                if not player.testing_finished:
                    strongest_together = False
        self.assertFalse(strongest_together)
        print("SUCCESS+++++++++++++++++++++++++++++++++++++: self.assertFalse(strongest_together)")

        strongest_together=True
        for player in player_list:
            print("{}, selected:{}, errors:{}, fin:{}".format(player.id,player.selected,player.testing_errors,player.testing_finished))
        auction.make_strongest_together()

        player_list = Player.objects.filter(auction=auction, user__isnull=False)
        for player in player_list:
            print("{}, selected:{}, errors:{}, fin:{}".format(player.id,player.selected,player.testing_errors,player.testing_finished))
        for player in player_list:
            if player.selected:
                if player.testing_errors > highest_error_selected:
                    if player.testing_finished:
                        strongest_together = False
                if not player.testing_finished:
                    strongest_together = False
        self.assertTrue(strongest_together)


        for player in player_list:
            print("".format(player.id,player.selected,player.testing_errors))
            if player.selected:
                self.assertLessEqual(player.testing_errors,highest_error_selected)
                self.assertTrue(player.testing_finished)



        # self.assertTrue(False)
