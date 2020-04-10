# # import json
# from django.core.cache import cache
# from django.test import TestCase, RequestFactory, Client
# from forward_and_spot.models import Offer, Auction, Player, Group, Player_stats, Period, Phase, Timer, Voucher,Treatment
# from dAuction2.models import User,  Experiment
# from forward_and_spot.test_views_set_offer import delete_all, function_in_FS_views_with_auction_setup
# # from master.functions_main import cache_me, invalidate_caches, authenticate
# from payout.views import main
#
# # import time
#
# # from django.http import *
# import random
# from distribution.models import  Distribution
# from master.models import MasterMan
#
# class test_payout(TestCase):
#     def setUp(self):
#         self.tearDown()
#         MasterMan.invalidate_caches()
#         Player_stats.objects.all().delete()
#         Player.objects.all().delete()
#         random.seed(1)
#         print("**********************")
#         print("setUp")
#         print("**********************")
#         print(Phase.objects.all())
#         print(Period.objects.all())
#         print(Auction.objects.all())
#         print(Group.objects.all())
#         print("**********************")
#         MasterMan.invalidate_caches()
#         self.factory = RequestFactory()
#         # auction = Auction.objects.get_or_create(pk=1)[0]
#
#         experiment = Experiment.objects.get_or_create()[0]
#         experiment.save()
#         treatment = Treatment.objects.get_or_create(experiment=experiment)[0]
#         treatment.qp_every=2
#
#         treatment.total_periods=9
#         treatment.PR_per_group = 4
#         treatment.RE_per_group = 4
#         treatment.total_groups = 2
#         treatment.save_and_cache()
#
#         # cache.set('treatment',treatment)

#         # auction_init(auction,treatment)
#         auction.started = True
#         auction.app = Auction.PAYOUT
#         print("auction.app = Auction.PAYOUT",auction.app)
#         auction.auction_started = True
#         auction.save_and_cache()
#
#         # cache.set('auction',auction)
#         # auction=auction.createVoucher(treatment)
#
#         group = Group.objects.get_or_create(idd=1, auction=auction)[0]
#         group.save()
#         print("group", group)
#         print("Group.objects.all()", Group.objects.filter(auction=auction).all())
#
#         group2 = Group.objects.get_or_create(idd=2, auction=auction)[0]
#         group.save()
#         print("group", group)
#         print("Group.objects.all()", Group.objects.all())
#
#         group_list = Group.objects.filter(auction=auction).all()
#
#         for group in group_list:
#             for role in range(0,2):
#                 user = User.objects.create(username=str(group)+"p0"+ "role{}".format(role))
#                 player = Player.objects.create(user=user, role=role, auction=auction, group=group)
#                 player.save()
#                 user.has_player = True
#                 user.save()
#
#                 user = User.objects.create(username=str(group) + "p1"+ "role{}".format(role))
#                 player = Player.objects.create(user=user, role=role, auction=auction, group=group)
#                 player.save()
#                 user.has_player = True
#                 user.save()
#
#                 user = User.objects.create(username=str(group) + "p2"+ "role{}".format(role))
#                 player = Player.objects.create(user=user, role=role, auction=auction, group=group)
#                 player.save()
#                 user.has_player = True
#                 user.save()
#
#                 user2 = User.objects.create(username=str(group)+"f0"+ "role{}".format(role))
#                 player2 = Player.objects.create(user=user2, role=role, auction=auction, group=group)
#                 player2.save()
#                 user2.has_player = True
#                 user2.save()
#         auction = Distribution.demand_draws_create(auction, treatment)
#         Player_stats.playerStats_create(auction, treatment)
#         player_list = Player.objects.filter(auction=auction).all()
#         print("treatment.qp_every:{}".format(treatment.qp_every))
#         for player in player_list:
#             player_stats_list = Player_stats.objects.filter(auction=auction,player=player).select_related('player', 'player__user').all().order_by('period')
#             for player_stats in player_stats_list:
#                 period = player_stats.period
#                 player_stats.profit = player_stats.period.idd * 10000 + player_stats.player_id * 100000 + player.group.idd * 10000000
#                 player_stats.profit_accuracy = player_stats.period.idd + player_stats.player_id * 10 + player.group.idd * 1000
#                 player_stats.save()
#                 if player.pay_period == period.idd:
#                     player.payout_trade = player_stats.profit
#                     print("player.payout_qs:{}".format(player.payout_qs))
#                     player.save()
#                 if player.pay_qs_period == period.idd:
#                     print("player.payout_qs:{} before".format(player.payout_qs))
#                     player.payout_qs = player_stats.profit_accuracy
#
#                     # print("player_stats.period.idd:{}".format(player_stats.period.idd))
#                     # print("player.payout_qs:{}".format(player.payout_qs))
#                     # print("player.group.idd:{}".format(player.group.idd))
#                     # print("player.id:{}".format(player.id))
#                     # print("player.user.id.id:{}".format(player.user.id))
#                     print("player.payout_qs:{}".format(player.payout_qs))
#                     player.save()
#
#
#         # auction_ready(auction)
#
#         print("treatment.total_periods", treatment.total_periods)
#
#         print("**********************")
#         print("end setUp")
#         print("**********************")
#
#     def tearDown(self):
#         # Clean up run after every test method.
#         delete_all(self)
#         # MasterMan.invalidate_caches()
#         # Offer.objects.all().delete()
#         # # cache.set("all_offers", "")
#         # Player.objects.all().delete()
#         # # cache.set("player_list","")
#         # Player_stats.objects.all().delete()
#         # # cache.set("all_player_stats","")
#         # Auction.objects.all().delete()
#         # # cache.set("auction", "")
#         # Period.objects.all().delete()
#         # # cache.set("period", "")
#         # Phase.objects.all().delete()
#         # # cache.set("phase", "")
#         # Group.objects.all().delete()
#         # # cache.set("group", "")
#         # # cache.set("group_list", "")
#         # Voucher.objects.all().delete()
#         # # cache.set('voucher_list','')
#         # # cache.set('vouchers_ser', '')
#         # Timer.objects.all().delete()
#         #
#         # Distribution.objects.all().delete()
#         # User.objects.all().delete()
#         print("**********************")
#         print("tearDown --- DELETED")
#         print("**********************")
#
#     def test_payout0(self):
#         # self.tearDown()
#         # MasterMan.invalidate_caches()
#         # Player_stats.objects.all().delete()
#         # Player.objects.all().delete()
#         # self.setUp()
#         # random.seed(1)
#         # auction = Auction.objects.get_or_create(pk=1)[0]
#         # treatment = Treatment.objects.last()
#         #
#         # auction = Auction.objects.get_or_create(treatment=treatment)[0]
#
#         # print("key_from_instance(auction)",key_from_instance(auction))
#         auction, treatment = Auction.cache_or_create_auction()
#         print("auction.app",auction.app)
#         print("auction.PAYOUT", auction.PAYOUT)
#         # dac(auction)
#
#         period = Period.objects.get(idd=1, auction=auction)
#         period.save()
#         # print("key_from_instance(period)", key_from_instance(period))
#         print("period", period)
#         print("period.id", period.id)
#         phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
#         phase.save_and_cache()
#         # MasterMan.cache_me('phase', phase)
#         # cache.set('phase', phase)
#         # print("key_from_instance(phase)", key_from_instance(phase))
#         print("phase.question_page", phase.question_page)
#
#         # auction = Auction.objects.get_or_create()[0]
#
#         # auction_id=auction.id
#         # group = Group.objects.get_or_create(idd=1, auction=auction)[0]
#         # group.save()
#         # group_id = group.id
#         group = Group.objects.get(idd=1, auction=auction)
#         group2 = Group.objects.get(idd=2, auction=auction)
#         user0 = User.objects.get(username=str(group)+"p0"+"role{}".format(0))
#         # user1 = User.objects.get(username=str(group2) + "p1")
#         # user_id=user.id
#
#         tt = Timer.objects.get_or_create(pk=1)[0]
#         # print("tt.end_time",tt.end_time)
#         # print("response:",response)
#         # print("response.content:", response.content)
#         # response_content=response.content
#         from django.shortcuts import render_to_response, redirect
#         # return redirect('payout-main')
#         data={}
#
#
#         period_list = Period.objects.filter(auction=auction).all()
#         player_list = Player.objects.filter(auction=auction).select_related('user').all()
#         for player in player_list:
#             for period in period_list:
#                 ps = player.player_stats_set.get(period=period)
#                 print("player:{}, ps.period: {}, ps.profit:{} , ps.profit_accuracy:{}".format(player, ps.period, ps.profit, ps.profit_accuracy))
#                 if period.idd<7:
#                     period.finished=True
#                     period.save()
#
#         for player in player_list:
#             print("player:{}, pay_period:{}, pay_qs_period:{},  player.payout_ECU:{}, payout_CZK:{}, payout_qs:{}, payout_trade:{}".format(player, player.pay_period,player.pay_qs_period, player.payout_ECU, player.payout_CZK,player.payout_qs,player.payout_trade))
#             self.assertEqual(player.payout_CZK, 0)
#             self.assertEqual(player.payout_ECU, 0)
#         # self.assertEqual(player.payout_qs, 2165)
#         # self.assertEqual(player.payout_trade,21630000)
#
#
#         self.factory = RequestFactory()
#         request = self.factory.post('/', data)
#         request.user = user0
#         player=Player.objects.get(user=user0)
#         # player id 1 has pay_period 6 and pay_qs_period 3, both periods have been played, so no problems
#         player.app = Player.PAYOUT
#         player.save()
#         # doesnt work somehow:
#         response= main(request)
#         data = cache.get('context')
#         print("data:{}".format(data))
#         print("response",response)
#         print("response", response.content)
#         if "10160000" in str(response.content):
#             print("10160000 in response.content")
#         # self.assertIn("You therefore earned ECU 2593",str(response.content))
#         # self.assertIn("per CZK this is worth CZK 51905186",
#         #     str(response.content))
#         print("response.status_code:{}".format(response.status_code))
#
#
#         # print("rss:{}".format(rss))
#         # print((player.payout_qs+player.payout_trade)/treatment.ECU_per_CZK_PR)
#         # print("response.context:{}".format(response.context))
#         #
#         # self.assertEqual(rss,(player.payout_qs+player.payout_trade)/treatment.ECU_per_CZK_PR)
#        # content print("json_data ", response.lists() )
#
#         # player = Player.objects.filter(auction=auction, pay_period=9,pay_qs_period=5).first()
#         # # player id 6 has pay_period 8 and pay_qs_peiod 5, pay_period 8 has thus not been played and a new one must be chosen
#         # player.app = Player.PAYOUT
#         # player.save()
#         # user1=player.user
#         # self.factory = RequestFactory()
#         # request = self.factory.post('/', data)
#         # request.user = user1
#         #
#         # period=Period.objects.get(idd=8)
#         # print("period.finished:{}".format(period.finished))
#         #
#         # # doesnt work somehow:
#         # response = main(request)  #here a problem occurs
#         # print("response", response.content)
#         #
#         # self.assertIn("The period number 7 was chosen", str(response.content))
#         # # self.assertIn("You earned ECU 36350000", str(response.content))
#
#         # player = Player.objects.filter(auction=auction, pay_period=6,pay_qs_period=9).first()
#         #     # .get(auction=auction, id=7)
#         # # player id 7 has pay_period 6 and pay_qs_period 9, pay_qs_period 9 has thus not been played and a new one must be chosen
#         # player.app = Player.PAYOUT
#         # player.save()
#         # user1 = player.user
#         # self.factory = RequestFactory()
#         # request = self.factory.post('/', data)
#         # request.user = user1
#         #
#         # period = Period.objects.get(idd=8)
#         # print("period.finished:{}".format(period.finished))
#         #
#         # # doesnt work somehow:
#         # response = main(request)
#         # print("response", response.content)
#         # self.assertIn("The period number 6 was chosen", str(response.content))
#         # # self.assertIn("The period number 5 was chosen", str(response.content))
#         # # self.assertIn("You earned ECU 22960000 in this period", str(response.content))
#         # # self.assertIn("You therefore earned ECU 2295", str(response.content))
#         #
#         # player = Player.objects.filter(auction=auction, pay_period__gt=4,pay_qs_period__gt=4).first()
#         # print("player:{}".format(player))
#         # player_list=Player.objects.filter(auction=auction).all()
#         # print("player_list:{}".format(player_list))
#         # player_list2 = Player.objects.filter(auction=auction, pay_period__gt=4, pay_qs_period__gt=4).all()
#         # print("player_list2:{}".format(player_list2))
#         # # get(auction=auction, id=10)
#         # # player id 10 has pay_period 8 and pay_qs_peiod 7, pay_period 8 and pay_qs_period 7 have thus not been played and new ones must be chosen
#         # Period.objects.filter(idd__gt=4).update(finished=False)
#         # player.app = Player.PAYOUT
#         # player.save()
#         # user1 = player.user
#         # self.factory = RequestFactory()
#         # request = self.factory.post('/', data)
#         # request.user = user1
#         #
#         # period = Period.objects.get(idd=8)
#         # print("period.finished:{}".format(period.finished))
#         #
#         # # doesnt work somehow:
#         # response = main(request)
#         # print("response", response.content)
#         # # self.assertIn("The period number 3 was chosen", str(response.content))
#         # # self.assertIn("You earned ECU 12210000", str(response.content))
#         # #
#         # # self.assertIn("The period number 1 was chosen", str(response.content))
#         # # self.assertIn("You therefore earned ECU 1221", str(response.content))
#         #
#         #
#         #
#         # # self.assertTrue(False)
#
#
