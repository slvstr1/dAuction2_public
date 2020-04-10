# import mock
import logging
from django.test import TestCase, RequestFactory
from forward_and_spot.models import Offer, Auction, Player, Group, Player_stats, Period, Phase, Treatment, Voucher
from forward_and_spot.views import  has_enough_vouchers, is_not_too_short_on_vouchers, is_using_vouchers, offer_was_made_just_before, must_wait_set
from forward_and_spot.functions import get_value_cum_RE, get_value_cum_PR, cv_STAND, cv_REV, set_products
from dAuction2.models import Experiment
from dAuction2.models import User
from master.models import MasterMan
from distribution.models import Distribution
from testing.models import Question
from django.db.models import Avg,StdDev
# from .views import set_offer
# from master.functions_main import createVoucher

# from mock import patch
log = logging.getLogger(__name__)


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
    # Timer.objects.all().delete()
    Distribution.objects.all().delete()
    User.objects.all().delete()
    Auction.objects.all().delete()


class functions_in_FS_views(TestCase):
    # def setUp(self):
    #     self
    def setUp(self):
        print("+"*40)
        print("setUp_" * 40)
        print("+" * 40)

    # @patch('set_offer')
    def test_is_using_vouchers(self):

        self.assertTrue(is_using_vouchers(Player.RE, Offer.BUY))
        self.assertTrue(is_using_vouchers(Player.PR, Offer.SELL))
        self.assertFalse(is_using_vouchers(Player.RE, Offer.SELL))
        self.assertFalse(is_using_vouchers(Player.PR, Offer.BUY))

    def test_has_enough_vouchers(self):
        self.assertTrue(has_enough_vouchers(max_vouchers=35, postedc_quantity=10, vouchers_used=10))
        self.assertTrue(
            has_enough_vouchers(max_vouchers=35, postedc_quantity=10, vouchers_used=25))
        self.assertFalse(
            has_enough_vouchers(max_vouchers=35, postedc_quantity=11, vouchers_used=25))
        self.assertFalse(
            has_enough_vouchers(max_vouchers=35, postedc_quantity=10, vouchers_used=26))
        self.assertFalse(
            has_enough_vouchers(max_vouchers=35, postedc_quantity=10, vouchers_used=26))
        self.assertFalse(
            has_enough_vouchers(max_vouchers=35, postedc_quantity=10, vouchers_used=26))
        self.assertTrue(
            has_enough_vouchers(max_vouchers=35, postedc_quantity=11, vouchers_used=24))
        self.assertTrue(
            has_enough_vouchers(max_vouchers=35, postedc_quantity=11, vouchers_used=24))
        self.assertTrue(
            has_enough_vouchers(max_vouchers=35, postedc_quantity=10, vouchers_used=10))
        self.assertFalse(
            has_enough_vouchers(max_vouchers=35, postedc_quantity=36, vouchers_used=10))
        self.assertFalse(
            has_enough_vouchers(max_vouchers=35, postedc_quantity=10, vouchers_used=36))
        self.assertFalse(
            has_enough_vouchers(max_vouchers=35, postedc_quantity=35, vouchers_used=10))
        self.assertFalse(
            has_enough_vouchers(max_vouchers=35, postedc_quantity=10, vouchers_used=35))
        self.assertFalse(
            has_enough_vouchers(max_vouchers=35, postedc_quantity=40, vouchers_used=10))
        self.assertFalse(
            has_enough_vouchers(max_vouchers=35, postedc_quantity=10, vouchers_used=40))


    def test_is_not_too_short_on_vouchers(self):
        self.assertTrue(is_not_too_short_on_vouchers(short_maximum=10,postedc_quantity=5,vouchers_negative=2))
        self.assertTrue(is_not_too_short_on_vouchers(short_maximum=10, postedc_quantity=2, vouchers_negative=5))
        self.assertTrue(is_not_too_short_on_vouchers(short_maximum=10, postedc_quantity=5, vouchers_negative=5))
        self.assertTrue(is_not_too_short_on_vouchers(short_maximum=10, postedc_quantity=5, vouchers_negative=5))
        self.assertFalse(is_not_too_short_on_vouchers(short_maximum=10, postedc_quantity=5, vouchers_negative=6))

    def test_offer_was_made_just_before(self):
        from django.core.cache import cache
        user_id1 = 1
        user_id2 = 2
        # wait_key1 = 'wait_four_seconds{}'.format(1)
        # wait_key2 = 'wait_four_seconds{}'.format(2)
        must_wait_set(user_id2, 0.1)

        # cache.set(wait_key1,None)
        # cache.set(wait_key2, None)
        self.assertFalse(offer_was_made_just_before(user_id1))
        self.assertTrue(offer_was_made_just_before(user_id2))
        import time
        time.sleep(.1)
        self.assertFalse(offer_was_made_just_before(user_id1))
        self.assertFalse(offer_was_made_just_before(user_id2))


    def test_get_value_cum_RE(self):
        self.assertEqual(get_value_cum_RE(vouchers_used=10,player_demand=15,retail_price=10),100)
        self.assertEqual(get_value_cum_RE(vouchers_used=20, player_demand=15, retail_price=10), 150)

    def test_cv_STAND(self):
        self.assertEqual(cv_STAND(vouchers_used=10, vouchers_negative= 0, unitsCleared= 11),(21,0))
        self.assertEqual(cv_STAND(vouchers_used=0, vouchers_negative=5, unitsCleared=11), (6, 0))
        self.assertEqual(cv_STAND(vouchers_used=0, vouchers_negative=5, unitsCleared=1), (0, 4))

    def test_cv_REV(self):
        self.assertEqual(cv_REV(vouchers_used=10, vouchers_negative= 0, unitsCleared= 11),(0,1))
        self.assertEqual(cv_REV(vouchers_used=0, vouchers_negative=5, unitsCleared=11), (0, 16))
        self.assertEqual(cv_REV(vouchers_used=0, vouchers_negative=5, unitsCleared=1), (0, 6))
        self.assertEqual(cv_REV(vouchers_used=10, vouchers_negative=0, unitsCleared=1), (9, 0))

    def test_set_products(self):
        self.assertEqual(set_products(offer_tiepe=Offer.SELL,unitsCleared= 5, priceCleared=3), (15, -15))
        self.assertEqual(set_products(offer_tiepe=Offer.BUY, unitsCleared= 5, priceCleared=3), (-15, 15))

class function_in_FS_views_with_auction_setup (TestCase):
        # def setUp(self):
        #     self
        def setUp(self):
            print("+" * 40)
            print("setUp_" * 40)
            print("+" * 40)
            print("before auction")
            MasterMan.invalidate_caches()
            Period.objects.all().delete()
            auction, treatment = Auction.cache_or_create_auction()

            # print("auction:{}, treatment:{}".format(auction, treatment))
            period_list = Period.objects.filter(auction=auction).all()
            # for p in period_list:
            #     print("period: {}, {}, {}".format(p, p.auction, p.updated))


            log.info("6 auction.auction_init(treatment)")
            # print("player_objects:{}".format(Player.objects.filter(auction=auction).count()))
            log.info("call_auction_init(treatment)")
            auction.auction_created = auction.auction_init(treatment)
            # print("player_objects:{}".format(Player.objects.filter(auction=auction).count()))
            #
            # print("auction:{}, treatment:{}".format(auction, treatment))
            period_list = Period.objects.filter(auction=auction).all()
            # for p in period_list:
            #     print("period: {}, {}, {}".format(p, p.auction, p.updated))

            log.info("7 auction.instructions_create()")
            auction.instructions_created = auction.instructions_create()
            auction.save_and_cache()
            log.info("8 Distribution.demand_draws_create")
            # print("player_objects:{}".format(Player.objects.filter(auction=auction).count()))
            Distribution.demand_draws_create(auction, treatment)
            # print("self.assertEqual(Voucher.objects.count(), 35)")
            self.assertEqual(Voucher.objects.count(), 35)
            auction.demand_avg = \
            list(Distribution.objects.filter(auction=auction).aggregate(Avg('demand_draw')).values())[
                0]
            auction.demand_sd = \
                list(Distribution.objects.filter(auction=auction).aggregate(StdDev('demand_draw')).values())[0]
            # log.info('auction.demand_avg:' ,auction.demand_avg )
            auction.price_avg = \
            list(Distribution.objects.filter(auction=auction).aggregate(Avg('price_draw')).values())[0]
            auction.price_sd = \
            list(Distribution.objects.filter(auction=auction).aggregate(StdDev('price_draw')).values())[
                0]
            auction.cov_DP = list(Distribution.objects.filter(auction=auction).aggregate(Avg('DP')).values())[0] - (
                    auction.price_avg * auction.demand_avg)
            log.info("auction.cov_DP___________:".format(auction.cov_DP))

            auction.distribution_auction_created = True
            auction.save_and_cache()
            log.info("auction.distribution_auction_created = True")

            print("11 if Question.get_totalquestions(")
            if Question.get_totalquestions(auction) == 0:
                # pass
                # if not auction.testing_questions_defined:
                auction.testing_totalquestions = Question.define_questions(treatment, auction)
                auction.save_and_cache()
            print("self.assertEqual(Voucher.objects.count(), 35)")
            self.assertEqual(Voucher.objects.count(), 35)
            Player_stats.playerStats_create()
            print("self.assertEqual(Voucher.objects.count(), 35)")
            self.assertEqual(Voucher.objects.count(), 35)
            j = 0
            to_insert = []

            # Voucher.objects.all().delete()

            # auction = Distribution.demand_draws_create(auction, treatment)
            period_list = Period.objects.filter(auction=auction).all()
            # for p in period_list:
            #     print("period: {}, {}, {}".format(p, p.auction, p.updated))

            # auction = Player_stats.playerStats_create(auction, treatment)
            # auction.save_and_cache()
            period_list = Period.objects.filter(auction=auction).all()
            # for p in period_list:
            #     print("period: {}, {}, {}".format(p, p.auction, p.updated))

        def test_get_value_cum_PR(self):
            # print("before treatment")
            # treatment= Treatment.cache_or_create_treatment()


            # for i in range(1,36):
            #     j+=i
            #     v= Voucher.objects.get_or_create(id=i,idd=i,value_cum=j,auction=auction)[0]
            #     print("Voucher.objects.all():{}".format(Voucher.objects.all().values("id")))
            #     # v.save()
            #     # v = Voucher(auction=auction, idd=i, value_cum=j, value=i)
            #     print("v:{}".format(v))
            #     to_insert.append(v)
            #     # v.save()
            # print("to_insert:{}".format(to_insert))
            # msg = Voucher.objects.bulk_create(to_insert)
            auction, treatment = Auction.cache_or_create_auction()
            # print(":{}".format(Player.objects.filter(auction=auction)))
            voucher_list = Voucher.objects.filter(auction=auction)
            # for voucher in voucher_list:
            #     print("voucher:{}, {}, {}, cum:{}".format(voucher, voucher.idd, voucher.value, voucher.value_cum))
            self.assertEqual(Voucher.objects.count(),35)

            self.assertEqual(Voucher.objects.count(), 35)
