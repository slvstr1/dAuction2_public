import json
from django.core.cache import cache
from django.test import TestCase, RequestFactory
from forward_and_spot.models import Offer, Auction, Player, Group, Player_stats, Period, Phase, Timer, Treatment
from dAuction2.models import Experiment
from dAuction2.models import User
from distribution.models import Distribution
from .master_api import ajax_admin
# from master.functions_main import cache_me, invalidate_caches
from forward_and_spot.test_views_set_offer import delete_all, function_in_FS_views_with_auction_setup
# from .functions_main import strongest_together
import logging
from master.models import MasterMan
log = logging.getLogger(__name__)
from django.http import *


class test_shedding(TestCase):
    def setUp(self):
        print("**********************")
        print("setUp")
        print("**********************")
        delete_all(self)
        print(Phase.objects.all())
        print(Period.objects.all())
        print(Auction.objects.all())
        print(Group.objects.all())
        Player.objects.all().delete()
        User.objects.all().delete()
        print("**********************")
        MasterMan.invalidate_caches()
        self.factory = RequestFactory()
        auction, treatment = Auction.cache_or_create_auction()
        # treatment = Treatment.cache_or_create_treatment()
        treatment.total_periods = 5
        treatment.PR_per_group = 4
        treatment.RE_per_group = 4
        treatment.total_groups = 2
        treatment.shedding = 8
        treatment.save_and_cache()
        # MasterMan.cache_me('treatment',treatment)
        # auction = Auction.create(treatment)
        auction.started = True
        auction.app = Auction.FS
        auction.auction_started = True
        auction.save_and_cache()
        # auction.cache_me()
        # auction=auction.createVoucher(treatment)

        for i in range(1,3):
            group = Group.objects.get_or_create(idd=i, auction=auction)[0]
            group.save()
            # print("group", group)
            # print("Group.objects.all()", Group.objects.all())

        group_list = Group.objects.all()
        for group in group_list:
            for i in range(0, 5):
                user = User.objects.create(username=str(group.idd*100+i))
                player = Player.objects.create(user=user, role=0, auction=auction, group=group)
                player.testing_errors = i+1
                player.testing_finished = True
                player.save()
                user.has_player = True
                user.save()
            for i in range(5, 12):
                user = User.objects.create(username=str(group.idd*100+i))
                player = Player.objects.create(user=user, role=1, auction=auction, group=group)
                player.testing_errors = i+1
                player.testing_finished = True
                player.save()
                user.has_player = True
                user.save()

        player_list = Player.objects.filter(role=0).select_related('group').order_by("group_id", "id")
        # print("number of players role 0:", player_list.count())

        Distribution.demand_draws_create(auction, treatment)

        player_list = Player.objects.all().select_related('group').order_by("group_id", "id")
        # print("number of players:", player_list.count())

        # playerstats_list =Player_stats.objects.all().order_by('id','period','player__user_id')
        # for playerstats in playerstats_list:
        #     print(playerstats)

        print("**********************")
        print("end setUp")
        print("**********************")

    def tearDown(self):
        # Clean up run after every test method.
        from forward_and_spot.models import Voucher
        MasterMan.invalidate_caches()
        Offer.objects.all().delete()
        Player.objects.all().delete()
        Player_stats.objects.all().delete()
        Auction.objects.all().delete()
        Period.objects.all().delete()
        Phase.objects.all().delete()
        Group.objects.all().delete()
        Voucher.objects.all().delete()
        Timer.objects.all().delete()
        Distribution.objects.all().delete()
        User.objects.all().delete()
        print("**********************")
        print("tearDown --- DELETED")
        print("**********************")

    def test_shedding0(self):
        # from .functions import shedding
        print("__________before shedding___________________")
        auction, treatment = Auction.cache_or_create_auction()

        print("")
        print("")

        player_list_selected = Player.objects.filter(selected=True).count()
        player_list_nselected = Player.objects.filter(selected=False).count()



        auction=auction.strongest_together(treatment)
        Player.refresh_all_players()

        print("__________after shedding___________________")

        player_list = Player.objects.all().select_related('group').order_by("group_id", "id")
        # for player in player_list:
        #     print("player:", player, " group:", player.group.idd, " id:", player.id, " error:", player.testing_errors,
        #           " selected:", player.selected)

        player_list_selected = Player.objects.filter(selected=True).count()
        player_list_nselected = Player.objects.filter(selected=False).count()

        # print("player_list_selected", player_list_selected)
        # print("player_list_nselected", player_list_nselected)

        self.assertTrue(player_list_selected,16)
        self.assertTrue(player_list_nselected,8)
        # self.assertFalse(False < True)
        group_list = Group.objects.all()
        for group in group_list:
            player_list_selected_gPR = Player.objects.filter(selected=True,group=group,role=Player.PR).count()
            player_list_selected_gRE = Player.objects.filter(selected=True, group=group, role=Player.RE).count()
            self.assertTrue(player_list_selected_gPR, 4)
            self.assertTrue(player_list_selected_gRE, 4)

        # self.assertTrue(False)