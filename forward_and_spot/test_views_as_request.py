import logging
from django.test import TestCase, RequestFactory, TransactionTestCase
from forward_and_spot.models import Treatment
from dAuction2.models import Experiment
from master.models import MasterMan
# Offer, Auction, Player, User, Group, Player_stats, Period, Phase,
from .views import set_offer_nr, set_offer
# from master.functions_main import createVoucher
from forward_and_spot.models import Offer, Auction, Player, Group, Player_stats, Period, Phase, Timer, Voucher
from dAuction2.models import Experiment
from dAuction2.models import User

from .test_views_set_offer import function_in_FS_views_with_auction_setup


# from master.functions_main import  cache_me, invalidate_caches, PlayerStats_create
from payout.views import main
# from forward_and_spot.models import Voucher
log = logging.getLogger(__name__)
logger = logging.getLogger(__name__)

# same as test_views.py, but with request
class test_set_offer_none(TransactionTestCase):
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
        log.info("+"*40)
        log.info("setUp")
        log.info("+" * 40)
        self.delete_all()
        # experiment = Experiment.objects.get_or_create()[0]
        # experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]
        # treatment.a=1
        # treatment.F=0
        # treatment.convexity_parameter=1
        # treatment.retail_price=197
        # treatment.active=True

        # tt = Timer()
        # tt.save_and_cache()

        function_in_FS_views_with_auction_setup.setUp(self)




    def tearDown(self):
        # Clean up run after every test method.
        self.delete_all()
        log.info("**********************")
        log.info("tearDown --- DELETED")
        log.info("**********************")

    def test_list_sell_on_none(self):
        print("START test 1")
        # MasterMan.invalidate_caches()

        # experiment = Experiment.objects.create()
        # experiment.save()
        # treatment = Treatment.objects.create(experiment=experiment, idd=1)
        # print("before treatment save")

        # print("after treatment save")
        # auction = Auction.objects.create(treatment=treatment)
        #
        # print("auction_:{}".format(auction))

        auction, treatment = Auction.cache_or_create_auction()
        period_list = Period.objects.filter( auction=auction).all()
        for p in period_list:
            print("period: {}, {}, {}".format(p, p.auction, p.updated))
        period = period_list.last()
        # period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        print("period:{}".format(period))
        print("before_phase")
        phase = Phase.objects.create(period=period,auction=auction,idd=1)
        phase.save()
        # user = User.objects.get_or_create()[0]
        user = User.objects.create()
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        # group_id = group.id
        # player = Player.objects.get_or_create(user=user,auction=auction,group=group)[0]
        player = Player.objects.create(user=user, auction=auction, group=group)
        player.save()
        player_id = player.id
        # p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,period=period)[0]
        p_stats = Player_stats.objects.create(player=player, auction=auction, group=group,period=period)
        p_stats.save()
        start=0
        # self.smallprep()

        posedc_type = 0 # SELL
        postedc_quantity = 5
        postedc_price = 1

        result = Offer.objects.all()
        log.info("result:{} ".format( result))

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

        log.info("set_offer(request)")

        set_offer(request)


        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.all()
        log.info ("result:{} ".format(result))
        self.assertTrue(result.exists())
        result_offer = Offer.objects.last()
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        log.info("result_offer: {}".format(result_offer))
        # self.assertEqual(result_offer.role,0)
        self.assertEqual(result_offer.unitsAvailable, 5)
        self.assertEqual(result_offer.priceOriginal, 1)
        log.info("**********************************************")
        log.info("SUCCESS 1")
        log.info("**********************************************")






    def test_list_sell_twice_on_none(self):
        MasterMan.invalidate_caches()
        # TestCase.tearDown()
        # TestCase.setUp()
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()

        period_list = Period.objects.filter(auction=auction).all()
        # for p in period_list:
        #     print("period: {}, {}, {}".format(p, p.auction, p.updated))
        period = period_list.last()
        # period = Period.objects.get_or_create(idd=1,auction=auction)[0]

        phase = Phase.objects.create(period=period, auction=auction, idd=1)
        phase.save()
        # user = User.objects.get_or_create()[0]
        user = User.objects.create()
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        # group_id = group.id
        # player = Player.objects.get_or_create(user=user,auction=auction,group=group)[0]
        player = Player.objects.create(user=user, auction=auction, group=group)
        player.save()
        player_id = player.id
        # p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,period=period)[0]
        p_stats = Player_stats.objects.create(player=player, auction=auction, group=group, period=period)
        p_stats.save()
        start = 0
        # self.smallprep()

        posedc_type = 0 # SELL
        postedc_quantity = 5
        postedc_price = 1

        result = Offer.objects.all()
        log.info("result:{}".format( result))

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

        log.info("set_offer(request)")
        set_offer(request)
        log.info("set_offer(request)")
        set_offer(request)


        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.all()
        log.info ("result:{} ".format(result))
        self.assertTrue(result.exists())
        result_offer = Offer.objects.last()
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        # log.info("result_offer: ", result_offer)
        # self.assertEqual(result_offer.role,0)
        self.assertEqual(result_offer.unitsAvailable, 5)
        self.assertEqual(result_offer.priceOriginal, 1)
        log.info("**********************************************")
        log.info("SUCCESS 2")
        log.info("**********************************************")

class test_set_offer(TransactionTestCase):

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
        log.info("+"*40)
        log.info("test_set_offer_quick_succession1(TestCase):")

        # print("1 total_vouchers:{}".format(Voucher.objects.all().count()))
        test_set_offer_none.setUp(self)
        # print("2 total_vouchers:{}".format(Voucher.objects.all().count()))
        #
        # experiment = Experiment.objects.get_or_create()[0]
        # experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]
        # treatment.a=1
        # treatment.F=0
        # treatment.convexity_parameter=1
        # treatment.retail_price=197
        # treatment.active = True

        # tt = Timer()
        # tt.save_and_cache()
        # function_in_FS_views_with_auction_setup.setUp(self)

    def tearDown(self):
        # Clean up run after every test method.
        test_set_offer_none.tearDown(self)
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
        # log.info("**********************")
        # log.info("tearDown --- DELETED")
        # log.info("**********************")

    def test_list_sell_on_buy_same(self):
        # 
        # 
        # 
        # print("3 total_vouchers:{}".format(Voucher.objects.all().count()))
        # MasterMan.invalidate_caches()
        # from master.functions_main import createVoucher
        log.info("START 8")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        # self.assertTrue(treatment.convexity_parameter == 1)
        # 
        #

        auction, treatment = Auction.cache_or_create_auction()
        auction_id=auction.id
        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        # 

        player = Player.objects.get_or_create(user=user,auction=auction,group=group)[0]
        player.save()
        player_id = player.id
        # print("4a total_vouchers:{}".format(Voucher.objects.all().count()))
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,period=period)[0]
        # print("4b total_vouchers:{}".format(Voucher.objects.all().count()))
        start=0
        # Voucher.objects.values_list


        posedc_type = 0 # SELL
        postedc_quantity = 5
        postedc_price = 1


        result = Offer.objects.all()
        # log.info("result: ", result)

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

        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id2, posedc_type2, postedc_quantity2,postedc_price2, group_id, player2)
        c2.save()
        result = Offer.objects.all()
        # log.info("result: ", result)
        # print("5 total_vouchers:{}".format(Voucher.objects.all().count()))

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
        log.info("set_offer(request)")

        # print("6 total_vouchers:{}".format(Voucher.objects.filter(auction=auction).count()))
        self.assertEqual(Voucher.objects.filter(auction=auction).count(),35)

        set_offer(request)

        result = Offer.objects.all()
        log.info("result:{} ".format( result))

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.filter(cleared=False)
        log.info("result:{} ".format(result))
        self.assertFalse(result.exists())
        result_offer0 = Offer.objects.filter(offer_tiepe=0).last()
        result_offer1 = Offer.objects.filter(offer_tiepe=1).last()

        log.info("result_offer0: {}, {}, {}".format( result_offer0, result_offer0.priceOriginal, result_offer0.unitsAvailable))

        log.info("result_offer1: {}, {}, {}".format(result_offer1,  result_offer1.priceOriginal,result_offer1.unitsAvailable))
        voucher_list = Voucher.objects.all()
        # for v in voucher_list:
        #     print("v:{}, {}, {}".format(v, v.value, v.value_cum))

        # log.info("result_offer0: {}", result_offer0)
        # log.info("result_offer1: ", result_offer1)
        # result_offer0 =result_offer0[0]
        # result_offer1 = result_offer1[0]
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
        self.assertEqual(result_pstats.profit , 5-2.8)
        self.assertEqual(result_pstats.vouchers_used ,5)
        self.assertEqual(result_pstats.vouchers_negative ,0)
        self.assertEqual(result_pstats.trading_result ,5)
        self.assertEqual(result_pstats2.profit ,-5)
        self.assertEqual(result_pstats2.vouchers_used , 0)
        self.assertEqual(result_pstats2.vouchers_negative , 5)
        self.assertEqual(result_pstats2.trading_result, -5)
        # log.info("result_pstats",result_pstats)
        # log.info("result_pstats2", result_pstats2)



        log.info("**********************************************")
        log.info("SUCCESS 8")
        log.info("**********************************************")


    def test_list_sell_on_buy_smallerb(self):
        # from master.functions_main import createVoucher
        # 
        # 
        # 
        # MasterMan.invalidate_caches()
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        # 
        #
        # auction_id=auction.id
        auction, treatment = Auction.cache_or_create_auction()

        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
#         
        auction_id=auction.id

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

        # standing offer
        posedc_type2 = 1  # BUY
        postedc_quantity2 = 5
        postedc_price2 = 2

        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id2, posedc_type2, postedc_quantity2,postedc_price2, group_id, player2)
        c2.save()

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
        log.info("set_offer(request)")
        set_offer(request)

        result = Offer.objects.all()
        log.info("result:{} ".format( result))

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.filter(cleared=False)
        log.info ("result:{} ".format(result))
        self.assertTrue(result.exists())
        result_offer0 = Offer.objects.filter(offer_tiepe=0)
        result_offer1nc = Offer.objects.filter(offer_tiepe=1,cleared=False)
        result_offer1c = Offer.objects.filter(offer_tiepe=1,cleared=True)
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        log.info("result_offer0:{} ".format( result_offer0))
        log.info("result_offer1nc: {}".format( result_offer1nc))
        log.info("result_offer1:{} ".format( result_offer1c))
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


        log.info("treatment.retail_price:{}".format(treatment.retail_price))

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        log.info("result_pstats:{}".format(result_pstats))
        log.info("result_pstats2:{}".format( result_pstats2))
        self.assertEqual(result_pstats.profit,8 - Voucher.objects.get(auction=auction, idd=4).value_cum)
        self.assertEqual(result_pstats.vouchers_used, 4)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 8)
        self.assertEqual(result_pstats2.profit , -8)
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 4)
        self.assertEqual(result_pstats2.trading_result, -8)


        log.info("**********************************************")
        log.info("SUCCESS 9")
        log.info("**********************************************")


    def test_list_sell_on_buy_smaller(self):
        # 
        # 
        # 
        # from master.functions_main import createVoucher
        from forward_and_spot.models import Voucher
        # MasterMan.invalidate_caches()
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        # 
        #
        auction, treatment = Auction.cache_or_create_auction()
        auction_id=auction.id
        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        # 
        from forward_and_spot.models import Voucher
        voucher_list = Voucher.objects.filter(auction=auction)
        log.info("voucher_list:{}".format(voucher_list))



        player = Player.objects.get_or_create(user=user,auction=auction,group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,period=period,player_demand=10)[0]
        start=0
        # Voucher.objects.values_list


        username = "u2"
        user2 = User.objects.create(username=username)
        user_id2 = user2.id
        player2 = Player.objects.get_or_create(user=user2, auction=auction, group=group,role=1)[0]
        player2.save()
        player_id2 = player2.id
        p_stats2 = Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period,role=1,player_demand=10)[0]

        posedc_type = 0 # SELL
        postedc_quantity = 4
        postedc_price = 1

        # standing offer
        posedc_type2 = 1  # BUY
        postedc_quantity2 = 5
        postedc_price2 = 2

        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id2, posedc_type2, postedc_quantity2,postedc_price2, group_id, player2)
        c2.save()

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
        log.info("set_offer(request)")
        set_offer(request)

        result = Offer.objects.all()
        log.info("result:{}".format( result))

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.filter(cleared=False)
        log.info ("result:{} ".format(result))
        self.assertTrue(result.exists())
        result_offer0 = Offer.objects.filter(offer_tiepe=0)
        result_offer1nc = Offer.objects.filter(offer_tiepe=1,cleared=False)
        result_offer1c = Offer.objects.filter(offer_tiepe=1,cleared=True)
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        log.info("result_offer0:{}".format( result_offer0))
        log.info("result_offer1nc:{} ".format( result_offer1nc))
        log.info("result_offer1:{} ".format( result_offer1c))
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


        log.info("treatment.retail_price:{}".format(treatment.retail_price))

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        log.info("result_pstats:{}".format(result_pstats))
        log.info("result_pstats2:{}".format( result_pstats2))
        self.assertEqual(result_pstats.profit,8 -Voucher.objects.get(auction=auction, idd=4).value_cum)
        self.assertEqual(result_pstats.vouchers_used, 4)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 8)
        # print("treatment.retail_price:{}".format(treatment.retail_price))
        # print("p_stats2.player_demand:{}".format(p_stats2.player_demand))
        self.assertEqual(result_pstats2.profit, -8 + treatment.retail_price*4)
        self.assertEqual(result_pstats2.vouchers_used, 4)
        self.assertEqual(result_pstats2.vouchers_negative, 0)
        self.assertEqual(result_pstats2.trading_result, -8)


        log.info("**********************************************")
        log.info("SUCCESS 9")
        log.info("**********************************************")


    def test_list_sell_on_buy_larger(self):
        # 
        # 
        # 
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        # 
        #
        auction, treatment = Auction.cache_or_create_auction()
        auction_id=auction.id
        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        # 

        voucher_list = Voucher.objects.filter(auction=auction)
        log.info("voucher_list:{}".format(voucher_list))

        player = Player.objects.get_or_create(user=user,auction=auction,group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,period=period)[0]
        start=0
        # Voucher.objects.values_list



        result = Offer.objects.all()
        log.info("result:{}".format( result))


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
        log.info("set_offer(request)")
        set_offer(request)

        result = Offer.objects.all()
        log.info("result:{}".format( result))

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.filter(cleared=False)
        log.info ("result:{}".format( result))

        log.info("result = Offer.objects.all():{}".format( Offer.objects.all()))
        self.assertTrue(result.exists())


        result_offer0nc = Offer.objects.filter(offer_tiepe=0,cleared=False)
        result_offer0c = Offer.objects.filter(offer_tiepe=0, cleared=True)
        result_offer1 = Offer.objects.filter(offer_tiepe=1)
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        log.info("result_offer0nc: {}".format( result_offer0nc))
        log.info("result_offer0c:{} ".format( result_offer0c))
        log.info("result_offer1:{} ".format( result_offer1))
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

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
        log.info("result_pstats".format(result_pstats))
        log.info("result_pstats2".format( result_pstats2))
        self.assertEqual(result_pstats.profit,12-Voucher.objects.get(auction=auction,idd=4).value_cum)
        self.assertEqual(result_pstats.vouchers_used, 4)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 12)
        self.assertEqual(result_pstats2.profit, -12)
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 4)
        self.assertEqual(result_pstats2.trading_result, -12)
        log.info("**********************************************")
        log.info("SUCCESS 10")
        log.info("**********************************************")



        def test_list_sell_on_buy_largerb(self):
            # MasterMan.invalidate_caches()
            experiment = Experiment.objects.get_or_create()[0]
            experiment.save()
            # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

            # 
            #
            auction, treatment = Auction.cache_or_create_auction()
            auction_id = auction.id
            period = Period.objects.get_or_create(idd=1, auction=auction)[0]
            phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
            user = User.objects.get_or_create()[0]
            user_id = user.id
            group = Group.objects.get_or_create(idd=1, auction=auction)[0]
            group_id = group.id
            # 

            player = Player.objects.get_or_create(user=user, auction=auction, group=group)[0]
            player.save()
            player_id = player.id
            p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group, period=period,role=1)[0]
            start = 0
            # Voucher.objects.values_list



            result = Offer.objects.all()
            log.info("result:{}".format( result))

            username = "u2"
            user2 = User.objects.create(username=username)
            user_id2 = user2.id
            player2 = Player.objects.get_or_create(user=user2, auction=auction, group=group)[0]
            player2.save()
            player_id2 = player2.id
            p_stats2 = Player_stats.objects.get_or_create(player=player2, auction=auction, group=group, period=period,role=2)[
                0]

            posedc_type = 0  # SELL
            postedc_quantity = 5
            postedc_price = 1

            posedc_type2 = 1  # BUY
            postedc_quantity2 = 4
            postedc_price2 = 3

            c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id2, posedc_type2, postedc_quantity2,
                                      postedc_price2, group_id, player2)
            c2.save()
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
            log.info("set_offer(request)")
            set_offer(request)

            result = Offer.objects.all()
            log.info("result:{}".format( result))

            # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

            result = Offer.objects.filter(cleared=False)
            log.info("result:{}".format( result))

            log.info("result = Offer.objects.all()".format( Offer.objects.all()))
            self.assertTrue(result.exists())

            result_offer0nc = Offer.objects.filter(offer_tiepe=0, cleared=False)
            result_offer0c = Offer.objects.filter(offer_tiepe=0, cleared=True)
            result_offer1 = Offer.objects.filter(offer_tiepe=1)
            # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
            log.info("result_offer0nc: {}".format( result_offer0nc))
            log.info("result_offer0c: {}".format( result_offer0c))
            log.info("result_offer1: {}".format( result_offer1))
            result_offer0nc = result_offer0nc[0]
            result_offer0c = result_offer0c[0]
            result_offer1 = result_offer1[0]

            self.assertEqual(result_offer0nc.offer_tiepe, 0)
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

            result_pstats = Player_stats.objects.get(auction=auction, group=group, period=period, player=player)
            result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player2)
            log.info("result_pstats".format( result_pstats))
            log.info("result_pstats2".format( result_pstats2))
            self.assertEqual(result_pstats.profit, 8- Voucher.objects.get(auction=auction,idd=4).value_cum)
            self.assertEqual(result_pstats.vouchers_used, 4)
            self.assertEqual(result_pstats.vouchers_negative, 0)
            self.assertEqual(result_pstats.trading_result, 12)
            self.assertEqual(result_pstats2.profit, -12 + treatment.retail_price*4)
            self.assertEqual(result_pstats2.vouchers_used, 0)
            self.assertEqual(result_pstats2.vouchers_negative, 4)
            self.assertEqual(result_pstats2.trading_result, -12)

            log.info("**********************************************")
            log.info("SUCCESS 10")
            log.info("**********************************************")



    def test_list_sell_on_buy_largerb2(self):
        # 
        # 
        # 
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        # 
        #
        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        # 

        player = Player.objects.get_or_create(user=user, auction=auction, group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group, period=period,role=1)[0]
        start = 0
        # Voucher.objects.values_list
        posedc_type = 0  # SELL
        postedc_quantity = 5
        postedc_price = 1

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

        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id2, posedc_type2, postedc_quantity2,postedc_price2, group_id, player2)
        c2.save()

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
        log.info("set_offer(request)")
        set_offer(request)

        result = Offer.objects.all()
        log.info("result:{}".format( result))

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.filter(cleared=False)
        log.info ("result:{}".format( result))
        self.assertFalse(result.exists())
        result_offer0 = Offer.objects.filter(offer_tiepe=0)
        result_offer1 = Offer.objects.filter(offer_tiepe=1)
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        log.info("result_offer0: {}".format( result_offer0))
        log.info("result_offer1: {}".format( result_offer1))
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
        log.info("result_pstats:{}".format(result_pstats))
        log.info("result_pstats2:{}".format( result_pstats2))
        self.assertEqual(result_pstats.profit, 5)
        self.assertEqual(result_pstats.vouchers_used, 0)
        self.assertEqual(result_pstats.vouchers_negative, 5)
        self.assertEqual(result_pstats.trading_result, 5)
        self.assertEqual(result_pstats2.profit, -5 )
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 5)
        self.assertEqual(result_pstats2.trading_result, -5)

        log.info("**********************************************")
        log.info("SUCCESS 11")
        log.info("**********************************************")


    def test_list_sell_on_buy_largerb(self):
        # 
        # 
        # 
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        #

        # 
        #
        auction, treatment =Auction.cache_or_create_auction()
        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        # 
        voucher_list = Voucher.objects.filter(auction=auction)
        log.info("voucher_list:{}".format(voucher_list))

        player = Player.objects.get_or_create(user=user, auction=auction, group=group)[0]
        player.save()
        player_id = player.id
        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group, period=period)[0]
        start = 0
        # Voucher.objects.values_list
        posedc_type = 0  # SELL
        postedc_quantity = 5
        postedc_price = 1

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

        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id2, posedc_type2, postedc_quantity2,postedc_price2, group_id, player2)
        c2.save()

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
        log.info("set_offer(request)")
        voucher_list = Voucher.objects.filter(auction=auction)
        log.info("voucher_list:{}".format(voucher_list))
        log.info("voucher_list_no:{}".format(voucher_list.count()))
        log.info("voucher_list_no:{}".format(voucher_list.count()))
        set_offer(request)

        result = Offer.objects.all()
        log.info("result:{}".format( result))

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)

        result = Offer.objects.filter(cleared=False)
        log.info ("result:{}".format( result))
        self.assertFalse(result.exists())
        result_offer0 = Offer.objects.filter(offer_tiepe=0)
        result_offer1 = Offer.objects.filter(offer_tiepe=1)
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        # log.info("result_offer0: ", result_offer0)
        # log.info("result_offer1: ", result_offer1)
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

        self.assertEqual(result_pstats.vouchers_used, 5)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 5)
        self.assertEqual(result_pstats.profit, 5- Voucher.objects.get(auction=auction,idd=5).value_cum)

        self.assertEqual(result_pstats2.profit, -5 )
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 5)
        self.assertEqual(result_pstats2.trading_result, -5)

        # log.info("result_pstats",result_pstats)
        # log.info("result_pstats2", result_pstats2)
        log.info("**********************************************")
        log.info("SUCCESS 11")
        log.info("**********************************************")


    def test_sell5on3buys15role0on0(self):
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        treatment.allow_multiple_offers= True
        treatment.save()

        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user_offer = User.objects.get_or_create()[0]
        user_offer_id = user_offer.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id

        voucher_list = Voucher.objects.filter(auction=auction)
        log.info("voucher_list:{}".format(voucher_list))
        log.info("voucher_list_no:{}".format(voucher_list.count()))

        player_offer = Player.objects.get_or_create(user=user_offer, auction=auction, group=group)[0]
        player_offer.save()
        player_offer_id = player_offer.id
        p_offer_stats = Player_stats.objects.get_or_create(player=player_offer, auction=auction, group=group, period=period)[0]
        start = 0
        # Voucher.objects.values_list
        posedc_type = 0  # SELL
        postedc_quantity = 5
        postedc_price = 1

        username = "u1"
        user1 = User.objects.get_or_create(username=username)[0]
        user1_id = user1.id

        player1 = Player.objects.get_or_create(user=user1, auction=auction, group=group)[0]
        player1.save()
        player_id1 = player1.id
        p1_stats = Player_stats.objects.get_or_create(player=player1, auction=auction, group=group, period=period)[0]

        posedc_type1 = 1  # BUY
        postedc_quantity1 = 15
        postedc_price1 = 1

        c1, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,postedc_price1, group_id, player1)
        c1.save()

        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,postedc_price1, group_id, player1)
        c2.save()

        c3, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,postedc_price1, group_id, player1)
        c3.save()

        log.info("")
        log.info("All offers now")
        offer_list= Offer.objects.all()
        for offer in offer_list:
            log.info("offer:{}".format(offer))
        log.info("")
        log.info("")
        self.assertTrue(offer_list.count() == 3)

        data = {}
        data['priceOriginal'] = postedc_price
        data['unitsOriginal'] = postedc_quantity
        data['Type'] = posedc_type
        data['auction_id'] = auction.id
        data['user_id'] = user_offer.id
        data['player_id'] = player_offer.id
        data['group_id'] = group.id

        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer
        log.info("set_offer(request)")
        import time
        start_time=time.time()
        set_offer(request)
        end_time = time.time()
        log.info("")
        log.info("total time:{}".format(end_time-start_time,3))
        log.info("")
        result = Offer.objects.all()
        log.info("result:{}".format( result))

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)


        result_offer0 = Offer.objects.filter(offer_tiepe=0).all()
        result_offer1 = Offer.objects.filter(offer_tiepe=1).all()
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        # log.info("result_offer0: ", result_offer0)
        # log.info("result_offer1: ", result_offer1)

        self.assertTrue(Offer.objects.filter(offer_tiepe=0,unitsAvailable=0,player=player_offer).all().count() ==1)
        self.assertTrue(Offer.objects.filter(offer_tiepe=1, unitsAvailable=0,player=player1).all().count() == 1)
        self.assertTrue(Offer.objects.filter(offer_tiepe=1, unitsAvailable=10, player=player1).all().count() == 1)


        result_pstats_offer = Player_stats.objects.get(auction=auction,group=group,period=period,player=player_offer)
        result_pstats1 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player1)
        log.info("result_pstats_offer:{}".format(result_pstats_offer))
        log.info("result_pstats1:{}".format(result_pstats1))

        self.assertEqual(result_pstats_offer.profit, 5- Voucher.objects.get(auction=auction, idd = 5).value_cum)
        self.assertEqual(result_pstats_offer.vouchers_used, 5)
        self.assertEqual(result_pstats_offer.vouchers_negative, 0)
        self.assertEqual(result_pstats_offer.trading_result, 5)
        self.assertEqual(result_pstats1.profit, -5 )
        self.assertEqual(result_pstats1.vouchers_used, 0)
        self.assertEqual(result_pstats1.vouchers_negative, 5)
        self.assertEqual(result_pstats1.trading_result, -5)

        log.info(f"result_pstats: {result_pstats_offer}")
        # log.info(f"result_pstats2: {result_pstats2}")
        log.info("**********************************************")
        log.info("SUCCESS 12")
        log.info("**********************************************")


    def test_sell5on3buys15role1on1b(self):
        # 


        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        treatment.allow_multiple_offers = True
        treatment.save_and_cache()

        


        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user_offer = User.objects.get_or_create()[0]
        user_offer_id = user_offer.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id

        voucher_list = Voucher.objects.filter(auction=auction)
        log.info("voucher_list:{}".format(voucher_list))
        log.info("voucher_list_no:{}".format(voucher_list.count()))

        player_offer = Player.objects.get_or_create(role=1,user=user_offer, auction=auction, group=group)[0]
        player_offer.save()
        player_offer_id = player_offer.id
        p_offer_stats = \
        Player_stats.objects.get_or_create(player=player_offer, auction=auction, group=group, period=period)[0]
        start = 0
        # Voucher.objects.values_list
        posedc_type = 0  # SELL
        postedc_quantity = 5
        postedc_price = 1

        username = "u1"
        user1 = User.objects.get_or_create(username=username)[0]
        user1_id = user1.id

        player1 = Player.objects.get_or_create(role=1,user=user1, auction=auction, group=group)[0]
        player1.save()
        player_id1 = player1.id
        p1_stats = Player_stats.objects.get_or_create(player=player1, auction=auction, group=group, period=period)[0]

        posedc_type1 = 1  # BUY
        postedc_quantity1 = 15
        postedc_price1 = 1

        c1, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c1.save()

        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c2.save()

        c3, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c3.save()

        log.info("")
        log.info("All offers now")
        offer_list = Offer.objects.all()
        for offer in offer_list:
            log.info("offer:{}".format(offer))
        log.info("")
        log.info("")
        self.assertTrue(offer_list.count() == 3)

        data = {}
        data['priceOriginal'] = postedc_price
        data['unitsOriginal'] = postedc_quantity
        data['Type'] = posedc_type
        data['auction_id'] = auction.id
        data['user_id'] = user_offer.id
        data['player_id'] = player_offer.id
        data['group_id'] = group.id

        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer
        log.info("set_offer(request)")
        import time
        start_time = time.time()
        set_offer(request)
        end_time = time.time()
        log.info("")
        log.info("total time:{}".format(end_time - start_time, 3))
        log.info("")
        result = Offer.objects.all()
        log.info("result:{} ".format( result))

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)


        result_offer0 = Offer.objects.filter(offer_tiepe=0).all()
        result_offer1 = Offer.objects.filter(offer_tiepe=1).all()
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        log.info("result_offer0:{}".format( result_offer0))
        log.info("result_offer1:{}".format( result_offer1))

        self.assertTrue(Offer.objects.filter(offer_tiepe=0, unitsAvailable=0, player=player_offer).all().count() == 1)
        self.assertTrue(Offer.objects.filter(offer_tiepe=1, unitsAvailable=0, player=player1).all().count() == 1)
        self.assertTrue(Offer.objects.filter(offer_tiepe=1, unitsAvailable=10, player=player1).all().count() == 1)

        result_pstats_offer = Player_stats.objects.get(auction=auction, group=group, period=period,
                                                          player=player_offer)
        result_pstats1 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player1)
        log.info("result_pstats_offer:{}".format(result_pstats_offer) )
        log.info("result_pstats1:{}".format(result_pstats1))
        log.info("result_pstats:{}".format( result_pstats_offer))
        log.info("result_pstats2:{}".format( result_pstats1))

        # self.assertEqual(result_pstats_offer.profit, -5 + 5 * treatment.retail_price)
        self.assertEqual(result_pstats_offer.profit, 5 - Voucher.objects.get(auction=auction, idd=5).value_cum)
        self.assertEqual(result_pstats_offer.vouchers_used, 5)
        self.assertEqual(result_pstats_offer.vouchers_negative, 0)
        self.assertEqual(result_pstats_offer.trading_result, 5)
        self.assertEqual(result_pstats1.profit, -5)
        self.assertEqual(result_pstats1.vouchers_used, 0)
        self.assertEqual(result_pstats1.vouchers_negative, 5)
        self.assertEqual(result_pstats1.trading_result, -5)

        log.info("**********************************************")
        log.info("SUCCESS 12")
        log.info("**********************************************")



    def test_sell5on3buys15role0on1(self):
        #
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()

        treatment.allow_multiple_offers = True
        treatment.save_and_cache()
        # MasterMan.cache_me('treatment', treatment)



        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user_offer = User.objects.get_or_create()[0]
        user_offer_id = user_offer.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id

        voucher_list = Voucher.objects.filter(auction=auction)
        log.info("voucher_list:{}".format(voucher_list))
        log.info("voucher_list_no:{}".format(voucher_list.count()))

        player_offer = Player.objects.get_or_create(role=0,user=user_offer, auction=auction, group=group)[0]
        player_offer.save()
        player_offer_id = player_offer.id
        p_offer_stats = \
        Player_stats.objects.get_or_create(player=player_offer, auction=auction, group=group, period=period)[0]
        start = 0
        # Voucher.objects.values_list
        posedc_type = 0  # SELL
        postedc_quantity = 5
        postedc_price = 1

        username = "u1"
        user1 = User.objects.get_or_create(username=username)[0]
        user1_id = user1.id

        player1 = Player.objects.get_or_create(role=1,user=user1, auction=auction, group=group)[0]
        player1.save()
        player_id1 = player1.id
        p1_stats = Player_stats.objects.get_or_create(player=player1, auction=auction, group=group, period=period)[0]

        posedc_type1 = 1  # BUY
        postedc_quantity1 = 15
        postedc_price1 = 1

        c1, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c1.save()

        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c2.save()

        c3, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c3.save()

        log.info("")
        log.info("All offers now")
        offer_list = Offer.objects.all()
        for offer in offer_list:
            log.info("offer:{}".format(offer))
        log.info("")
        log.info("")
        self.assertTrue(offer_list.count() == 3)

        data = {}
        data['priceOriginal'] = postedc_price
        data['unitsOriginal'] = postedc_quantity
        data['Type'] = posedc_type
        data['auction_id'] = auction.id
        data['user_id'] = user_offer.id
        data['player_id'] = player_offer.id
        data['group_id'] = group.id

        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer
        log.info("set_offer(request)")
        import time
        start_time = time.time()
        set_offer(request)
        end_time = time.time()
        log.info("")
        log.info("total time:{}".format(end_time - start_time, 3))
        log.info("")
        result = Offer.objects.all()
        log.info("result:{}".format( result))

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)


        result_offer0 = Offer.objects.filter(offer_tiepe=0).all()
        result_offer1 = Offer.objects.filter(offer_tiepe=1).all()
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        log.info("result_offer0:{} ".format( result_offer0))
        log.info("result_offer1:{} ".format( result_offer1))

        self.assertTrue(Offer.objects.filter(offer_tiepe=0, unitsAvailable=0, player=player_offer).all().count() == 1)
        self.assertTrue(Offer.objects.filter(offer_tiepe=1, unitsAvailable=0, player=player1).all().count() == 1)
        self.assertTrue(Offer.objects.filter(offer_tiepe=1, unitsAvailable=10, player=player1).all().count() == 1)

        result_pstats_offer = Player_stats.objects.get(auction=auction, group=group, period=period,
                                                          player=player_offer)
        result_pstats1 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player1)

        log.info("result_pstats:{}".format( result_pstats_offer))
        log.info("result_pstats2:{}".format( result_pstats1))

        # self.assertEqual(result_pstats_offer.profit, 0)
        self.assertEqual(result_pstats_offer.profit, 5 - Voucher.objects.get(auction=auction, idd=5).value_cum)
        self.assertEqual(result_pstats_offer.vouchers_used, 5)
        self.assertEqual(result_pstats_offer.vouchers_negative, 0)
        self.assertEqual(result_pstats_offer.trading_result, 5)
        self.assertEqual(result_pstats1.profit, -5)
        self.assertEqual(result_pstats1.vouchers_used, 0)
        self.assertEqual(result_pstats1.vouchers_negative, 5)
        self.assertEqual(result_pstats1.trading_result, -5)

        log.info("**********************************************")
        log.info("SUCCESS 12")
        log.info("**********************************************")


    def test_list_1sell5_on_3buys15_role_1_on_0(self):
        t=TestCase()


        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        treatment.allow_multiple_offers = True
        treatment.save()
        # MasterMan.cache_me('treatment', treatment)



        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user_offer = User.objects.get_or_create()[0]
        user_offer_id = user_offer.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id

        voucher_list = Voucher.objects.filter(auction=auction)
        log.info("voucher_list:{}".format(voucher_list))
        log.info("voucher_list_no:{}".format(voucher_list.count()))

        player_offer = Player.objects.get_or_create(role=1,user=user_offer, auction=auction, group=group)[0]
        player_offer.save()
        player_offer_id = player_offer.id
        p_offer_stats = Player_stats.objects.get_or_create(player=player_offer, auction=auction, group=group, period=period)[0]
        start = 0
        # Voucher.objects.values_list
        posedc_type = 0  # SELL
        postedc_quantity = 5
        postedc_price = 1

        username = "u1"
        user1 = User.objects.get_or_create(username=username)[0]
        user1_id = user1.id

        player1 = Player.objects.get_or_create(role=0,user=user1, auction=auction, group=group)[0]
        player1.save()
        player_id1 = player1.id
        p1_stats = Player_stats.objects.get_or_create(player=player1, auction=auction, group=group, period=period)[0]

        posedc_type1 = 1  # BUY
        postedc_quantity1 = 15
        postedc_price1 = 1

        c1, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c1.save()

        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c2.save()

        c3, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c3.save()

        log.info("")
        log.info("All offers now")
        offer_list = Offer.objects.all()
        for offer in offer_list:
            log.info("offer:{}".format(offer))
        log.info("")
        log.info("")
        self.assertTrue(offer_list.count() == 3)

        data = {}
        data['priceOriginal'] = postedc_price
        data['unitsOriginal'] = postedc_quantity
        data['Type'] = posedc_type
        data['auction_id'] = auction.id
        data['user_id'] = user_offer.id
        data['player_id'] = player_offer.id
        data['group_id'] = group.id

        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer
        log.info("set_offer(request)")
        import time
        start_time = time.time()
        set_offer(request)
        end_time = time.time()
        log.info("")
        log.info("total time:{}".format(end_time - start_time, 3))
        log.info("")
        result = Offer.objects.all()
        log.info("result:{}".format( result))

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)


        result_offer0 = Offer.objects.filter(offer_tiepe=0).all()
        result_offer1 = Offer.objects.filter(offer_tiepe=1).all()
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        log.info("result_offer0:{}".format( result_offer0))
        log.info("result_offer1:{}".format(result_offer1))

        self.assertTrue(Offer.objects.filter(offer_tiepe=0, unitsAvailable=0, player=player_offer).all().count() == 1)
        self.assertTrue(Offer.objects.filter(offer_tiepe=1, unitsAvailable=0, player=player1).all().count() == 1)
        self.assertTrue(Offer.objects.filter(offer_tiepe=1, unitsAvailable=10, player=player1).all().count() == 1)

        result_pstats_offer = Player_stats.objects.get(auction=auction, group=group, period=period,
                                                          player=player_offer)
        result_pstats1 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player1)
        log.info("result_pstats:{}".format( result_pstats_offer))
        log.info("result_pstats2:{}".format( result_pstats1))

        # self.assertEqual(result_pstats_offer.profit, 0)
        self.assertEqual(result_pstats_offer.profit, 5 - Voucher.objects.get(auction=auction, idd=5).value_cum)
        self.assertEqual(result_pstats_offer.vouchers_used, 5)
        self.assertEqual(result_pstats_offer.vouchers_negative, 0)
        self.assertEqual(result_pstats_offer.trading_result, 5)
        self.assertEqual(result_pstats1.profit, -5)
        self.assertEqual(result_pstats1.vouchers_used, 0)
        self.assertEqual(result_pstats1.vouchers_negative, 5)
        self.assertEqual(result_pstats1.trading_result, -5)

        log.info("**********************************************")
        log.info("SUCCESS 12")
        log.info("**********************************************")


    def test_list1sell5on3buys2_role_1_on_0(self):
        t=TestCase()

        MasterMan.invalidate_caches()
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        treatment.allow_multiple_offers = True
        treatment.save()
        # MasterMan.cache_me('treatment', treatment)



        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user_offer = User.objects.get_or_create()[0]
        user_offer_id = user_offer.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id

        voucher_list = Voucher.objects.filter(auction=auction)
        log.info("voucher_list:{}".format(voucher_list))
        log.info("voucher_list_no:{}".format(voucher_list.count()))

        player_offer = Player.objects.get_or_create(role=1,user=user_offer, auction=auction, group=group)[0]
        player_offer.save()
        player_offer_id = player_offer.id
        p_offer_stats = Player_stats.objects.get_or_create(player=player_offer, auction=auction, group=group, period=period)[0]
        start = 0
        # Voucher.objects.values_list
        posedc_type = 0  # SELL
        postedc_quantity = 5
        postedc_price = 1

        username = "u1"
        user1 = User.objects.get_or_create(username=username)[0]
        user1_id = user1.id

        player1 = Player.objects.get_or_create(role=0,user=user1, auction=auction, group=group)[0]
        player1.save()
        player_id1 = player1.id
        p1_stats = Player_stats.objects.get_or_create(player=player1, auction=auction, group=group, period=period)[0]

        posedc_type1 = 1  # BUY
        postedc_quantity1 = 2
        postedc_price1 = 1

        c1, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c1.save()

        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c2.save()

        c3, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1, postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c3.save()

        log.info("")
        log.info("All offers now")
        offer_list = Offer.objects.all()
        for offer in offer_list:
            log.info("offer:{}".format(offer))
        log.info("")
        log.info("")
        self.assertTrue(offer_list.count() == 3)

        data = {}
        data['priceOriginal'] = postedc_price
        data['unitsOriginal'] = postedc_quantity
        data['Type'] = posedc_type
        data['auction_id'] = auction.id
        data['user_id'] = user_offer.id
        data['player_id'] = player_offer.id
        data['group_id'] = group.id

        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer
        log.info("set_offer(request)")
        import time
        start_time = time.time()
        set_offer(request)
        end_time = time.time()
        log.info("")
        log.info("total time:{}".format(end_time - start_time, 3))
        log.info("")
        result = Offer.objects.all()
        log.info("result:{} ".format( result))

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)


        result_offer0 = Offer.objects.filter(offer_tiepe=0).all()
        result_offer1 = Offer.objects.filter(offer_tiepe=1).all()
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        log.info("result_offer0: {}".format( result_offer0))
        log.info("result_offer1: {}".format( result_offer1))

        self.assertTrue(Offer.objects.filter(offer_tiepe=0, unitsAvailable=0, unitsCleared=1,player=player_offer).all().count() == 1)
        self.assertTrue(Offer.objects.filter(offer_tiepe=0, unitsAvailable=0, unitsCleared=2,
                                             player=player_offer).all().count() == 2)
        self.assertTrue(Offer.objects.filter(offer_tiepe=1, unitsAvailable=0, unitsCleared=2,player=player1).all().count() == 2)
        self.assertTrue(
            Offer.objects.filter(offer_tiepe=1, unitsAvailable=0, unitsCleared=1, player=player1).all().count() == 1)
        self.assertTrue(Offer.objects.filter(offer_tiepe=1, unitsAvailable=1, unitsCleared=0, player=player1).all().count() == 1)

        result_pstats_offer = Player_stats.objects.get(auction=auction, group=group, period=period,
                                                          player=player_offer)
        result_pstats1 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player1)
        log.info("result_pstats:{}".format( result_pstats_offer))
        log.info("result_pstats2:{}".format( result_pstats1))

        self.assertEqual(result_pstats_offer.profit, 5- Voucher.objects.get(auction=auction, idd=5).value_cum)
        self.assertEqual(result_pstats_offer.vouchers_used, 5)
        self.assertEqual(result_pstats_offer.vouchers_negative, 0)
        self.assertEqual(result_pstats_offer.trading_result, 5)
        self.assertEqual(result_pstats1.profit, -5)
        self.assertEqual(result_pstats1.vouchers_used, 0)
        self.assertEqual(result_pstats1.vouchers_negative, 5)
        self.assertEqual(result_pstats1.trading_result, -5)

        log.info("**********************************************")
        log.info("SUCCESS 12")
        log.info("**********************************************")


    def test_list1sell5on3buys5_role_1_on_0b(self):
        MasterMan.invalidate_caches()
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        treatment.allow_multiple_offers = True
        treatment.save()
        # MasterMan.cache_me('treatment', treatment)



        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user_offer = User.objects.get_or_create()[0]
        user_offer_id = user_offer.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id

        voucher_list = Voucher.objects.filter(auction=auction)
        log.info("voucher_list:{}".format(voucher_list))
        log.info("voucher_list_no:{}".format(voucher_list.count()))

        player_offer = Player.objects.get_or_create(role=1, user=user_offer, auction=auction, group=group)[0]
        player_offer.save()
        player_offer_id = player_offer.id
        p_offer_stats = \
        Player_stats.objects.get_or_create(player=player_offer, auction=auction, group=group, period=period)[0]
        start = 0
        # Voucher.objects.values_list
        posedc_type = 0  # SELL
        postedc_quantity = 5
        postedc_price = 1

        username = "u1"
        user1 = User.objects.get_or_create(username=username)[0]
        user1_id = user1.id

        player1 = Player.objects.get_or_create(role=0, user=user1, auction=auction, group=group)[0]
        player1.save()
        player_id1 = player1.id
        p1_stats = Player_stats.objects.get_or_create(player=player1, auction=auction, group=group, period=period)[
            0]

        posedc_type1 = 1  # BUY
        postedc_quantity1 = 5
        postedc_price1 = 1

        c1, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1,
                                  postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c1.save()

        c2, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1,
                                  postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c2.save()

        c3, reuse, cc = Offer.create_present_offer(treatment, auction_id, phase, player_id1, posedc_type1,
                                  postedc_quantity1,
                                  postedc_price1, group_id, player1)
        c3.save()

        log.info("")
        log.info("All offers now")
        offer_list = Offer.objects.all()
        for offer in offer_list:
            log.info("offer:{}".format(offer))
        log.info("")
        log.info("")
        self.assertTrue(offer_list.count() == 3)

        data = {}
        data['priceOriginal'] = postedc_price
        data['unitsOriginal'] = postedc_quantity
        data['Type'] = posedc_type
        data['auction_id'] = auction.id
        data['user_id'] = user_offer.id
        data['player_id'] = player_offer.id
        data['group_id'] = group.id

        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer
        log.info("set_offer(request)")
        import time
        start_time = time.time()
        set_offer(request)
        end_time = time.time()
        log.info("")
        log.info("total time:{}".format(end_time - start_time, 3))
        log.info("")
        result = Offer.objects.all()
        log.info("result: ".format( result))

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)


        result_offer0 = Offer.objects.filter(offer_tiepe=0).all()
        result_offer1 = Offer.objects.filter(offer_tiepe=1).all()
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        log.info("result_offer0: ".format( result_offer0))
        log.info("result_offer1: ".format( result_offer1))

        self.assertTrue(Offer.objects.filter(offer_tiepe=0, unitsAvailable=0, unitsCleared=5,
                                             player=player_offer).all().count() == 1)
        self.assertTrue(Offer.objects.filter(offer_tiepe=1, unitsAvailable=0, unitsCleared=5,
                                             player=player1).all().count() == 1)
        self.assertTrue(
            Offer.objects.filter(offer_tiepe=1, unitsAvailable=5, unitsCleared=0,
                                 player=player1).all().count() == 2)
        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player_offer)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player1)
        log.info("result_pstats".format(result_pstats))
        log.info("result_pstats2".format( result_pstats2))
        # self.assertEqual(result_pstats.profit, 0)
        self.assertEqual(result_pstats.profit, 5 - Voucher.objects.get(auction=auction, idd=5).value_cum)
        self.assertEqual(result_pstats.vouchers_used, 5)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 5)
        self.assertEqual(result_pstats2.profit, -5 )
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 5)
        self.assertEqual(result_pstats2.trading_result, -5)

        log.info("**********************************************")
        log.info("SUCCESS 12")
        log.info("**********************************************")


    def test_list1sell2onbuys60_role_0_on_1(self):
        MasterMan.invalidate_caches()
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()

        auction, treatment = Auction.cache_or_create_auction()
        treatment.allow_multiple_offers = True
        treatment.time_for_succession = 0
        treatment.save_and_cache()
        # MasterMan.cache_me('treatment', treatment)



        # auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        username = "u2"
        user_offer = User.objects.get_or_create(username=username)[0]
        username = "u3"
        user_offer2 = User.objects.get_or_create(username=username)[0]
        username = "u4"
        user_offer3 = User.objects.get_or_create(username=username)[0]
        username = "u5"
        user_offer4 = User.objects.get_or_create(username=username)[0]
        username = "u6"
        user_offer5 = User.objects.get_or_create(username=username)[0]

        user_list= User.objects.all()
        self.assertTrue(user_list.count()==5)

        group = Group.objects.get_or_create(idd=1, auction=auction)[0]


        voucher_list = Voucher.objects.filter(auction=auction)
        log.info("voucher_list:{}".format(voucher_list))
        log.info("voucher_list_no:{}".format(voucher_list.count()))

        player_offer = Player.objects.get_or_create(role=1, user=user_offer, auction=auction, group=group)[0]
        player_offer2 = Player.objects.get_or_create(role=1, user=user_offer2, auction=auction, group=group)[0]
        player_offer3 = Player.objects.get_or_create(role=1, user=user_offer3, auction=auction, group=group)[0]
        player_offer4 = Player.objects.get_or_create(role=1, user=user_offer4, auction=auction, group=group)[0]
        player_offer5 = Player.objects.get_or_create(role=1, user=user_offer5, auction=auction, group=group)[0]

        player_offer.save()
        player_offer2.save()
        player_offer3.save()
        player_offer4.save()
        player_offer5.save()
        player_offer_id = player_offer.id
        p_offer_stats = Player_stats.objects.get_or_create(player=player_offer, auction=auction, group=group, period=period,player_demand=120)[0]
        p_offer_stats.save()
        p_offer_stats2 = Player_stats.objects.get_or_create(player=player_offer2, auction=auction, group=group, period=period,player_demand=120)[0]
        p_offer_stats2.save()
        p_offer_stats3 = \
        Player_stats.objects.get_or_create(player=player_offer3, auction=auction, group=group, period=period,player_demand=120)[0]
        p_offer_stats3.save()
        p_offer_stats4 = Player_stats.objects.get_or_create(player=player_offer4, auction=auction, group=group, period=period,player_demand=120)[0]
        p_offer_stats4.save()
        p_offer_stats5 = Player_stats.objects.get_or_create(player=player_offer5, auction=auction, group=group, period=period,player_demand=120)[0]
        p_offer_stats5.save()

        start = 0
        # Voucher.objects.values_list
        posedc_type = 0  # SELL
        postedc_quantity = 2
        postedc_price = 1

        username = "u1"
        user1 = User.objects.get_or_create(username=username)[0]
        user1_id = user1.id

        player1 = Player.objects.get_or_create(role=1, user=user1, auction=auction, group=group)[0]
        player1.save()
        player_id1 = player1.id
        p1_stats = Player_stats.objects.get_or_create(player=player1, auction=auction, group=group, period=period, role=player1.role,player_demand=120)[
            0]

        posedc_type1 = 1  # BUY
        postedc_quantity1 = 3
        postedc_price1 = 1

        from django_bulk_update.helper import bulk_update
        to_insert = []
        for i in range(40):
            c1 = Offer(auction=auction,group=group,player=player1,  phase=phase,offer_tiepe=posedc_type1, unitsAvailable= postedc_quantity1, priceOriginal=postedc_price1 ,cleared=False)
            to_insert.append(c1)
        msg = Offer.objects.bulk_create(to_insert)

        log.info("")
        log.info("All offers now")
        offer_list = Offer.objects.all()
        for offer in offer_list:
            log.info("offer:{}".format(offer))
        log.info("")
        log.info("")
        self.assertTrue(offer_list.count() == 40)

        data = {}
        data['priceOriginal'] = postedc_price
        data['unitsOriginal'] = postedc_quantity
        data['Type'] = posedc_type
        data['auction_id'] = auction.id
        data['user_id'] = user_offer.id
        data['player_id'] = player_offer.id
        data['group_id'] = group.id

        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer
        log.info("set_offer(request)")

        import time
        from django.conf import settings
        settings.DEBUG = False
        from django.db import connection
        start_time = time.time()

        # print("players:{}".format(Player.objects.filter(auction=auction).all()))
        player_list = Player.objects.filter(auction=auction).all()
        # for pl in player_list:
        #     print("pl:{}".format(pl))
        for i in range(16):
            set_offer(request)

        data['user_id'] = user_offer2.id
        data['player_id'] = player_offer2.id
        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer2
        for i in range(16):
            set_offer(request)
        data['user_id'] = user_offer3.id
        data['player_id'] = player_offer3.id
        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer3
        for i in range(16):
            set_offer(request)

        data['user_id'] = user_offer4.id
        data['player_id'] = player_offer4.id
        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer4
        for i in range(16):
            set_offer(request)

        data['user_id'] = user_offer5.id
        data['player_id'] = player_offer5.id
        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer5
        for i in range(16):
            set_offer(request)

        end_time = time.time()
        log.info("")
        log.info("")
        log.info("avg time:{}".format((end_time - start_time)/(5*16), 3))
        # self.assertEqual((end_time - start_time)/(5*16),0)
        log.info("len(connection.queries)")
        log.info(len(connection.queries))

        result = Offer.objects.all()
        log.info("result: ".format( result))
        log.info("")
        log.info("")

        # log.info(connection.queries)

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)


        result_offer0 = Offer.objects.filter(offer_tiepe=0).all()
        result_offer1 = Offer.objects.filter(offer_tiepe=1).all()
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        log.info("result_offer0: ".format( result_offer0))
        log.info("result_offer1: ".format( result_offer1))

        log.info("result_offer0.all().count():{}".format(
            result_offer0.all().count()))
        log.info("result_offer0.filter(unitsAvailable=0,unitsCleared=2).count():{}".format(result_offer0.filter(unitsAvailable=0,unitsCleared=2).count()))
        log.info("result_offer0.filter(unitsAvailable=0,unitsCleared=1).count():{}".format(
            result_offer0.filter(unitsAvailable=0, unitsCleared=1).count()))

        self.assertEqual(Offer.objects.filter(offer_tiepe=0, unitsAvailable=0, unitsCleared=2).all().count() , 40)
        self.assertEqual(Offer.objects.filter(offer_tiepe=1, unitsAvailable=0, unitsCleared=1).all().count() , 40)

        log.info("result_offer1.all().count():{}".format(
            result_offer1.all().count()))
        log.info("result_offer1.filter(unitsAvailable=0,unitsCleared=2).count():{}".format(
            result_offer1.filter(unitsAvailable=0, unitsCleared=2).count()))
        log.info("result_offer1.filter(unitsAvailable=0,unitsCleared=1).count():{}".format(
            result_offer1.filter(unitsAvailable=0, unitsCleared=1).count()))

        self.assertEqual(result_offer1.all().count(),80)
        self.assertEqual(result_offer1.filter(unitsAvailable=0, unitsCleared=2).count() , 40)
        self.assertEqual(result_offer1.filter(unitsAvailable=0, unitsCleared=1).count() , 40)

        result_pstats = Player_stats.objects.get(auction=auction,group=group,period=period,player=player_offer)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player1)
        log.info("result_pstats".format(result_pstats))
        log.info("result_pstats2".format( result_pstats2))
        self.assertEqual(result_pstats.profit, 32- Voucher.objects.get(auction=auction, idd=32).value_cum)

        self.assertEqual(result_pstats.vouchers_used, 32)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 32)
        self.assertEqual(result_pstats2.profit, 120 * treatment.retail_price - 120)
        self.assertEqual(result_pstats2.vouchers_used, 120)
        self.assertEqual(result_pstats2.vouchers_negative, 0)
        self.assertEqual(result_pstats2.trading_result, -120)


        log.info("**********************************************")
        log.info("SUCCESS 12")
        log.info("**********************************************")

    def test_list1sell2onbuys60_role_0_on_1b(self):
        MasterMan.invalidate_caches()
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        treatment.allow_multiple_offers = True
        treatment.time_for_succession = 0
        print("before treatmentsave")
        treatment.save()
        print("after treatmentsave")
        # MasterMan.cache_me('treatment', treatment)




        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        username = "u2"
        user_offer = User.objects.get_or_create(username=username)[0]
        username = "u3"
        user_offer2 = User.objects.get_or_create(username=username)[0]
        username = "u4"
        user_offer3 = User.objects.get_or_create(username=username)[0]
        username = "u5"
        user_offer4 = User.objects.get_or_create(username=username)[0]
        username = "u6"
        user_offer5 = User.objects.get_or_create(username=username)[0]

        user_list = User.objects.all()
        self.assertTrue(user_list.count() == 5)

        group = Group.objects.get_or_create(idd=1, auction=auction)[0]


        voucher_list = Voucher.objects.filter(auction=auction)
        log.info("voucher_list:{}".format(voucher_list))
        log.info("voucher_list_no:{}".format(voucher_list.count()))

        player_offer = Player.objects.get_or_create(role=1, user=user_offer, auction=auction, group=group)[0]
        player_offer2 = Player.objects.get_or_create(role=1, user=user_offer2, auction=auction, group=group)[0]
        player_offer3 = Player.objects.get_or_create(role=1, user=user_offer3, auction=auction, group=group)[0]
        player_offer4 = Player.objects.get_or_create(role=1, user=user_offer4, auction=auction, group=group)[0]
        player_offer5 = Player.objects.get_or_create(role=1, user=user_offer5, auction=auction, group=group)[0]

        player_offer.save()
        player_offer2.save()
        player_offer3.save()
        player_offer4.save()
        player_offer5.save()
        player_offer_id = player_offer.id
        p_offer_stats = \
        Player_stats.objects.get_or_create(player=player_offer, auction=auction, group=group, period=period)[0]
        p_offer_stats.save()
        p_offer_stats2 = \
        Player_stats.objects.get_or_create(player=player_offer2, auction=auction, group=group, period=period)[0]
        p_offer_stats2.save()
        p_offer_stats3 = \
            Player_stats.objects.get_or_create(player=player_offer3, auction=auction, group=group, period=period)[0]
        p_offer_stats3.save()
        p_offer_stats4 = \
        Player_stats.objects.get_or_create(player=player_offer4, auction=auction, group=group, period=period)[0]
        p_offer_stats4.save()
        p_offer_stats5 = \
        Player_stats.objects.get_or_create(player=player_offer5, auction=auction, group=group, period=period)[0]
        p_offer_stats5.save()

        start = 0
        # Voucher.objects.values_list
        posedc_type = 0  # SELL
        postedc_quantity = 17
        postedc_price = 3

        username = "u1"
        user1 = User.objects.get_or_create(username=username)[0]
        user1_id = user1.id

        player1 = Player.objects.get_or_create(role=1, user=user1, auction=auction, group=group)[0]
        player1.save()
        player_id1 = player1.id
        p1_stats = Player_stats.objects.get_or_create(player=player1, auction=auction, group=group, period=period,role=player1.role)[0]

        posedc_type1 = 1  # BUY
        postedc_quantity1 = 3
        postedc_price1 = 10

        from django_bulk_update.helper import bulk_update
        to_insert = []
        for i in range(40):
            c1 = Offer(auction=auction, group=group, player=player1, phase=phase, offer_tiepe=posedc_type1,
                       unitsAvailable=postedc_quantity1, priceOriginal=postedc_price1, cleared=False)
            to_insert.append(c1)
        msg = Offer.objects.bulk_create(to_insert)

        log.info("")
        log.info("All offers now")
        offer_list = Offer.objects.all()
        for offer in offer_list:
            log.info("offer:{}".format(offer))
        log.info("")
        log.info("")
        self.assertTrue(offer_list.count() == 40)

        data = {}
        data['priceOriginal'] = postedc_price
        data['unitsOriginal'] = postedc_quantity
        data['Type'] = posedc_type
        data['auction_id'] = auction.id
        data['user_id'] = user_offer.id
        data['player_id'] = player_offer.id
        data['group_id'] = group.id

        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer
        log.info("set_offer(request)")

        import time
        from django.conf import settings
        settings.DEBUG = False
        from django.db import connection
        start_time = time.time()
        for i in range(2):
            set_offer(request)

        data['user_id'] = user_offer2.id
        data['player_id'] = player_offer2.id
        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer2
        for i in range(2):
            set_offer(request)
        data['user_id'] = user_offer3.id
        data['player_id'] = player_offer3.id
        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer3
        for i in range(2):
            set_offer(request)

        data['user_id'] = user_offer4.id
        data['player_id'] = player_offer4.id
        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer4
        for i in range(2):
            set_offer(request)

        data['user_id'] = user_offer5.id
        data['player_id'] = player_offer5.id
        self.factory = RequestFactory()
        request = self.factory.post('/', data)
        request.user = user_offer5
        for i in range(16):
            set_offer(request)

        end_time = time.time()
        log.info("")
        log.info("")
        log.info("avg time:{}".format((end_time - start_time) / (5 * 2), 3))
        # self.assertEqual((end_time - start_time) / (5 * 16), 0)
        # self.assertTrue(False)
        log.info("len(connection.queries)")
        log.info(len(connection.queries))

        result = Offer.objects.all()
        log.info("result: {}".format( result))
        log.info("")
        log.info("")

        # log.info(connection.queries)

        # set_offer_nr(auction, auction_id, group_id, player, player_id, user_id, p_stats, posedc_type, postedc_quantity,postedc_price, period, phase, start)


        result_offer0 = Offer.objects.filter(offer_tiepe=0).all()
        result_offer1 = Offer.objects.filter(offer_tiepe=1).all()
        # log.info("result_offer: ", result_offer,result_offer.role,result_offer.priceOriginal,result_offer.unitsAvailable)
        log.info("result_offer0: {}".format( result_offer0))
        log.info("result_offer1: {}".format( result_offer1))

        log.info("result_offer0.all().count():{}".format(
            result_offer0.all().count()))

        log.info("result_offer1.filter(unitsAvailable=3).count():{}".format(
            result_offer1.filter(unitsAvailable=3).count()))

        log.info("result_offer1.filter(unitsAvailable=3, unitsCleared=3).count():{}".format(
            result_offer1.filter(unitsAvailable=3, unitsCleared=2).count()))
        log.info("result_offer1.filter(unitsAvailable=3, unitsCleared=1).count():{}".format(
            result_offer1.filter(unitsAvailable=3, unitsCleared=1).count()))

        self.assertEqual(Offer.objects.filter(offer_tiepe=0).all().count(), 0)


        self.assertEqual(Offer.objects.filter(offer_tiepe=1, unitsAvailable=0).all().count() , 0)
        self.assertEqual(Offer.objects.filter(offer_tiepe=1, unitsAvailable=3).all().count(), 40)
        log.info("result_offer1.all().count():{}".format(
            result_offer1.all().count()))
        log.info("result_offer1.filter(unitsAvailable=0,unitsCleared=2).count():{}".format(
            result_offer1.filter(unitsAvailable=0, unitsCleared=2).count()))
        log.info("result_offer1.filter(unitsAvailable=0,unitsCleared=1).count():{}".format(
            result_offer1.filter(unitsAvailable=0, unitsCleared=1).count()))

        self.assertEqual(result_offer1.all().count() , 40)
        self.assertEqual(result_offer1.filter(unitsAvailable=3).count() , 40)
        self.assertEqual(result_offer1.filter(unitsAvailable=0, unitsCleared=1).count(), 0)

        result_pstats = Player_stats.objects.get(auction=auction, group=group, period=period, player=player_offer)
        result_pstats2 = Player_stats.objects.get(auction=auction, group=group, period=period, player=player1)
        log.info("result_pstats:{}".format( result_pstats))
        log.info("result_pstats2:{}".format( result_pstats2))
        self.assertEqual(result_pstats.profit, 0)
        self.assertEqual(result_pstats.vouchers_used, 0)
        self.assertEqual(result_pstats.vouchers_negative, 0)
        self.assertEqual(result_pstats.trading_result, 0)
        self.assertEqual(result_pstats2.profit, 0)
        self.assertEqual(result_pstats2.vouchers_used, 0)
        self.assertEqual(result_pstats2.vouchers_negative, 0)
        self.assertEqual(result_pstats2.trading_result, 0)


        log.info("*******m***************************************")
        log.info("SUCCESS 12")
        log.info("**********************************************")