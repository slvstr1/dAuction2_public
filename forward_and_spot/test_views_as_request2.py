from forward_and_spot.models import Treatment
from dAuction2.models import Experiment
from django.test import TestCase, RequestFactory, TransactionTestCase
from forward_and_spot.views import set_offer_nr, set_offer
# from master.functions_main import createVoucher
from forward_and_spot.models import Offer, Auction, Player, Group, Player_stats, Period, Phase, Timer, Voucher
from dAuction2.models import Experiment
from dAuction2.models import User
from .test_views_set_offer import function_in_FS_views_with_auction_setup

# from master.functions_main import  cache_me, invalidate_caches, PlayerStats_create
from payout.views import main
from master.models import MasterMan



class test_set_offer_oneofferonly(TransactionTestCase):
    def delete_all(self):
        from forward_and_spot.models import Voucher
        from distribution.models import Distribution
        from testing.models import Question
        MasterMan.invalidate_caches()
        Offer.objects.all().delete()
        Player.objects.all().delete()
        Player_stats.objects.all().delete()

        Period.objects.all().delete()
        Phase.objects.all().delete()
        Group.objects.all().delete()
        Voucher.objects.all().delete()
        Question.objects.all().delete()
        Experiment.objects.all().delete()
        Timer.objects.all().delete()
        Distribution.objects.all().delete()
        User.objects.all().delete()
        Auction.objects.all().delete()

    def setUp(self):
        print("+"*40)
        print("test_set_offer_quick_succession1(TestCase):")
        self.delete_all()
        function_in_FS_views_with_auction_setup.setUp(self)
        print("**********************")
        print("setUp")
        print("**********************")


    def tearDown(self):
        self.delete_all()
        print("**********************")
        print("tearDown --- DELETED")
        print("**********************")

    def test_list1sell2onbuys60_role_0_on_1_nomultipleoffers(self):
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]
        auction, treatment = Auction.cache_or_create_auction()
        treatment.allow_multiple_offers = False
        treatment.time_for_succession = 0
        treatment.save_and_cache()
        # MasterMan.cache_me('treatment', treatment)
        # auction = Auction.objects.get_or_create(treatment=treatment)[0]


        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        username = "u2"
        user2 = User.objects.get_or_create(username=username)[0]

        user_list = User.objects.all()
        self.assertTrue(user_list.count() == 1)

        group = Group.objects.get_or_create(idd=1, auction=auction)[0]



        player2 = Player.objects.get_or_create(role=1, user=user2, auction=auction, group=group)[0]

        player2.save()

        player_offer_id = player2.id
        p_offer_stats = \
            Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period)[0]
        p_offer_stats.save()

        start = 0
        # Voucher.objects.values_list
        posedc_type = 0  # SELL
        postedc_quantity = 4
        postedc_price = 459

        username = "u1"
        user1 = User.objects.get_or_create(username=username)[0]
        user1_id = user1.id

        player1 = Player.objects.get_or_create(role=0, user=user1, auction=auction, group=group)[0]
        player1.save()
        player_id1 = player1.id
        p1_stats = \
        Player_stats.objects.get_or_create(player=player1, auction=auction, group=group, period=period, role=player1.role)[
            0]
        p1_stats.save()
        posedc_type1 = 0  # BUY
        postedc_quantity1 = 3
        postedc_price1 = 10
        data = {}
        data['priceOriginal'] = postedc_price
        data['unitsOriginal'] = postedc_quantity
        data['Type'] = posedc_type
        data['auction_id'] = auction.id
        data['user_id'] = user1.id
        data['player_id'] = player1.id
        data['group_id'] = group.id

        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user1
        print("set_offer(request)")

        for i in range(2):
            set_offer(request)

        print("")
        print("All offers now")
        offer_list = Offer.objects.all()
        # for offer in offer_list:
        #     print("offer:{}".format(offer))
        print("")
        print("")
        # print("treatment.time_for_succession:{}".format(treatment.time_for_succession))
        self.assertEqual(offer_list.count(), 2)

        data = {}
        data['priceOriginal'] = 110
        data['unitsOriginal'] = 3
        data['Type'] = 1
        data['auction_id'] = auction.id
        data['user_id'] = user2.id
        data['player_id'] = player2.id
        data['group_id'] = group.id

        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user2
        print("set_offer(request)")

        for i in range(2):
            set_offer(request)

        data = {}
        data['priceOriginal'] = 2
        data['unitsOriginal'] = 2
        data['Type'] = 0
        data['auction_id'] = auction.id
        data['user_id'] = user1.id
        data['player_id'] = player1.id
        data['group_id'] = group.id

        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user1
        print("set_offer(request)")

        for i in range(2):
            set_offer(request) # here I get the problem!

        result = Offer.objects.all()
        # print("result: ", result)
        print("")
        print("")

        # print(connection.queries)

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)


        result_offer0 = Offer.objects.filter(offer_tiepe=0).all()
        result_offer1 = Offer.objects.filter(offer_tiepe=1).all()
        # print("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        # print("result_offer0: ", result_offer0)
        # print("result_offer1: ", result_offer1)
        #
        # print("result_offer0.all().count():{}".format(
        #     result_offer0.all().count()))

        # print("result_offer1.filter(unitsAvailable=3).count():{}".format(
        #     result_offer1.filter(unitsAvailable=3).count()))
        #
        # print("result_offer1.filter(unitsAvailable=3, unitsCleared=3).count():{}".format(
        #     result_offer1.filter(unitsAvailable=3, unitsCleared=2).count()))
        # print("result_offer1.filter(unitsAvailable=3, unitsCleared=1).count():{}".format(
        #     result_offer1.filter(unitsAvailable=3, unitsCleared=1).count()))

        self.assertEqual(Offer.objects.filter(offer_tiepe=0).all().count(), 5)

        self.assertEqual(Offer.objects.filter(offer_tiepe=1, unitsAvailable=0).all().count(), 2)
        self.assertEqual(Offer.objects.filter(offer_tiepe=1, unitsAvailable=3).all().count(), 1)
        # print("result_offer1.all().count():{}".format(
        #     result_offer1.all().count()))
        # print("result_offer1.filter(unitsAvailable=0,unitsCleared=2).count():{}".format(
        #     result_offer1.filter(unitsAvailable=0, unitsCleared=2).count()))
        # print("result_offer1.filter(unitsAvailable=0,unitsCleared=1).count():{}".format(
        #     result_offer1.filter(unitsAvailable=0, unitsCleared=1).count()))

        self.assertEqual(result_offer1.all().count(), 3)
        self.assertEqual(result_offer1.filter(unitsAvailable=3).count(), 1)
        self.assertEqual(result_offer1.filter(unitsAvailable=0, unitsCleared=1).count(), 1)

        result_pstats = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player1)
        # print("result_pstats", result_pstats)
        # print("result_pstats2", result_pstats2)
        self.assertEqual(result_pstats.profit, -330)
        self.assertEqual(result_pstats.vouchers_used, 0)
        self.assertEqual(result_pstats.vouchers_negative, 3)
        self.assertEqual(result_pstats.trading_result, -330)
        self.assertEqual(result_pstats2.profit, 329.6)
        self.assertEqual(result_pstats2.vouchers_used, 3)
        self.assertEqual(result_pstats2.vouchers_negative, 0)
        self.assertEqual(result_pstats2.trading_result, 330)

        print("**********************************************")
        print("SUCCESS 13")
        print("**********************************************")











    def test_list1sell2onbuys60_role_0_on_1_nomultipleoffersb(self):
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]
        auction, treatment = Auction.cache_or_create_auction()
        treatment.allow_multiple_offers = False
        treatment.time_for_succession = 2
        treatment.save_and_cache()
        # MasterMan.cache_me('treatment', treatment)
        # auction = Auction.objects.get_or_create(treatment=treatment)[0]


        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        username = "u2"
        user2 = User.objects.get_or_create(username=username)[0]

        user_list = User.objects.all()
        self.assertTrue(user_list.count() == 1)

        group = Group.objects.get_or_create(idd=1, auction=auction)[0]



        player2 = Player.objects.get_or_create(role=1, user=user2, auction=auction, group=group)[0]

        player2.save()

        player_offer_id = player2.id
        p_offer_stats = \
            Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period)[0]
        p_offer_stats.save()

        start = 0
        # Voucher.objects.values_list
        posedc_type = 0  # SELL
        postedc_quantity = 4
        postedc_price = 459

        username = "u1"
        user1 = User.objects.get_or_create(username=username)[0]
        user1_id = user1.id

        player1 = Player.objects.get_or_create(role=0, user=user1, auction=auction, group=group)[0]
        player1.save()
        player_id1 = player1.id
        p1_stats = \
        Player_stats.objects.get_or_create(player=player1, auction=auction, group=group, period=period, role=player1.role)[
            0]
        p1_stats.save()
        posedc_type1 = 0  # BUY
        postedc_quantity1 = 3
        postedc_price1 = 10
        data = {}
        data['priceOriginal'] = postedc_price
        data['unitsOriginal'] = postedc_quantity
        data['Type'] = posedc_type
        data['auction_id'] = auction.id
        data['user_id'] = user1.id
        data['player_id'] = player1.id
        data['group_id'] = group.id

        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user1
        print("set_offer(request)")

        for i in range(2):
            set_offer(request)

        print("")
        print("All offers now")
        offer_list = Offer.objects.all()
        # for offer in offer_list:
        #     print("offer:{}".format(offer))
        print("")
        print("")
        # print("treatment.time_for_succession:{}".format(treatment.time_for_succession))
        self.assertEqual(offer_list.count(), 1)

        data = {}
        data['priceOriginal'] = 110
        data['unitsOriginal'] = 3
        data['Type'] = 1
        data['auction_id'] = auction.id
        data['user_id'] = user2.id
        data['player_id'] = player2.id
        data['group_id'] = group.id

        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user2
        # print("set_offer(request)")

        for i in range(2):
            set_offer(request)

        data = {}
        data['priceOriginal'] = 2
        data['unitsOriginal'] = 2
        data['Type'] = 0
        data['auction_id'] = auction.id
        data['user_id'] = user1.id
        data['player_id'] = player1.id
        data['group_id'] = group.id

        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user1
        print("set_offer(request)")

        for i in range(2):
            set_offer(request) # here I get the problem!

        result = Offer.objects.all()
        # print("result: ", result)
        print("")
        print("")

        # print(connection.queries)

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)


        result_offer0 = Offer.objects.filter(offer_tiepe=0).all()
        result_offer1 = Offer.objects.filter(offer_tiepe=1).all()
        # print("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        # print("result_offer0: ", result_offer0)
        # print("result_offer1: ", result_offer1)
        #
        # print("result_offer0.all().count():{}".format(
        #     result_offer0.all().count()))

        # print("result_offer1.filter(unitsAvailable=3).count():{}".format(
        #     result_offer1.filter(unitsAvailable=3).count()))
        #
        # print("result_offer1.filter(unitsAvailable=3, unitsCleared=3).count():{}".format(
        #     result_offer1.filter(unitsAvailable=3, unitsCleared=2).count()))
        # print("result_offer1.filter(unitsAvailable=3, unitsCleared=1).count():{}".format(
        #     result_offer1.filter(unitsAvailable=3, unitsCleared=1).count()))

        self.assertEqual(Offer.objects.filter(offer_tiepe=0).all().count(), 1)

        self.assertEqual(Offer.objects.filter(offer_tiepe=1, unitsAvailable=0).all().count(), 0)
        self.assertEqual(Offer.objects.filter(offer_tiepe=1, unitsAvailable=3).all().count(), 1)
        # print("result_offer1.all().count():{}".format(
        #     result_offer1.all().count()))
        # print("result_offer1.filter(unitsAvailable=0,unitsCleared=2).count():{}".format(
        #     result_offer1.filter(unitsAvailable=0, unitsCleared=2).count()))
        # print("result_offer1.filter(unitsAvailable=0,unitsCleared=1).count():{}".format(
        #     result_offer1.filter(unitsAvailable=0, unitsCleared=1).count()))

        self.assertEqual(result_offer1.all().count(), 1)
        self.assertEqual(result_offer1.filter(unitsAvailable=3).count(), 1)
        self.assertEqual(result_offer1.filter(unitsAvailable=0, unitsCleared=1).count(), 0)

        result_pstats = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player1)
        # print("result_pstats", result_pstats)
        # print("result_pstats2", result_pstats2)
        self.assertEqual(result_pstats.profit, 0)
        self.assertEqual(result_pstats.vouchers_used, 0)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 0)
        self.assertEqual(result_pstats2.profit, 0)
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 0)
        self.assertEqual(result_pstats2.trading_result, 0)

        print("**********************************************")
        print("SUCCESS 13")
        print("**********************************************")
