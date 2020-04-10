import json
from django.core.cache import cache
from django.test import TestCase, RequestFactory, TransactionTestCase
from forward_and_spot.models import Offer, Auction, Player, Group, Player_stats, Period, Phase, Timer, Treatment
from distribution.models import  Distribution
from dAuction2.models import Experiment
from dAuction2.models import User
from master.models import MasterMan
from .master_api import ajax_admin
# from master.functions_main import  cache_me, invalidate_caches
import logging
from master.models import MasterMan
from forward_and_spot.test_views_set_offer import function_in_FS_views_with_auction_setup, delete_all

# logger = logging.getLogger(__name__)
log = logging.getLogger(__name__)
import time

from django.http import *


class test_ajax_admin(TransactionTestCase):
    def setUp(self):
        print("**********************")
        print("setUp")
        print("**********************")
        print(Phase.objects.all())
        print(Period.objects.all())
        print(Auction.objects.all())
        print(Group.objects.all())
        print("**********************")
        delete_all(self)
        function_in_FS_views_with_auction_setup.setUp(self)

        # MasterMan.invalidate_caches()
        self.factory = RequestFactory()
        # treatment = Treatment.cache_or_create_treatment()
        # auction = Auction.create(treatment)
        auction, treatment = Auction.cache_or_create_auction()
        auction.started = True
        auction.app = Auction.FS
        auction.auction_started = True
        # auction.PR_per_group = 1
        auction.save()
        # # auction=Voucher.createVoucher(auction, treatment)
        #
        # group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        # group.save()
        # print("group:{}".format( group))
        # print("Group.objects.all():{}".format( Group.objects.all()))
        #
        # group2 = Group.objects.get_or_create(idd=2, auction=auction)[0]
        # group.save()
        # print("group", group)
        # print("Group.objects.all()", Group.objects.all())
        #
        # group_list = Group.objects.filter(auction=auction).all()
        # for group in group_list:
        #
        #     user = User.objects.create(username=str(group)+"p")
        #     player = Player.objects.create(user=user, role=1, auction=auction, group=group)
        #     player.save()
        #     user.has_player = True
        #     user.save()
        #
        #     user = User.objects.create(username=str(group) + "p2")
        #     player = Player.objects.create(user=user, role=0, auction=auction, group=group)
        #     player.save()
        #     user.has_player = True
        #     user.save()
        #
        #     user2 = User.objects.create(username=str(group)+"f")
        #     player2 = Player.objects.create(user=user2, role=0, auction=auction, group=group)
        #     player2.save()
        #     user2.has_player = True
        #     user2.save()
        #
        # auction = Distribution.demand_draws_create(auction, treatment)
        # Player_stats.playerStats_create(auction, treatment)
        # auction = auction.auction_ready( treatment)
        # auction.save_and_cache()
        # tt = Timer.cache_get()
        # if not tt:
        #     tt = Timer.objects.get_or_create(pk=1)[0]
        # tt = tt.timer_set(time_length=treatment.time_for_question_page, short_time_length=None)
        # tt.cache_me()
        # # state = Player.WAITv
        # Player.refresh_all_players()
        # print("treatment.total_periods", treatment.total_periods)

        print("**********************")
        print("end setUp")
        print("**********************")

    def tearDown(self):
        delete_all(self)
        # Clean up run after every test method.
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

    # def test_ajax_admin0(self):
    #
    #     print("__________ test_ajax_admin0")
    #     # treatment = Treatment.cache_or_create_treatment()
    #     auction, treatment = Auction.cache_or_create_auction()
    #     treatment.qp_every = 1
    #     treatment.active=True
    #     treatment.save_and_cache()
    #     # treatment.cache_me()
    #
    #     # auction = Auction.objects.get_or_create(treatment=treatment)[0]
    #     # auction.save_and_cache()
    #     # auction.cache_me('auction',auction)
    #     period = Period.objects.get(idd=1, auction=auction)
    #     period.save()
    #     print("period", period)
    #     print("period.id", period.id)
    #     phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
    #     phase.save_and_cache()
    #     # MasterMan.cache_me('phase', phase)
    #     # cache.set('phase', phase)
    #     # print("key_from_instance(phase)", key_from_instance(phase))
    #     print("phase.question_page", phase.question_page)
    #
    #     # auction = Auction.objects.get_or_create()[0]
    #     
    #     # auction_id=auction.id
    #     # group = Group.objects.get_or_create(idd=1, auction=auction)[0]
    #     # group.save()
    #     # group_id = group.id
    #     group = Group.objects.get(idd=1, auction=auction)
    #     group2 = Group.objects.get(idd=2, auction=auction)
    #     user_list = User.objects.all()
    #     user1p = user_list.last()
    #         # User.objects.get(pk=1)
    #     user2p = user_list.first()
    #         # User.objects.get(pk=2)
    #     # user_id=user.id
    #     request = self.factory.get('/')
    #     request.user = user1p
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     # print("tt.end_time",tt.end_time)
    #     # print("response:",response)
    #     # print("response.content:", response.content)
    #     # response_content=response.content
    #
    #
    #     player_list = Player.objects.filter(auction=auction)
    #     for p in player_list:
    #         print ("pl_:{}, id:{} ,user:{}".format(p,p.id, p.user))
    #     player1p = Player.objects.get(auction=auction, user=user1p)
    #     player2p = Player.objects.get(auction=auction, user=user2p)
    #     # period = Period.objects.get_or_create(idd=1, auction=auction)[0]
    #     # period.save()
    #     # phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1, nothing=True)[0]
    #     # phase.save()
    #     # cache.set('phase', phase)
    #     # phase = Phase.objects.get(auction=auction,period=period)
    #     phase = Phase.objects.get(auction=auction,period=period)
    #     print("phase.question_page", phase.question_page)
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() + 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data:", json_data['cache_duration'])
    #     phase = Phase.objects.get(auction=auction,period=period)
    #     print("phase.question_page", phase.question_page)
    #
    #     auction_ser_data = cache.get("auction_ser_data")
    #     print("auction_ser_data", auction_ser_data)
    #     # response = self.client.get('/', {'instrument': 'drums'})
    #     # req = json.loads(request.body.decode('utf-8'))
    #     # json_data = json.loads(request.read().decode('utf-8'))
    #     # data = json.loads(response.body)
    #     # print("data",data)
    #     period = Period.objects.get_or_create(idd=1, auction=auction)[0]
    #     playerstats1p = Player_stats.objects.get(player=player1p, auction=auction, period=period)
    #     print(playerstats1p)
    #     print(playerstats1p.penalty_phase_total)
    #     self.assertEqual(response.status_code, 200)
    #     print("json_data['phase']", json_data['phase'])
    #     print("json_data['period']", json_data['period'])
    #
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], True)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], True)
    #     print("")
    #     print("SUCCESS 1")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() + 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #
    #     playerstats = Player_stats.objects.get(player=player1p, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], True)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], True)
    #     print("")
    #     print("SUCCESS 2")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player1p, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     self.assertEqual(json_data['phase']['active_state'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], False)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("")
    #     print("SUCCESS 3")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player1p, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], False)
    #     self.assertEqual(json_data['phase']['active_state'], 2)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("")
    #     print("SUCCESS 4")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player1p, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     self.assertEqual(json_data['phase']['active_state'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], False)
    #     self.assertEqual(json_data['phase']['waiting_page'], True)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("")
    #     print("SUCCESS 5")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player1p, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 2)
    #     self.assertEqual(json_data['phase']['active_state'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], False)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("")
    #     print("SUCCESS 6")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player1p, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 2)
    #     self.assertEqual(json_data['phase']['active_state'], 2)
    #     # self.assertEqual(json_data['phase']['nothing'], False)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("")
    #     print("SUCCESS 7")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player1p, auction=auction, period=period)
    #     print("playerstats:{}".format(playerstats))
    #     print("playerstats.penalty_phase_total:{}".format(playerstats.penalty_phase_total))
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 2)
    #     self.assertEqual(json_data['phase']['active_state'], 3)
    #     # self.assertEqual(json_data['phase']['nothing'], True)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("")
    #     print("SUCCESS 8")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player1p, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 2)
    #     self.assertEqual(json_data['phase']['active_state'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], False)
    #     self.assertEqual(json_data['phase']['waiting_page'], True)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("")
    #     print("SUCCESS 9")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player1p, auction=auction, period=period)
    #
    #     print("playerstats:{}".format(playerstats))
    #     print("playerstats.penalty_phase_total:{}".format(playerstats.penalty_phase_total))
    #     print("treatment.total_periods:{}".format(treatment.total_periods))
    #     self.assertEqual(json_data['period']['idd'], 2)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     self.assertEqual(json_data['phase']['active_state'], 1)
    #
    #
    #
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     print("treatment:{}".format(treatment))
    #     print("treatment.qp_every:{}".format(treatment.qp_every))
    #
    #     # why not True?
    #     self.assertEqual(json_data['phase']['question_page'], True)
    #     print("")
    #     print("SUCCESS 10")
    #     print("")
    #
    #     print("treatment.total_periods", treatment.total_periods)
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     # units_soldbyPR_agg = Player_stats.objects.filter(auction=auction, group=group, period=period, role=Player.PR).aggregate(Sum('vouchers_used'))['vouchers_used__sum']
    #
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     print("json_data['period']", json_data['period'])
    #     print("json_data['period']['idd']", json_data['period']['idd'])
    #     period = Period.objects.filter(idd=json_data['period']['idd'])
    #     playerstats = Player_stats.objects.get(player=player1p, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 2)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #
    #     # why not 1?
    #     self.assertEqual(json_data['phase']['active_state'], 1)
    #
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("")
    #     print("SUCCESS 11")
    #     print("")
    #     print("+++__________________________________________+++")

    # def test_ajax_admin1(self):
    #     # treatment = Treatment.cache_or_create_treatment()
    #     auction, treatment = Auction.cache_or_create_auction()
    #     # treatment.qp_every = 1
    #
    #     
    #     # auction = Auction.objects.get_or_create(treatment=treatment)[0]
    #     # auction.save_and_cache()
    #     # MasterMan.cache_me('auction', auction)
    #
    #     auction = Distribution.demand_draws_create(auction, treatment)
    #     auction = auction.auction_ready( treatment)
    #     auction.save_and_cache()
    #     tt = Timer.cache_get()
    #     if not tt:
    #         tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt = tt.timer_set(time_length=treatment.time_for_question_page, short_time_length=None)
    #     tt.cache_me()
    #     # state = Player.WAITv
    #     Player.refresh_all_players()
    #
    #     # auction = Auction.objects.get_or_create()[0]
    #     
    #     # auction_id=auction.id
    #     # group = Group.objects.get_or_create(idd=1, auction=auction)[0]
    #     # group.save()
    #     # group_id = group.id
    #     group = Group.objects.get(idd=1, auction=auction)
    #     # user = User.objects.get(username=str(group) + "p")
    #
    #     user_list = User.objects.all()
    #     # user1p = user_list.last()
    #     # User.objects.get(pk=1)
    #     user = user_list.first()
    #
    #     # user = User.objects.get(pk=1)
    #     # user2p = User.objects.get(pk=2)
    #     # user = User.objects.get_or_create(pk=1)[0]
    #     # user_id=user.id
    #     request = self.factory.get('/')
    #     request.user = user
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     # print("tt.end_time",tt.end_time)
    #     # print("response:",response)
    #     # print("response.content:", response.content)
    #     # response_content=response.content
    #     # auction = Auction.objects.get_or_create(pk=1)[0]
    #     player = Player.objects.get(auction=auction, user=user)
    #     # period = Period.objects.get_or_create(idd=1, auction=auction)[0]
    #     # period.save()
    #     # phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1, nothing=True)[0]
    #     # phase.save()
    #     # cache.set('phase', phase)
    #     Player_stats.playerStats_create(auction, treatment)
    #
    #     phase = Phase.objects.get(auction=auction)
    #     print("phase.question_page", phase.question_page)
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() + 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['cache_duration']:", json_data['cache_duration'])
    #     phase = Phase.objects.get(auction=auction)
    #     print("phase.question_page", phase.question_page)
    #
    #     auction_ser_data = cache.get("auction_ser_data")
    #     print("auction_ser_data", auction_ser_data)
    #     # response = self.client.get('/', {'instrument': 'drums'})
    #     # req = json.loads(request.body.decode('utf-8'))
    #     # json_data = json.loads(request.read().decode('utf-8'))
    #     # data = json.loads(response.body)
    #     # print("data",data)
    #     period = Period.objects.get_or_create(idd=1, auction=auction)[0]
    #     playerstats = Player_stats.objects.get(player=player, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(response.status_code, 200)
    #     print("json_data['phase']", json_data['phase'])
    #     print("json_data['period']", json_data['period'])
    #
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], True)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], True)
    #     print("")
    #     print("SUCCESS 1")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() + 999)
    #     tt.save()
    #     tt.cache_me()
    #     # cache.set('tt', tt)
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #
    #     playerstats = Player_stats.objects.get(player=player, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], True)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], True)
    #     print("")
    #     print("SUCCESS 2")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     tt.cache_me()
    #     # cache.set('tt', tt)
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     self.assertEqual(json_data['phase']['active_state'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], False)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("")
    #     print("SUCCESS 3")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     tt.cache_me()
    #     # cache.set('tt', tt)
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], False)
    #     self.assertEqual(json_data['phase']['active_state'], 2)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("")
    #     print("SUCCESS 4")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     self.assertEqual(json_data['phase']['active_state'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], False)
    #     self.assertEqual(json_data['phase']['waiting_page'], True)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("")
    #     print("SUCCESS 5")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     group_list = Group.objects.all()
    #     print("group_list", group_list)
    #     print(Player.objects.all())
    #     print("Player_stats.objects.all()", Player_stats.objects.all())
    #     for group in group_list:
    #         print("Player_stats.objects.filter(auction=auction, group=group, period=period,role=Player.RE)",
    #               Player_stats.objects.filter(auction=auction, group=group, period=period, role=Player.RE))
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player, auction=auction, period=period)
    #     print(playerstats)
    #     print("playerstats.player_demand", playerstats.player_demand)
    #     print("player.role", player.role)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 2)
    #     self.assertEqual(json_data['phase']['active_state'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], False)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     print("json_data['period']", json_data['period'])
    #     playerstats = Player_stats.objects.get(player=player, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #
    #     period = Period.objects.get(idd=json_data['period']['idd'])
    #
    #     print("period", period)
    #     print("period.id", period.id)
    #     # print("period.total_demand", period.total_demand)
    #
    #     period_list = Period.objects.all()
    #     print("period_list", period_list)
    #
    #     print("")
    #     print("SUCCESS 6")
    #     print("")

    # def test_ajax_admin2(self):
    #
    #     print("__________ajax_admin")
    #     auction, treatment = Auction.cache_or_create_auction()
    #     # treatment_list = Treatment.objects.all()
    #     # for treatment in treatment_list:
    #     #     print("treatment:{}".format(treatment))
    #     # auction = Auction.objects.all().last()
    #     # treatment = auction.treatment
    #     # print("auction: {}".format(auction))
    #     # demand_draws_create(auction)
    #     # auction_ready(auction)
    #     group_list = Group.objects.all()
    #     print("group_list:{}".format(group_list ))
    #     for group in group_list:
    #         print("group:{} - auction:{}".format(group,auction))
    #     group = Group.objects.get_or_create(idd=1, auction=auction)[0]
    #     # group.save()
    #     user3 = User.objects.get_or_create( username="f2")[0]
    #     player = Player.objects.get_or_create(user=user3, role=0, auction=auction, group=group)[0]
    #     player.save()
    #     user3.has_player = True
    #     user3.save()
    #     auction.RE_per_group = 1
    #     auction.PR_per_group = 2
    #     auction.save()
    #
    #     # demand_draws_create(auction)
    #
    #     # auction = Auction.objects.get_or_create()[0]
    #     
    #     # auction_id=auction.id
    #     # group = Group.objects.get_or_create(idd=1, auction=auction)[0]
    #     # group.save()
    #     # group_id = group.id
    #     group = Group.objects.get(idd=1, auction=auction)
    #     user = User.objects.get_or_create(username=str(group) + "p")[0]
    #
    #     # user = User.objects.get_or_create(pk=1)[0]
    #     # user_id=user.id
    #     request = self.factory.get('/')
    #     request.user = user
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     # print("tt.end_time",tt.end_time)
    #     # print("response:",response)
    #     # print("response.content:", response.content)
    #     # response_content=response.content
    #     # auction = Auction.objects.get_or_create(pk=1)[0]
    #     player = Player.objects.get_or_create(auction=auction, user=user, group=group)[0]
    #     # period = Period.objects.get_or_create(idd=1, auction=auction)[0]
    #     # period.save()
    #     # phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1, nothing=True)[0]
    #     # phase.save()
    #     # cache.set('phase', phase)
    #     print("1")
    #     period_list = Period.objects.all()
    #     for period in period_list:
    #         print("period:{} period.auction:{}".format(period, period.auction))
    #     period = Period.objects.get(idd=1,auction=auction)
    #     phase = Phase.objects.get_or_create(auction=auction,period=period)[0]
    #     print("phase.question_page", phase.question_page)
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() + 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data:", json_data['cache_duration'])
    #     phase = Phase.objects.get(auction=auction)
    #     print("phase.question_page", phase.question_page)
    #
    #     auction_ser_data = cache.get("auction_ser_data")
    #     print("auction_ser_data", auction_ser_data)
    #     period_list = Period.objects.all()
    #     print("here problem with dupl period?")
    #
    #     print("2")
    #     for period in period_list:
    #         print("period:{} period.auction:{}".format(period,period.auction))
    #
    #     playerstats = Player_stats(player=player, auction=auction, group=group, period=period)
    #
    #     print("xxx")
    #     period_list = Period.objects.all()
    #     for period in period_list:
    #         print("period:{} period.auction:{}".format(period, period.auction))
    #
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(response.status_code, 200)
    #     print ("json_data:{}".format(json_data))
    #     print("json_data['phase']", json_data['phase'])
    #     print("json_data['period']", json_data['period'])
    #
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], True)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], True)
    #     print("")
    #     print("SUCCESS 1")
    #     print("")
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() + 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     # print("xxx")
    #     # period_list = Period.objects.all()
    #     # for period in period_list:
    #     #     print("period:{}".format(period))
    #
    #
    #     response = ajax_admin(request)
    #
    #     json_data = json.loads(response.content.decode())
    #
    #     print("xxx")
    #     period_list = Period.objects.all()
    #     for period in period_list:
    #         print("period:{}".format(period))
    #
    #     playerstats = Player_stats(player=player, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], True)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], True)
    #     print("")
    #     print("SUCCESS 2")
    #     print("")
    #
    #     print("xxx")
    #     period_list = Period.objects.all()
    #     for period in period_list:
    #         print("period:{}".format(period))
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     self.assertEqual(json_data['phase']['active_state'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], False)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("")
    #     print("SUCCESS 3")
    #     print("")
    #
    #     print("2a")
    #     period_list = Period.objects.all()
    #     for period in period_list:
    #         print("period:{}".format(period))
    #
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     self.assertEqual(json_data['phase']['active_state'], 2)
    #     # self.assertEqual(json_data['phase']['nothing'], False)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("")
    #     print("SUCCESS 4")
    #     print("")
    #
    #     print("2b")
    #     period_list = Period.objects.all()
    #     for period in period_list:
    #         print("period:{}".format(period))
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #
    #     print("2c")
    #     period_list = Period.objects.all()
    #     for period in period_list:
    #         print("period:{}".format(period))
    #
    #     json_data = json.loads(response.content.decode())
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 1)
    #     self.assertEqual(json_data['phase']['active_state'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], False)
    #     self.assertEqual(json_data['phase']['waiting_page'], True)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("")
    #     print("SUCCESS 5")
    #     print("")
    #
    #     print("3")
    #     period_list = Period.objects.all()
    #     for period in period_list:
    #         print("period:{}".format(period))
    #
    #     tt = Timer.objects.get_or_create(pk=1)[0]
    #     tt.end_time = int(time.time() - 999)
    #     tt.save()
    #     group_list = Group.objects.all()
    #     print("group_list", group_list)
    #     print(Player.objects.all())
    #     print("Player_stats.objects.all()", Player_stats.objects.all())
    #     for group in group_list:
    #         print("Player_stats.objects.filter(auction=auction, group=group, period=period,role=Player.RE)",
    #               Player_stats.objects.filter(auction=auction, group=group, period=period, role=Player.RE))
    #     # cache.set('tt', tt)
    #     tt.cache_me()
    #     response = ajax_admin(request)
    #     json_data = json.loads(response.content.decode())
    #
    #     print("4")
    #     period_list = Period.objects.all()
    #     for period in period_list:
    #         print("period:{}".format(period))
    #
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     playerstats = Player_stats.objects.get(player=player, auction=auction, period=period)
    #     print(playerstats)
    #     print("playerstats.player_demand", playerstats.player_demand)
    #     print("player.role", player.role)
    #     print(playerstats.penalty_phase_total)
    #     self.assertEqual(json_data['period']['idd'], 1)
    #     self.assertEqual(json_data['phase']['idd'], 2)
    #     self.assertEqual(json_data['phase']['active_state'], 1)
    #     # self.assertEqual(json_data['phase']['nothing'], False)
    #     self.assertEqual(json_data['phase']['waiting_page'], False)
    #     self.assertEqual(json_data['phase']['question_page'], False)
    #     print("json_data:", json_data)
    #     print("json_data['phase']", json_data['phase'])
    #     print("json_data['period']", json_data['period'])
    #     print("5")
    #     period_list = Period.objects.all()
    #     for perioda in period_list:
    #         print("period:{}".format(perioda))
    #
    #     playerstats = Player_stats.objects.get(player=player, auction=auction, period=period)
    #     print(playerstats)
    #     print(playerstats.penalty_phase_total)
    #
    #     period_list = Period.objects.all()
    #     for perioda in period_list:
    #         print("period:{}".format(perioda))
    #
    #     period = Period.objects.get(idd=json_data['period']['idd'])
    #
    #     print("period", period)
    #     print("period.id", period.id)
    #     # print("period.total_demand", period.total_demand)
    #
    #     period_list = Period.objects.all()
    #     print("period_list", period_list)
    #
    #     print("")
    #     print("SUCCESS 6")
    #     print("")
    #
    #     # self.assertTrue(False<True)
    #     # self.assertFalse(False < True)

