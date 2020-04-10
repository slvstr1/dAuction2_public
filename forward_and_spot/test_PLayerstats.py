import logging
from django.test import TestCase, RequestFactory, TransactionTestCase
from forward_and_spot.models import Treatment
from dAuction2.models import Experiment
from master.models import MasterMan
# Offer, Auction, Player, User, Group, Player_stats, Period, Phase,
from .views import set_offer_nr, set_offer
# from master.functions_main import createVoucher
# from forward_and_spot.models import Offer, Auction, Player, Group, Player_stats, Period, Phase, Timer, Voucher
# from dAuction2.models import User
from forward_and_spot.functions import assign_leftover, divideTotal,checkMaxObey
from .test_views_set_offer import function_in_FS_views_with_auction_setup, delete_all

log = logging.getLogger(__name__)

class test_set_offer_none(TransactionTestCase):
    def delete_all(self):
        delete_all(self)


    def setUp(self):
        log.info("+"*40)
        log.info("setUp")
        log.info("+" * 40)
        self.delete_all()

    def tearDown(self):
        # Clean up run after every test method.
        self.delete_all()
        log.info("**********************")
        log.info("tearDown --- DELETED")
        log.info("**********************")

    def test_assign_leftover(self):
        RE_per_group = 5
        leftover_RE = 0
        demand_share_RE = 4
        demand_share_list_RE = assign_leftover(RE_per_group, leftover_RE, demand_share_RE)
        print(f"demand_share_list_RE: {demand_share_list_RE}")
        self.assertEqual(demand_share_list_RE, [4,4,4,4,4])

        RE_per_group = 5
        leftover_RE = 2
        demand_share_RE = 4
        demand_share_list_RE = assign_leftover(RE_per_group, leftover_RE, demand_share_RE)
        print(f"demand_share_list_RE: {demand_share_list_RE}")
        self.assertGreaterEqual(5, max(demand_share_list_RE))
        self.assertEqual(min(demand_share_list_RE),4)
        self.assertCountEqual(demand_share_list_RE,[4,4,4,5,5])

        RE_per_group = 4
        leftover_RE = 2
        demand_share_RE = 14
        demand_share_list_RE = assign_leftover(RE_per_group, leftover_RE, demand_share_RE)
        print(f"demand_share_list_RE: {demand_share_list_RE}")
        self.assertGreaterEqual(15, max(demand_share_list_RE))
        self.assertEqual(min(demand_share_list_RE), 14)
        self.assertCountEqual(demand_share_list_RE, [14,14, 15, 15])

        # self.assertFalse(True)
    def test_divideTotal(self):
        # divideTotal(demand_draw, PR_per_group )
        self.assertEqual((2,0),divideTotal(10, 5))
        self.assertEqual((2, 2), divideTotal(10, 4))
        self.assertEqual((5, 0), divideTotal(20, 4))
        self.assertEqual((4, 3), divideTotal(19, 4))
        # self.assertFalse(True)

    def test_checkMaxObey(self):
        self.assertEqual(checkMaxObey(12,15, False),(12,False))
        self.assertEqual(checkMaxObey(15, 15, False), (15, False))
        self.assertEqual(checkMaxObey(16, 15, False), (15, True))
        self.assertEqual(checkMaxObey(26, 15, False), (15, True))

        self.assertEqual(checkMaxObey(12, 15, True), (12, True))
        self.assertEqual(checkMaxObey(15, 15, True), (15, True))
        self.assertEqual(checkMaxObey(16, 15, True), (15, True))
        self.assertEqual(checkMaxObey(26, 15, True), (15, True))
        # self.assertFalse(True)