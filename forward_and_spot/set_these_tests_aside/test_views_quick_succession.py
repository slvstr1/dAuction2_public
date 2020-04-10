from django.test import TestCase
from forward_and_spot.models import Offer, Auction, Player, Group, Player_stats, Period, Phase,Timer,Treatment
from dAuction2.models import Experiment
from dAuction2.models import User
from master.models import MasterMan
from .views import set_offer_nr,  set_offer
# from master.functions_main import createVoucher, invalidate_caches
from django.test import TestCase, RequestFactory
import time
from forward_and_spot.models import Voucher

class test_set_offer_quick_succession1(TestCase):
    # from master.functions_main import createVoucher
    def setUp(self):
        print("+"*40)
        print("test_set_offer_quick_succession1(TestCase):")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        treatment = Treatment.objects.get_or_create(experiment=experiment)[0]
        treatment.a = 1
        treatment.F = 0
        treatment.convexity_parameter = 1
        treatment.retail_price = 197
        treatment.save()


    def tearDown(self):
        # Clean up run after every test method.
        from forward_and_spot.models import Voucher
        from distribution.models import Distribution
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

    def test_list_sell_on_none_then_buy_sell(self):
        """
        tests that when player1 sells, and his sell gets immediately bought, he doesnt immediately resell
        """
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        treatment = Treatment.objects.get_or_create(experiment=experiment)[0]
        treatment.save()
        auction = Auction.objects.get_or_create(treatment=treatment)[0]

        auction.time_for_succession=4
        auction.save()
        auction_id=auction.id
        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        Voucher.createVoucher(auction, treatment)

        player = Player.objects.get_or_create(user=user,auction=auction,group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,period=period)[0]
        start=0
        posedc_type = 0 # SELL
        postedc_quantity = 5
        postedc_price = 1
        data = {}
        data['priceOriginal'] = postedc_price
        data['unitsOriginal'] = postedc_quantity
        data['Type'] = posedc_type
        data['auction_id'] = auction.id
        data['user_id'] = user.id
        data['player_id'] = player.id
        data['group_id'] = group.id
        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user


        username = "u2"
        user2 = User.objects.create(username=username)
        user_id2 = user2.id
        player2 = Player.objects.get_or_create(user=user2, auction=auction, group=group)[0]
        player2.save()
        player_id2 = player2.id
        p_stats2 = Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period)[0]
        posedc_type2 = 1  # BUY
        postedc_quantity2 = 5
        postedc_price2 = 1
        data2 = {}
        data2['priceOriginal'] = postedc_price2
        data2['unitsOriginal'] = postedc_quantity2
        data2['Type'] = posedc_type2
        data2['auction_id'] = auction.id
        data2['user_id'] = user2.id
        data2['player_id'] = player2.id
        data2['group_id'] = group.id
        self.factory = RequestFactory()
        request2 = self.factory.post('/', data2)
        request2.user = user2


        result = Offer.objects.all()
        print("result: ", result)

        print("set_offer(request)")
        set_offer(request)
        time.sleep(4.2)
        print("set_offer(request2)")
        set_offer(request2)
        print("set_offer(request)")
        set_offer(request)

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.all()
        print ("result: ",result)
        self.assertTrue(result.exists())
        result_offer = Offer.objects.last()
        # print("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        print("result_offer: ", result_offer)
        # self.assertEqual(result_offer.role,0)
        self.assertEqual(result_offer.unitsAvailable, 0)
        self.assertEqual(result_offer.priceOriginal, 1)
        print("**********************************************")
        print("SUCCESS 1")
        print("**********************************************")

    def test_list_sell_on_buy_then_sell(self):
        """
        tests that when player1 sells, and his sell gets immediately bought, he doesnt immediately resell
        """
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        treatment = Treatment.objects.get_or_create(experiment=experiment)[0]
        print("before treatmentsave")
        treatment.save()
        print("after treatmentsave")
        auction = Auction.objects.get_or_create(treatment=treatment)[0]
        auction.save()

        auction_id=auction.id
        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        Voucher.createVoucher(auction, treatment)

        player = Player.objects.get_or_create(user=user,auction=auction,group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,period=period)[0]
        start=0
        posedc_type = 0 # SELL
        postedc_quantity = 5
        postedc_price = 1
        data = {}
        data['priceOriginal'] = postedc_price
        data['unitsOriginal'] = postedc_quantity
        data['Type'] = posedc_type
        data['auction_id'] = auction.id
        data['user_id'] = user.id
        data['player_id'] = player.id
        data['group_id'] = group.id
        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user


        username = "u2"
        user2 = User.objects.create(username=username)
        user_id2 = user2.id
        player2 = Player.objects.get_or_create(user=user2, auction=auction, group=group)[0]
        player2.save()
        player_id2 = player2.id
        p_stats2 = Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period)[0]
        posedc_type2 = 1  # BUY
        postedc_quantity2 = 5
        postedc_price2 = 1
        data2 = {}
        data2['priceOriginal'] = postedc_price2
        data2['unitsOriginal'] = postedc_quantity2
        data2['Type'] = posedc_type2
        data2['auction_id'] = auction.id
        data2['user_id'] = user2.id
        data2['player_id'] = player2.id
        data2['group_id'] = group.id
        self.factory = RequestFactory()
        request2 = self.factory.post('/', data2)
        request2.user = user2


        result = Offer.objects.all()
        print("result: ", result)

        print("set_offer(request2)")
        set_offer(request2)
        print("set_offer(request)")
        set_offer(request)
        print("set_offer(request)")
        set_offer(request)

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.all()
        print ("result: ",result)
        self.assertTrue(result.exists())
        result_offer = Offer.objects.last()
        # print("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        print("result_offer: ", result_offer)
        # self.assertEqual(result_offer.role,0)
        self.assertEqual(result_offer.unitsAvailable, 0)
        self.assertEqual(result_offer.priceOriginal, 1)

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        print("result_pstats",result_pstats)
        print("result_pstats2", result_pstats2)
        self.assertEqual(result_pstats.profit, 0)
        self.assertEqual(result_pstats.vouchers_used, 5)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 5)
        self.assertEqual(result_pstats2.profit, -5 )
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 5)
        self.assertEqual(result_pstats2.trading_result, -5)



        print("**********************************************")
        print("SUCCESS 1")
        print("**********************************************")


        print("set_offer(request2)")
        set_offer(request2)
        print("set_offer(request)")
        set_offer(request)
        time.sleep(4.2)
        print("set_offer(request)")
        set_offer(request)

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.all()
        print ("result: ",result)
        self.assertTrue(result.exists())
        result_offer = Offer.objects.last()
        # print("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        print("result_offer: ", result_offer)
        # self.assertEqual(result_offer.role,0)
        self.assertEqual(result_offer.unitsAvailable, 5)
        self.assertEqual(result_offer.priceOriginal, 1)

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        print("result_pstats",result_pstats)
        print("result_pstats2", result_pstats2)

        self.assertTrue(result_pstats.profit == 0.0)
        self.assertTrue(result_pstats.vouchers_used == 5)
        self.assertTrue(result_pstats.vouchers_negative == 0)
        self.assertTrue(result_pstats.trading_result == 5)
        self.assertTrue(result_pstats2.profit == -5)
        self.assertTrue(result_pstats2.vouchers_used == 0)
        self.assertTrue(result_pstats2.vouchers_negative == 5)
        self.assertTrue(result_pstats2.trading_result == -5)



        print("**********************************************")
        print("SUCCESS 1")
        print("**********************************************")



    def test_list_sell_on_buy_then_sleep_then_sell(self):
        """
        tests that when player1 sells, and his sell gets immediately bought, he doesnt immediately resell
        """
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        treatment = Treatment.objects.get_or_create(experiment=experiment)[0]
        treatment.save()
        auction = Auction.objects.get_or_create(treatment=treatment)[0]
        auction.save()

        auction_id=auction.id
        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        Voucher.createVoucher(auction, treatment)

        player = Player.objects.get_or_create(user=user,auction=auction,group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,period=period)[0]
        start=0
        posedc_type = 0 # SELL
        postedc_quantity = 5
        postedc_price = 1
        data = {}
        data['priceOriginal'] = postedc_price
        data['unitsOriginal'] = postedc_quantity
        data['Type'] = posedc_type
        data['auction_id'] = auction.id
        data['user_id'] = user.id
        data['player_id'] = player.id
        data['group_id'] = group.id
        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user


        username = "u2"
        user2 = User.objects.create(username=username)
        user_id2 = user2.id
        player2 = Player.objects.get_or_create(user=user2, auction=auction, group=group)[0]
        player2.save()
        player_id2 = player2.id
        p_stats2 = Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period)[0]
        posedc_type2 = 1  # BUY
        postedc_quantity2 = 5
        postedc_price2 = 1
        data2 = {}
        data2['priceOriginal'] = postedc_price2
        data2['unitsOriginal'] = postedc_quantity2
        data2['Type'] = posedc_type2
        data2['auction_id'] = auction.id
        data2['user_id'] = user2.id
        data2['player_id'] = player2.id
        data2['group_id'] = group.id
        self.factory = RequestFactory()
        request2 = self.factory.post('/', data2)
        request2.user = user2


        result = Offer.objects.all()
        print("result: ", result)

        print("set_offer(request2)")
        set_offer(request2)
        print("set_offer(request)")
        set_offer(request)
        time.sleep(4.2)
        print("set_offer(request)")
        set_offer(request)

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.all()
        print ("result: ",result)
        self.assertTrue(result.exists())
        result_offer = Offer.objects.last()
        # print("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        print("result_offer: ", result_offer)
        # self.assertEqual(result_offer.role,0)
        self.assertEqual(result_offer.unitsAvailable, 5)
        self.assertEqual(result_offer.priceOriginal, 1)

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        print("result_pstats",result_pstats)
        print("result_pstats2", result_pstats2)
        self.assertEqual(result_pstats.profit, 0)
        self.assertEqual(result_pstats.vouchers_used, 5)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 5)
        self.assertEqual(result_pstats2.profit, -5 )
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 5)
        self.assertEqual(result_pstats2.trading_result, -5)



        print("**********************************************")
        print("SUCCESS 1")
        print("**********************************************")

        print("set_offer(request2)")
        set_offer(request2)
        print("set_offer(request)")
        set_offer(request)
        # time.sleep(4.2)
        print("set_offer(request)")
        set_offer(request)

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.all()
        print("result: ", result)
        self.assertTrue(result.exists())
        result_offer = Offer.objects.last()
        # print("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        print("result_offer: ", result_offer)
        # self.assertEqual(result_offer.role,0)
        self.assertEqual(result_offer.unitsAvailable, 0)
        self.assertEqual(result_offer.priceOriginal, 1)
        print("**********************************************")
        print("SUCCESS 2")
        print("**********************************************")