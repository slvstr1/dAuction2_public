import json
from django.core.cache import cache
from django.test import TestCase, RequestFactory
from forward_and_spot.models import Offer, Auction, Player, Group, Player_stats, Period, Phase, Timer, Treatment
from distribution.models import Distribution
from dAuction2.models import Experiment
from dAuction2.models import User
from .master_api import ajax_admin
# from master.functions_main import cache_me, invalidate_caches
import time
import logging
from master.models import MasterMan
from forward_and_spot.test_views_set_offer import delete_all, function_in_FS_views_with_auction_setup

# logger = logging.getLogger(__name__)
log = logging.getLogger(__name__)
from django.http import *


class test_qp(TestCase):
    def setUp(self):
        print("**********************")
        print("setUp")
        print("**********************")
        print(Phase.objects.all())
        print(Period.objects.all())
        print(Auction.objects.all())
        print(Group.objects.all())
        print("**********************")
        MasterMan.invalidate_caches()
        delete_all(self)
        self.factory = RequestFactory()

        # treatment=Treatment.cache_or_create_treatment()
        # auction = Auction.create(treatment)
        auction, treatment = Auction.cache_or_create_auction()
        auction.started = True
        auction.app = Auction.FS
        auction.auction_started = True
        auction.PR_per_group = 1
        auction.save()
        # auction=Voucher.createVoucher(auction, treatment)

        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group.save()
        print("group", group)
        # print("Group.objects.all()", Group.objects.all())

        group2 = Group.objects.get_or_create(idd=2, auction=auction)[0]
        group.save()
        # print("group", group)
        # print("Group.objects.all()", Group.objects.all())

        group_list = Group.objects.all()
        for group in group_list:

            user = User.objects.create(username=str(group)+"p")
            player = Player.objects.create(user=user, role=1, auction=auction, group=group)
            player.save()
            user.has_player = True
            user.save()

            user = User.objects.create(username=str(group) + "p2")
            player = Player.objects.create(user=user, role=0, auction=auction, group=group)
            player.save()
            user.has_player = True
            user.save()

            user2 = User.objects.create(username=str(group)+"f")
            player2 = Player.objects.create(user=user2, role=0, auction=auction, group=group)
            player2.save()
            user2.has_player = True
            user2.save()

        # demand_draws_create(auction, treatment)
        Distribution.demand_draws_create(auction, treatment)
        Player_stats.playerStats_create()
        auction.auction_ready(treatment)
        auction.save_and_cache()
        tt = Timer.cache_get()
        if not tt:
            tt = Timer.objects.get_or_create(pk=1)[0]
        tt = tt.timer_set(time_length=treatment.time_for_question_page, short_time_length=None)
        tt.cache_me()
        # state = Player.WAITv
        Player.refresh_all_players()
        # print("treatment.total_periods", treatment.total_periods)

        print("**********************")
        print("end setUp")
        print("**********************")

    def tearDown(self):
        # Clean up run after every test method.
        delete_all(self)
        # from forward_and_spot.models import Voucher
        # from distribution.models import Distribution
        # MasterMan.invalidate_caches()
        # Offer.objects.all().delete()
        # # cache.set("all_offers", "")
        # Player.objects.all().delete()
        # # cache.set("player_list","")
        # Player_stats.objects.all().delete()
        # # cache.set("all_player_stats","")
        # Auction.objects.all().delete()
        # # cache.set("auction", "")
        # Period.objects.all().delete()
        # # cache.set("period", "")
        # Phase.objects.all().delete()
        # # cache.set("phase", "")
        # Group.objects.all().delete()
        # # cache.set("group", "")
        # # cache.set("group_list", "")
        # Voucher.objects.all().delete()
        # # cache.set('voucher_list','')
        # # cache.set('vouchers_ser', '')
        # Timer.objects.all().delete()
        #
        # Distribution.objects.all().delete()
        # User.objects.all().delete()
        print("**********************")
        print("tearDown --- DELETED")
        print("**********************")

    def test_qp(self):

        print("__________ajax_admin")

        # treatment = Treatment.objects.get(id=1)
        
        # auction = Auction.objects.all().last()
        # treatment=auction.treatment
        
        # print("key_from_instance(auction)",key_from_instance(auction))
        auction, treatment = Auction.cache_or_create_auction()

        # dac(auction)

        print("1")
        period_list = Period.objects.all()
        # for period in period_list:
        #     print("period:{} period.auction:{} period.id:{} period.idd:{}".format(period, period.auction,period.id,period.idd))

        period = Period.objects.get(idd=1, auction=auction)
        period.save()
        # print("key_from_instance(period)", key_from_instance(period))
        # print("period", period)
        # print("period.id", period.id)
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        phase.save_and_cache()
        # phase.cache_me('phase', phase)
        # cache.set('phase', phase)
        # print("key_from_instance(phase)", key_from_instance(phase))
        # print("phase.question_page", phase.question_page)

        # auction = Auction.objects.get_or_create()[0]
        
        # auction_id=auction.id
        # group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        # group.save()
        # group_id = group.id
        group = Group.objects.get(idd=1, auction=auction)
        group2 = Group.objects.get(idd=2, auction=auction)
        user1p = User.objects.get(username=str(group)+"p")
        user2p = User.objects.get(username=str(group2) + "p")
        # user_id=user.id
        request = self.factory.get('/')
        request.user = user1p
        tt = Timer.objects.get_or_create(pk=1)[0]
        # print("tt.end_time",tt.end_time)
        # print("response:",response)
        # print("response.content:", response.content)
        # response_content=response.content



        player1p = Player.objects.get(auction=auction, user=user1p)
        player2p = Player.objects.get(auction=auction, user=user2p)
        # period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        # period.save()
        # phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1, nothing=True)[0]
        # phase.save()
        # cache.set('phase', phase)
        # phase = Phase.objects.get(auction=auction,period=period)
        phase = Phase.objects.get(auction=auction,period=period)
        # print("phase.question_page", phase.question_page)

        tt = Timer.objects.get_or_create(pk=1)[0]
        tt.end_time = int(time.time() + 999)
        tt.save()
        # cache.set('tt', tt)
        tt.cache_me()

        response = ajax_admin(request)
        json_data = json.loads(response.content.decode())
        # print("json_data:", json_data)
        # print("json_data:", json_data['cache_duration'])
        phase = Phase.objects.get(auction=auction,period=period)
        # print("phase.question_page", phase.question_page)

        auction_ser_data = cache.get("auction_ser_data")
        # print("auction_ser_data", auction_ser_data)
        # response = self.client.get('/', {'instrument': 'drums'})
        # req = json.loads(request.body.decode('utf-8'))
        # json_data = json.loads(request.read().decode('utf-8'))
        # data = json.loads(response.body)
        # print("data",data)
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        playerstats1p = Player_stats.objects.get(player=player1p, auction=auction, period=period)
        print(playerstats1p)
        print(playerstats1p.penalty_phase_total)
        self.assertEqual(response.status_code, 200)
        # print("json_data['phase']", json_data['phase'])
        # print("json_data['period']", json_data['period'])

        self.assertEqual(json_data['period']['idd'], 1)
        self.assertEqual(json_data['phase']['idd'], 1)
        # self.assertEqual(json_data['phase']['nothing'], True)
        self.assertEqual(json_data['phase']['waiting_page'], False)
        self.assertEqual(json_data['phase']['question_page'], True)
        print("")
        print("SUCCESS 1")
        print("")

        for i in range(1,9):
            tt = Timer.objects.get_or_create(pk=1)[0]
            tt.end_time = int(time.time() - 999)
            tt.save()
            # cache.set('tt', tt)
            tt.cache_me()
            response = ajax_admin(request)
            json_data = json.loads(response.content.decode())

        playerstats = Player_stats.objects.get(player=player1p, auction=auction, period=period)
        print(playerstats)
        print(playerstats.penalty_phase_total)
        self.assertEqual(json_data['period']['idd'], 2)
        self.assertEqual(json_data['phase']['idd'], 1)
        # self.assertEqual(json_data['phase']['nothing'], True)
        self.assertEqual(json_data['phase']['waiting_page'], False)
        self.assertEqual(json_data['phase']['question_page'], False)
        print("")
