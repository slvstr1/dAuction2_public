from django.test import TestCase, TransactionTestCase
from forward_and_spot.models import Offer, Auction, Player, Group, Player_stats, Period, Phase, Treatment, Voucher
from dAuction2.models import Experiment
from dAuction2.models import User
from .views import set_offer_nr
from forward_and_spot.test_views_set_offer import function_in_FS_views_with_auction_setup,delete_all
# from master.functions_main import createVoucher

class test_create_matching_offer_list(TransactionTestCase):
    # def setUp(self):
    #     self
    def setUp(self):
        print("+"*40)
        print("test_set_offer_quick_succession1(TestCase):")
        # experiment = Experiment.objects.get_or_create()[0]
        # experiment.save()
        # auction, treatment = Auction.cache_or_create_auction()
        # treatment.a=1
        # treatment.F=0
        # treatment.convexity_parameter=1
        # treatment.retail_price=197
        # treatment.save_and_cache()
        delete_all(self)
        function_in_FS_views_with_auction_setup.setUp(self)

    def test_list_none(self):
        # experiment = Experiment.objects.get_or_create()[0]
        # experiment.save()
        auction, treatment = Auction.cache_or_create_auction()

        auction_id=auction.id
        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        # user_id=user.id
        user2 = User.objects.get_or_create()[0]

        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        group2 = Group.objects.get_or_create(idd=2, auction=auction)[0]
        group2_id = group2.id
        player = Player.objects.get_or_create(user=user,auction=auction,group=group)[0]
        player2 = Player.objects.get_or_create(user=user2, auction=auction, group=group)[0]
        player.save()
        player2.save()
        player_id = player.id
        player2_id = player2.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,period=period)[0]

        posedc_type = 0 # SELL
        postedc_quantity = 5
        postedc_price = 1

        posedc_type2 = 1  # SELL

        c, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase,player_id,posedc_type,postedc_quantity,postedc_price,group_id,player)
        c.save()
        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id, posedc_type2, postedc_quantity, postedc_price,group2_id, player)
        c2.save()
        result = c.create_matching_offer_list(auction_id,phase,player_id,group_id)
        # print ("result: ",result)
        self.assertTrue(len(result)==0)

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        # print("result_pstats",result_pstats)
        # print("result_pstats2", result_pstats2)
        self.assertEqual(result_pstats.profit, 0)
        self.assertEqual(result_pstats.vouchers_used, 0)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 0)
        self.assertEqual(result_pstats2.profit, 0 )
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 0)
        self.assertEqual(result_pstats2.trading_result, 0)


    def test_list_sell_on_buy(self):
        # experiment = Experiment.objects.get_or_create()[0]
        # experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        # auction = Auction.objects.get_or_create(treatment=treatment)[0]

        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        username = "u1"
        user = User.objects.create(username=username)
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user, auction=auction, group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group, period=period)[0]

        username = "u2"
        user2 = User.objects.create(username=username)
        user_id2 = user2.id
        player2 = Player.objects.get_or_create(user=user2, auction=auction, group=group)[0]
        player2.save()
        p2_stats = Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period,role=player2.role)[0]
        p2_stats.save()
        player_id2 = player2.id

        posedc_type2 = 1  # SELL
        postedc_quantity2 = 5
        postedc_price2 = 1

        c2, reuse,cc = Offer.create_present_offer(treatment, auction_id, phase, player_id2, posedc_type2, postedc_quantity2,postedc_price2, group_id, player2)
        c2.save()


        posedc_type = 0  # SELL
        postedc_quantity = 5
        postedc_price = 1

        c, reuse,cc = Offer.create_present_offer(treatment, auction_id, phase, player_id, posedc_type, postedc_quantity,
                                 postedc_price, group_id, player)

        result = c.create_matching_offer_list( auction_id, phase, player_id, group_id)
        # print("result: ", result)
        self.assertFalse(len(result) == 0)

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        # print("result_pstats",result_pstats)
        # print("result_pstats2", result_pstats2)
        self.assertEqual(result_pstats.profit, 0)
        self.assertEqual(result_pstats.vouchers_used, 0)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 0)
        self.assertEqual(result_pstats2.profit, 0 )
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 0)
        self.assertEqual(result_pstats2.trading_result, 0)


    def test_list_buy_on_sell(self):
        # experiment = Experiment.objects.get_or_create()[0]
        # experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        # auction = Auction.objects.get_or_create(treatment=treatment)[0]

        auction, treatment = Auction.cache_or_create_auction()

        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        username = "u1"
        user = User.objects.create(username=username)
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user, auction=auction, group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group, period=period)[0]

        username = "u2"
        user2 = User.objects.create(username=username)
        user_id2 = user2.id
        player2 = Player.objects.get_or_create(user=user2, auction=auction, group=group)[0]
        player2.save()
        player_id2 = player2.id
        p2_stats = Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period,role=player2.role)[0]
        p2_stats.save()

        posedc_type2 = 0  # SELL
        postedc_quantity2 = 5
        postedc_price2 = 1

        c2, reuse,cc = Offer.create_present_offer(treatment, auction_id, phase, player_id2, posedc_type2, postedc_quantity2,
                                  postedc_price2, group_id, player2)
        c2.save()

        posedc_type = 1  # BUY
        postedc_quantity = 5
        postedc_price = 1

        c, reuse,cc = Offer.create_present_offer(treatment, auction_id, phase, player_id, posedc_type, postedc_quantity,
                                 postedc_price, group_id, player)

        result = c.create_matching_offer_list(auction_id, phase, player_id, group_id)
        # print("result: ", result)
        self.assertFalse(len(result) == 0)

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        # print("result_pstats",result_pstats)
        # print("result_pstats2", result_pstats2)
        self.assertEqual(result_pstats.profit, 0)
        self.assertEqual(result_pstats.vouchers_used, 0)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 0)
        self.assertEqual(result_pstats2.profit, 0 )
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 0)
        self.assertEqual(result_pstats2.trading_result, 0)


    def test_list_sell_on_buy_but_same(self):
        # experiment = Experiment.objects.get_or_create()[0]
        # experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        # auction = Auction.objects.get_or_create(treatment=treatment)[0]

        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        username = "u1"
        user = User.objects.create(username=username)
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user, auction=auction, group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group, period=period)[0]
        p_stats.save()

        username = "u2"
        user2 = User.objects.create(username=username)
        user_id2 = user2.id
        player2 = Player.objects.get_or_create(user=user2, auction=auction, group=group)[0]
        player2.save()
        player_id2 = player2.id
        p2_stats = Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period,
                                                      role=player2.role)[0]
        p2_stats.save()


        posedc_type2 = 1  # SELL
        postedc_quantity2 = 5
        postedc_price2 = 1

        c2, reuse,cc = Offer.create_present_offer(treatment, auction_id, phase, player_id, posedc_type2, postedc_quantity2, postedc_price2, group_id, player)
        c2.save()

        posedc_type = 0  # SELL
        postedc_quantity = 5
        postedc_price = 1

        c, reuse,cc = Offer.create_present_offer(treatment, auction_id, phase, player_id, posedc_type, postedc_quantity,
                                 postedc_price, group_id, player)

        result = c.create_matching_offer_list(auction_id, phase, player_id, group_id)
        # print("result: ", result)
        self.assertTrue(len(result) == 0)

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        # print("result_pstats",result_pstats)
        # print("result_pstats2", result_pstats2)
        self.assertEqual(result_pstats.profit, 0)
        self.assertEqual(result_pstats.vouchers_used, 0)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 0)
        self.assertEqual(result_pstats2.profit, 0)
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 0)
        self.assertEqual(result_pstats2.trading_result, 0)



    def test_list_sell_on_sell(self):
        # experiment = Experiment.objects.get_or_create()[0]
        # experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        # auction = Auction.objects.get_or_create(treatment=treatment)[0]

        auction, treatment = Auction.cache_or_create_auction()

        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        username = "u1"
        user = User.objects.create(username=username)
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user, auction=auction, group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group, period=period)[0]

        username = "u2"
        user2 = User.objects.create(username=username)
        user_id2 = user2.id
        player2 = Player.objects.get_or_create(user=user2, auction=auction, group=group)[0]
        player2.save()
        player_id2 = player2.id
        p2_stats = Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period,role=player2.role)[0]
        p2_stats.save()

        posedc_type2 = 0  # SELL
        postedc_quantity2 = 5
        postedc_price2 = 1

        c2, reuse,cc = Offer.create_present_offer(treatment, auction_id, phase, player_id2, posedc_type2, postedc_quantity2,postedc_price2, group_id, player2)
        c2.save()


        posedc_type = 0  # SELL
        postedc_quantity = 5
        postedc_price = 1

        c, reuse,cc = Offer.create_present_offer(treatment, auction_id, phase, player_id, posedc_type, postedc_quantity,
                                 postedc_price, group_id, player)

        result = c.create_matching_offer_list(auction_id, phase, player_id, group_id)
        # print("result: ", result)
        self.assertTrue(len(result) == 0)

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        # print("result_pstats",result_pstats)
        # print("result_pstats2", result_pstats2)
        self.assertEqual(result_pstats.profit, 0)
        self.assertEqual(result_pstats.vouchers_used, 0)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 0)
        self.assertEqual(result_pstats2.profit, 0)
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 0)
        self.assertEqual(result_pstats2.trading_result, 0)



    def test_list_buy_on_buy(self):
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        # auction = Auction.objects.get_or_create(treatment=treatment)[0]

        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        username = "u1"
        user = User.objects.create(username=username)
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user, auction=auction, group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group, period=period)[0]

        username = "u2"
        user2 = User.objects.create(username=username)
        user_id2 = user2.id
        player2 = Player.objects.get_or_create(user=user2, auction=auction, group=group)[0]
        player2.save()
        player_id2 = player2.id
        p2_stats = Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period,role=player2.role)[0]

        posedc_type2 = 1  # BUY
        postedc_quantity2 = 5
        postedc_price2 = 1

        c2, reuse,cc = Offer.create_present_offer(treatment, auction_id, phase, player_id2, posedc_type2, postedc_quantity2,postedc_price2, group_id, player2)
        c2.save()


        posedc_type = 1  # BUY
        postedc_quantity = 5
        postedc_price = 1

        c, reuse,cc = Offer.create_present_offer(treatment, auction_id, phase, player_id, posedc_type, postedc_quantity,
                                 postedc_price, group_id, player)

        result = c.create_matching_offer_list(auction_id, phase, player_id, group_id)
        # print("result: ", result)
        self.assertTrue(len(result) == 0)
        result2 = Offer.objects.all()
        # print("result2:", result2)

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        # print("result_pstats",result_pstats)
        # print("result_pstats2", result_pstats2)
        self.assertEqual(result_pstats.profit, 0)
        self.assertEqual(result_pstats.vouchers_used, 0)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 0)
        self.assertEqual(result_pstats2.profit, 0 )
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 0)
        self.assertEqual(result_pstats2.trading_result, 0)



class test_set_offer_none(TransactionTestCase):
    def setUp(self):
        print("+"*40)
        print("test_set_offer_quick_succession1(TestCase):")
        delete_all(self)
        function_in_FS_views_with_auction_setup.setUp(self)

        # experiment = Experiment.objects.get_or_create()[0]
        # experiment.save()
        # auction, treatment = Auction.cache_or_create_auction()
        # treatment.a=1
        # treatment.F=0
        # treatment.convexity_parameter=1
        # treatment.retail_price=197
        # # treatment.save_and_cache()


    def test_list_sell_on_none(self):
        # experiment = Experiment.objects.get_or_create()[0]
        # experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        # auction = Auction.objects.get_or_create(treatment=treatment)[0]

        auction, treatment = Auction.cache_or_create_auction()

        auction_id=auction.id
        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user,auction=auction,group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,period=period)[0]
        start=0

        posedc_type = 0 # SELL
        postedc_quantity = 5
        postedc_price = 1

        result = Offer.objects.all()
        # print("result: ", result)

        set_offer_nr(treatment, auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.all()
        # print ("result: ",result)
        self.assertTrue(result.exists())
        result_offer = Offer.objects.last()
        # print("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        # print("result_offer: ", result_offer)
        # self.assertEqual(result_offer.role,0)
        self.assertEqual(result_offer.unitsAvailable, 5)
        self.assertEqual(result_offer.priceOriginal, 1)

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        # print("result_pstats",result_pstats)
        self.assertEqual(result_pstats.profit, 0)
        self.assertEqual(result_pstats.vouchers_used, 0)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 0)


class test_set_offer(TransactionTestCase):
    def setUp(self):
        print("+"*40)
        print("test_set_offer_quick_succession1(TestCase):")
        delete_all(self)
        function_in_FS_views_with_auction_setup.setUp(self)

        # experiment = Experiment.objects.get_or_create()[0]
        # experiment.save()
        # # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]
        # auction, treatment = Auction.cache_or_create_auction()
        # treatment.a=1
        # treatment.F=0
        # treatment.convexity_parameter=1
        # treatment.retail_price=197
        # treatment.save_and_cache()


    def test_list_sell_on_buy_same(self):
        # from master.functions_main import createVoucher
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        # auction = Auction.objects.get_or_create(treatment=treatment)[0]

        auction, treatment = Auction.cache_or_create_auction()

        auction_id=auction.id
        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        # auction=Voucher.createVoucher(auction, treatment)

        player = Player.objects.get_or_create(user=user,auction=auction,group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,period=period)[0]
        start=0
        # Voucher.objects.values_list



        posedc_type = 0 # SELL
        postedc_quantity = 5
        postedc_price = 1

        result = Offer.objects.all()
        # print("result: ", result)


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

        c2, reuse,cc = Offer.create_present_offer(treatment, auction_id, phase, player_id2, posedc_type2, postedc_quantity2,postedc_price2, group_id, player2)
        c2.save()


        set_offer_nr(treatment, auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.filter(cleared=False)
        print ("result: ",result)
        self.assertFalse(result.exists())
        result_offer0 = Offer.objects.filter(offer_tiepe=0)
        result_offer1 = Offer.objects.filter(offer_tiepe=1)
        # print("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        # print("result_offer0: ", result_offer0)
        # print("result_offer1: ", result_offer1)
        result_offer0 =result_offer0[0]
        result_offer1 = result_offer1[0]
        self.assertEqual(result_offer0.offer_tiepe,0)
        self.assertEqual(result_offer0.priceOriginal, 1)
        self.assertEqual(result_offer0.unitsAvailable, 0)

        self.assertEqual(result_offer0.priceCleared, 1)
        self.assertEqual(result_offer0.unitsCleared, 5)
        # self.assertEqual(result_offer0.unitsOriginal, 5)
        # ! -1 ???

        self.assertEqual(result_offer1.offer_tiepe, 1)
        self.assertEqual(result_offer1.priceOriginal, 1)
        self.assertEqual(result_offer1.unitsAvailable, 0)

        self.assertEqual(result_offer1.priceCleared, 1)
        self.assertEqual(result_offer1.unitsCleared, 5)
        # self.assertEqual(result_offer1.unitsOriginal, 5)

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        # print("result_pstats",result_pstats)
        # print("result_pstats2", result_pstats2)
        # self.assertEqual(result_pstats.profit, 0)
        self.assertEqual(result_pstats.vouchers_used, 5)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 5)
        # self.assertEqual(result_pstats2.profit, -5 )
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 5)
        self.assertEqual(result_pstats2.trading_result, -5)


    def test_list_sell_on_buy_smaller(self):
        # from master.functions_main import createVoucher
        # experiment = Experiment.objects.get_or_create()[0]
        # experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        # auction = Auction.objects.get_or_create(treatment=treatment)[0]

        auction, treatment = Auction.cache_or_create_auction()

        auction_id=auction.id
        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        # auction=Voucher.createVoucher(auction, treatment)

        player = Player.objects.get_or_create(user=user,auction=auction,group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,period=period)[0]
        start=0
        # Voucher.objects.values_list


        username = "u2"
        user2 = User.objects.create(username=username)
        user_id2 = user2.id
        player2 = Player.objects.get_or_create(user=user2, auction=auction, group=group)[0]
        player2.save()
        player_id2 = player2.id
        p_stats2 = Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period)[0]



        posedc_type = 0 # SELL
        postedc_quantity = 4
        postedc_price = 1

        # result = Offer.objects.all()
        # print("result: ", result)
        posedc_type2 = 1  # BUY
        postedc_quantity2 = 5
        postedc_price2 = 2

        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id2, posedc_type2, postedc_quantity2,postedc_price2, group_id, player2)
        c2.save()


        set_offer_nr(treatment, auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.filter(cleared=False)
        print ("result: ",result)
        self.assertTrue(result.exists())
        result_offer0 = Offer.objects.filter(offer_tiepe=0)
        result_offer1nc = Offer.objects.filter(offer_tiepe=1,cleared=False)
        result_offer1c = Offer.objects.filter(offer_tiepe=1,cleared=True)
        # print("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        print("result_offer0: ", result_offer0)
        print("result_offer1nc: ", result_offer1nc)
        print("result_offer1: ", result_offer1c)
        result_offer0 =result_offer0[0]
        result_offer1nc = result_offer1nc[0]
        result_offer1c = result_offer1c[0]
        self.assertEqual(result_offer0.offer_tiepe,0)
        self.assertEqual(result_offer0.priceOriginal, 1)
        self.assertEqual(result_offer0.unitsAvailable, 0)

        self.assertEqual(result_offer0.priceCleared, 2)
        self.assertEqual(result_offer0.unitsCleared, 4)
        # self.assertEqual(result_offer0.unitsOriginal, 5)
        # ! -1 ???

        self.assertEqual(result_offer1nc.offer_tiepe, 1)
        self.assertEqual(result_offer1nc.priceOriginal, 2)
        self.assertEqual(result_offer1nc.unitsAvailable, 1)
        self.assertEqual(result_offer1nc.priceCleared, 0)
        self.assertEqual(result_offer1nc.unitsCleared, 0)

        self.assertEqual(result_offer1c.offer_tiepe, 1)
        self.assertEqual(result_offer1c.priceOriginal, 2)
        self.assertEqual(result_offer1c.unitsAvailable, 0)
        self.assertEqual(result_offer1c.priceCleared, 2)
        self.assertEqual(result_offer1c.unitsCleared, 4)

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        print("result_pstats",result_pstats)
        print("result_pstats2", result_pstats2)
        # self.assertEqual(result_pstats.profit, 4)
        self.assertEqual(result_pstats.vouchers_used, 4)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 8)
        # self.assertEqual(result_pstats2.profit, -8 )
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 4)
        self.assertEqual(result_pstats2.trading_result, -8)


    def test_list_sell_on_buy_larger(self):
        # experiment = Experiment.objects.get_or_create()[0]
        # experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        # auction = Auction.objects.get_or_create(treatment=treatment)[0]

        auction, treatment = Auction.cache_or_create_auction()
        auction_id=auction.id
        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        # auction=Voucher.createVoucher(auction, treatment)

        player = Player.objects.get_or_create(user=user,auction=auction,group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,period=period)[0]
        start=0
        # Voucher.objects.values_list



        result = Offer.objects.all()
        print("result: ", result)


        username = "u2"
        user2 = User.objects.create(username=username)
        user_id2 = user2.id
        player2 = Player.objects.get_or_create(user=user2, auction=auction, group=group)[0]
        player2.save()
        player_id2 = player2.id
        p_stats2 = Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period)[0]


        posedc_type = 0 # SELL
        postedc_quantity = 5
        postedc_price = 1

        posedc_type2 = 1  # BUY
        postedc_quantity2 = 4
        postedc_price2 = 3

        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id2, posedc_type2, postedc_quantity2,postedc_price2, group_id, player2)
        c2.save()

        import time
        start_time=time.time()
        print("start set_offer")
        set_offer_nr(treatment, auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)
        end_time=time.time()
        print("total:{}".format(round(end_time-start_time,3)))
        # assert (False)

        result = Offer.objects.filter(cleared=False)
        print ("result: ",result)

        print("result = Offer.objects.all()", Offer.objects.all())
        self.assertTrue(result.exists())


        result_offer0nc = Offer.objects.filter(offer_tiepe=0,cleared=False)
        result_offer0c = Offer.objects.filter(offer_tiepe=0, cleared=True)
        result_offer1 = Offer.objects.filter(offer_tiepe=1)
        # print("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        print("result_offer0nc: ", result_offer0nc)
        print("result_offer0c: ", result_offer0c)
        print("result_offer1: ", result_offer1)
        result_offer0nc =result_offer0nc[0]
        result_offer0c = result_offer0c[0]
        result_offer1 = result_offer1[0]

        self.assertEqual(result_offer0nc.offer_tiepe,0)
        self.assertEqual(result_offer0nc.priceOriginal, 1)
        self.assertEqual(result_offer0nc.unitsAvailable, 1)
        self.assertEqual(result_offer0nc.priceCleared, 0)
        self.assertEqual(result_offer0nc.unitsCleared, 0)

        self.assertEqual(result_offer0c.offer_tiepe, 0)
        self.assertEqual(result_offer0c.priceOriginal, 1)
        self.assertEqual(result_offer0c.unitsAvailable, 0)
        self.assertEqual(result_offer0c.priceCleared, 3)
        self.assertEqual(result_offer0c.unitsCleared, 4)



        self.assertEqual(result_offer1.offer_tiepe, 1)
        self.assertEqual(result_offer1.priceOriginal, 3)
        self.assertEqual(result_offer1.unitsAvailable, 0)
        self.assertEqual(result_offer1.priceCleared, 3)
        self.assertEqual(result_offer1.unitsCleared, 4)
        # self.assertEqual(result_offer1.unitsOriginal, 5)

        result_pstats = Player_stats.objects.filter(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.filter(auction=auction, group=group, period=period, player=player2)
        print("result_pstats",result_pstats)
        print("result_pstats2", result_pstats2)

        Player_stats.objects.filter(player=player2,auction=auction,group=group,period=period).delete()
        Player.objects.filter(user=user2).delete()
        User.objects.filter(username="u2").delete()
        username = "u2"
        user2 = User.objects.get_or_create(username=username)[0]
        user_id2 = user2.id
        player2 = Player.objects.get_or_create(user=user2, auction=auction, group=group)[0]
        player2.save()
        player_id2 = player2.id
        p_stats2 = Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period)[0]

        posedc_type2 = 1  # BUY
        postedc_quantity2 = 5
        postedc_price2 = 1

        Offer.objects.all().delete()
        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id2, posedc_type2, postedc_quantity2,postedc_price2, group_id, player2)
        c2.save()

        posedc_type = 0  # SELL
        postedc_quantity = 5
        postedc_price = 1

        set_offer_nr(treatment, auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.filter(cleared=False)
        print ("result: ",result)
        self.assertFalse(result.exists())
        result_offer0 = Offer.objects.filter(offer_tiepe=0)
        result_offer1 = Offer.objects.filter(offer_tiepe=1)
        # print("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        print("result_offer0: ", result_offer0)
        print("result_offer1: ", result_offer1)
        result_offer0 =result_offer0[0]
        result_offer1 = result_offer1[0]
        self.assertEqual(result_offer0.offer_tiepe,0)
        self.assertEqual(result_offer0.priceOriginal, 1)
        self.assertEqual(result_offer0.unitsAvailable, 0)

        self.assertEqual(result_offer0.priceCleared, 1)
        self.assertEqual(result_offer0.unitsCleared, 5)
        # self.assertEqual(result_offer0.unitsOriginal, 5)
        # ! -1 ???

        self.assertEqual(result_offer1.offer_tiepe, 1)
        self.assertEqual(result_offer1.priceOriginal, 1)
        self.assertEqual(result_offer1.unitsAvailable, 0)

        self.assertEqual(result_offer1.priceCleared, 1)
        self.assertEqual(result_offer1.unitsCleared, 5)
        # self.assertEqual(result_offer1.unitsOriginal, 5)

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        print("result_pstats",result_pstats)
        print("result_pstats2", result_pstats2)
        # self.assertEqual(result_pstats.profit, 8)
        self.assertEqual(result_pstats.vouchers_used, 9)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 17)
        # self.assertEqual(result_pstats2.profit, -5 )
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 5)
        self.assertEqual(result_pstats2.trading_result, -5)
