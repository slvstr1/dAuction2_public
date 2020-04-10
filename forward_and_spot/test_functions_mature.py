from django.test import TestCase, TransactionTestCase
from forward_and_spot.models import Offer, Auction, Player, Group, Player_stats, Period, Phase, Voucher, Treatment
from dAuction2.models import Experiment
from dAuction2.models import User
from forward_and_spot.functions import set_voucher
from forward_and_spot.test_views_set_offer import function_in_FS_views_with_auction_setup, delete_all
# from .views import set_offer_nr, create_present_offer, create_matching_offer_list
# from .functions_mature import cv_REV, cv_REV_RE, cv_STAND_PR, cv_STAND, set_voucher
# from master.functions_main import createVoucher

class test_set_voucher(TransactionTestCase):
    def setUp(self):
        print("+"*40)
        print("test_set_offer_quick_succession1(TestCase):")
        delete_all(self)
        function_in_FS_views_with_auction_setup.setUp(self)
        print("**********************")
        print("setUp")
        print("**********************")


    def tearDown(self):
        delete_all(self)
        print("**********************")
        print("tearDown --- DELETED")
        print("**********************")

    def test_set_voucher_PR_PR_5_5_5(self):
        print("_____________test_set_voucher_PR_PR_5_5_5")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        # treatment =Treatment.objects.get_or_create(experiment=experiment)[0]

        # auction = Auction.objects.get_or_create(treatment=treatment)[0]

        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id

        
        
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id

        user = User.objects.get_or_create(username="p")[0]
        user_id = user.id
        player = Player.objects.get_or_create(user=user, role=0, auction=auction, group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 5
        vouchers_negative = 0

        p_stats = Player_stats.objects.get_or_create(player=player, role=0, auction=auction, group=group, period=period,
                                                     vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        user_idf = userf.id
        playerf = Player.objects.get_or_create(user=userf, role=0, auction=auction, group=group)[0]
        playerf.save()
        player_idf = playerf.id

        vouchers_used = 5
        vouchers_negative = 0

        unitsCleared = 5

        f_stats = Player_stats.objects.get_or_create(player=playerf, role=0, auction=auction, group=group, period=period,vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0 # SELL

        set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)

        # print ("p_stats",p_stats)
        # print("f_stats", f_stats)
        self.assertEqual(p_stats.vouchers_used,0)
        self.assertEqual(p_stats.vouchers_negative, 0)
        self.assertEqual(f_stats.vouchers_used, 10)
        self.assertEqual(f_stats.vouchers_negative, 0)


    def test_set_voucher_PR_PR_2_3_5(self):
        print("_____________test_set_voucher_PR_PR_2_3_5")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id


        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id

        user = User.objects.get_or_create(username="p")[0]
        user_id = user.id
        player = Player.objects.get_or_create(user=user, role=0, auction=auction, group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 2
        vouchers_negative = 0

        p_stats = Player_stats.objects.get_or_create(player=player, role=0, auction=auction, group=group, period=period,
                                                     vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        user_idf = userf.id
        playerf = Player.objects.get_or_create(user=userf, role=0, auction=auction, group=group)[0]
        playerf.save()
        player_idf = playerf.id

        vouchers_used = 3
        vouchers_negative = 0

        unitsCleared = 5

        f_stats = Player_stats.objects.get_or_create(player=playerf, role=0, auction=auction, group=group, period=period,vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0 # SELL

        set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)

        # print ("p_stats",p_stats)
        # print("f_stats", f_stats)
        self.assertEqual(p_stats.vouchers_used,0)
        self.assertEqual(p_stats.vouchers_negative, 3)
        self.assertEqual(f_stats.vouchers_used, 8)
        self.assertEqual(f_stats.vouchers_negative, 0)


    def test_set_voucher_RE_PR_2_3_5(self):
        print("_____________test_set_voucher_RE_PR_2_3_5")

        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()


        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id

        user = User.objects.get_or_create(username="p")[0]
        user_id = user.id
        player = Player.objects.get_or_create(user=user, role=1, auction=auction, group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 2
        vouchers_negative = 0

        p_stats = Player_stats.objects.get_or_create(player=player, role=1, auction=auction, group=group, period=period,
                                                     vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        user_idf = userf.id
        playerf = Player.objects.get_or_create(user=userf, role=0, auction=auction, group=group)[0]
        playerf.save()
        player_idf = playerf.id

        vouchers_used = 3
        vouchers_negative = 0

        unitsCleared = 5

        f_stats = Player_stats.objects.get_or_create(player=playerf, role=0, auction=auction, group=group, period=period,vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0 # SELL
        set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)

        # print ("p_stats",p_stats)
        # print("f_stats", f_stats)
        self.assertEqual(p_stats.vouchers_used,7)
        self.assertEqual(p_stats.vouchers_negative, 0)
        self.assertEqual(f_stats.vouchers_used, 8)
        self.assertEqual(f_stats.vouchers_negative, 0)


    def test_set_voucher_PR_RE_2_3_5(self):
        print("_____________test_set_voucher_PR_RE_2_3_5")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id


        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id

        user = User.objects.get_or_create(username="p")[0]
        user_id = user.id
        player = Player.objects.get_or_create(user=user, role=0, auction=auction, group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 2
        vouchers_negative = 0

        p_stats = Player_stats.objects.get_or_create(player=player, role=0, auction=auction, group=group, period=period,
                                                     vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        user_idf = userf.id
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        player_idf = playerf.id

        vouchers_used = 3
        vouchers_negative = 0

        unitsCleared = 5

        f_stats = Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0 # SELL

        set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)


        # print ("p_stats",p_stats)
        # print("f_stats", f_stats)
        self.assertEqual(p_stats.vouchers_used,0)
        self.assertEqual(p_stats.vouchers_negative, 3)
        self.assertEqual(f_stats.vouchers_used, 0)
        self.assertEqual(f_stats.vouchers_negative, 2)


    def test_set_voucher_RE_RE_2_3_5(self):
        print("_____________test_set_voucher_RE_RE_2_3_5")

        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()


        auction_id = auction.id

        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id

        user = User.objects.get_or_create(username="p")[0]
        user_id = user.id
        player = Player.objects.get_or_create(user=user, role=1, auction=auction, group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 2
        vouchers_negative = 0

        p_stats = Player_stats.objects.get_or_create(player=player, role=1, auction=auction, group=group, period=period,
                                                     vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        user_idf = userf.id
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        player_idf = playerf.id

        vouchers_used = 3
        vouchers_negative = 0

        unitsCleared = 5

        f_stats = Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0 # SELL

        set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction,treatment)

        # print ("p_stats",p_stats)
        # print("f_stats", f_stats)
        self.assertEqual(p_stats.vouchers_used,7)
        self.assertEqual(p_stats.vouchers_negative, 0)
        self.assertEqual(f_stats.vouchers_used, 0)
        self.assertEqual(f_stats.vouchers_negative, 2)



from forward_and_spot.functions import cv_REV, get_value_cum_RE, cv_STAND, get_value_cum_PR
class test_cv_REV(TransactionTestCase):
    def setUp(self):
        print("+"*40)
        print("test_set_offer_quick_succession1(TransactionTestCase):")
        delete_all(self)
        function_in_FS_views_with_auction_setup.setUp(self)
        print("**********************")
        print("setUp")
        print("**********************")


    def tearDown(self):
        delete_all(self)
        print("**********************")
        print("tearDown --- DELETED")
        print("**********************")


    def test_cv_REV_5_0_5(self):
        print("test_cv_REV_5_0_5")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id=auction.id

        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user,role=0,auction=auction,group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 5
        vouchers_negative = 0
        unitsCleared = 5

        p_stats = Player_stats.objects.get_or_create(player=player,role=0, auction=auction, group=group,period=period, vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats =Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)
        new_vouchers_used,  vouchers_negative = cv_REV(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_PR(auction, new_vouchers_used)
            # cv_REV(p_stats, unitsCleared, auction)

        print ("result: ",new_vouchers_used, value_cum, vouchers_negative )
        self.assertEqual(new_vouchers_used, 0)
        self.assertEqual(value_cum, 0)
        self.assertEqual(vouchers_negative, 0)

    def test_cv_REV_5_0_7(self):
        print("test_cv_REV_5_0_7")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id


        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user,role=0, auction=auction, group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 5
        vouchers_negative = 0
        unitsCleared = 7

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group, period=period,role=0,
                                                     vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)

        new_vouchers_used, vouchers_negative = cv_REV(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_PR(auction, new_vouchers_used)

        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_REV(p_stats, unitsCleared, auction)

        print("result: ", new_vouchers_used, value_cum, vouchers_negative)
        self.assertEqual(new_vouchers_used, 0)
        self.assertEqual(value_cum, 0)
        self.assertEqual(vouchers_negative, 2)


    def test_cv_REV_0_2_4(self):
        print("test_cv_REV_0_2_4")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()

        auction_id = auction.id


        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user,role=0, auction=auction, group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 0
        vouchers_negative = 2
        unitsCleared = 4

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,role=0, period=period,
                                                     vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)


        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_REV(p_stats, unitsCleared, auction)
        new_vouchers_used, vouchers_negative = cv_REV(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_PR(auction, new_vouchers_used)

        print("result: ", new_vouchers_used, value_cum, vouchers_negative)
        self.assertEqual(new_vouchers_used, 0)
        self.assertEqual(value_cum, 0)
        self.assertEqual(vouchers_negative, 6)

    def test_cv_REV_10_0_4(self):
        print("test_cv_REV_10_0_4")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]
        auction, treatment = Auction.cache_or_create_auction()

        auction_id = auction.id


        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user,role=0, auction=auction, group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 10
        vouchers_negative = 0
        unitsCleared = 4

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,role=0, period=period,
                                                     vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)

        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_REV(p_stats, unitsCleared, auction)
        new_vouchers_used, vouchers_negative = cv_REV(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_PR(auction, new_vouchers_used)

        print("result: ", new_vouchers_used, value_cum, vouchers_negative)
        self.assertEqual(new_vouchers_used, 6)
        # self.assertEqual(value_cum, 0)

        value= Voucher.objects.get(idd=new_vouchers_used).value_cum
        new_vouchers_used

        self.assertEqual(value_cum, value)

        self.assertEqual(vouchers_negative, 0)


class test_cv_REV_RE(TransactionTestCase):

    def setUp(self):
        print("+" * 40)
        print("test_set_offer_quick_succession1(TransactionTestCase):")
        delete_all(self)
        function_in_FS_views_with_auction_setup.setUp(self)
        print("**********************")
        print("setUp")
        print("**********************")

    def tearDown(self):
        delete_all(self)
        print("**********************")
        print("tearDown --- DELETED")
        print("**********************")

    def test_cv_REV_RE_5_0_5(self):
        print("+"*100)
        print("+" * 100)

        print("test_cv_REV_RE_5_0_5")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]
        #

        # auction= Auction.objects.get_or_create(treatment=treatment)[0]
        auction, treatment = Auction.cache_or_create_auction()

        auction_id=auction.id
        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user,role=1,auction=auction,group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 5
        vouchers_negative = 0
        unitsCleared = 5

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,role=1,period=period, vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)

        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_REV_RE(p_stats, unitsCleared, treatment)
        new_vouchers_used, vouchers_negative = cv_REV(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_RE(new_vouchers_used, p_stats.player_demand,treatment.retail_price)

        print ("result: ",new_vouchers_used, value_cum, vouchers_negative )
        print("p_stats",p_stats)
        self.assertEqual(new_vouchers_used, 0)
        self.assertEqual(value_cum, 0)
        self.assertEqual(vouchers_negative, 0)

    def test_cv_REV_RE_5_0_7(self):
        print("test_cv_REV_RE_5_0_7")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user,role=1, auction=auction, group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 5
        vouchers_negative = 0
        unitsCleared = 7

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,role=1, period=period,
                                                     vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)


        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_REV_RE(p_stats, unitsCleared, treatment)
        new_vouchers_used, vouchers_negative = cv_REV(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_RE(new_vouchers_used, p_stats.player_demand, treatment.retail_price)

        print("result: ", new_vouchers_used, value_cum, vouchers_negative)
        print("p_stats",p_stats)

        self.assertEqual(new_vouchers_used, 0)
        self.assertEqual(value_cum, 0)
        self.assertEqual(vouchers_negative, 2)


    def test_cv_REV_RE_0_2_4(self):
        print("test_cv_REV_RE_0_2_4")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user,role=1, auction=auction, group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 0
        vouchers_negative = 2
        unitsCleared = 4

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,role=1, period=period,
                                                     vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)



        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_REV_RE(p_stats, unitsCleared, treatment)
        new_vouchers_used, vouchers_negative = cv_REV(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_RE(new_vouchers_used, p_stats.player_demand, treatment.retail_price)

        print("result: ", new_vouchers_used, value_cum, vouchers_negative)
        print("p_stats",p_stats)
        self.assertEqual(new_vouchers_used, 0)
        self.assertEqual(value_cum, 0)
        self.assertEqual(vouchers_negative, 6)

    def test_cv_REV_RE_10_0_4(self):
        print("test_cv_REV_RE_10_0_4")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user,role=1, auction=auction, group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 10
        vouchers_negative = 0
        unitsCleared = 4

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,role=1, period=period,vouchers_used=vouchers_used, vouchers_negative=vouchers_negative, player_demand=10)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)


        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_REV_RE(p_stats, unitsCleared, treatment)
        new_vouchers_used, vouchers_negative = cv_REV(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_RE(new_vouchers_used, p_stats.player_demand, treatment.retail_price)

        # print("result: ", new_vouchers_used, value_cum, vouchers_negative)
        # print("p_stats",p_stats)
        # print("new_vouchers_used * auction.retail_price",new_vouchers_used * auction.retail_price)
        self.assertEqual(new_vouchers_used, 6)
        # self.assertEqual(value_cum, 0)
        self.assertEqual(vouchers_negative, 0)

        self.assertEqual(value_cum, new_vouchers_used * treatment.retail_price )
        # self.assertEqual(1, 2)
    print("+"*100)
    print("+"*100)

    def test_cv_REV_RE_10_0_4_dem4(self):
        print("test_cv_REV_RE_10_0_4")
        experiment = Experiment.objects.get_or_create()[0]

        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user,role=1, auction=auction, group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 10
        vouchers_negative = 0
        unitsCleared = 4

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,role=1, period=period,vouchers_used=vouchers_used, vouchers_negative=vouchers_negative, player_demand=4)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)



        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_REV_RE(p_stats, unitsCleared, treatment)
        new_vouchers_used, vouchers_negative = cv_REV(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_RE(new_vouchers_used, p_stats.player_demand, treatment.retail_price)

        # print("result: ", new_vouchers_used, value_cum, vouchers_negative)
        # print("p_stats",p_stats)
        # print("new_vouchers_used * auction.retail_price",new_vouchers_used * auction.retail_price)
        self.assertEqual(new_vouchers_used, 6)
        # self.assertEqual(value_cum, 0)
        self.assertEqual(vouchers_negative, 0)

        self.assertEqual(value_cum, 4 * treatment.retail_price )
        # self.assertEqual(1, 2)
    print("+"*100)
    print("+"*100)


class test_cv_STAND(TransactionTestCase):
    def setUp(self):
        print("+" * 40)
        print("test_set_offer_quick_succession1(TransactionTestCase):")
        delete_all(self)
        function_in_FS_views_with_auction_setup.setUp(self)
        print("**********************")
        print("setUp")
        print("**********************")

    def tearDown(self):
        delete_all(self)
        print("**********************")
        print("tearDown --- DELETED")
        print("**********************")

    def test_cv_STAND_5_0_5(self):
        print("test_cv_STAND_5_0_5")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id=auction.id
        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user,role=1,auction=auction,group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 5
        vouchers_negative = 0
        unitsCleared = 5

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,role=1,period=period, vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)




        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_STAND(p_stats, unitsCleared, treatment)
        new_vouchers_used, vouchers_negative = cv_STAND(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_RE(new_vouchers_used, p_stats.player_demand, treatment.retail_price)

        print ("result: ",new_vouchers_used, value_cum, vouchers_negative )
        self.assertEqual(new_vouchers_used, 10)
        # self.assertEqual(value_cum, 0)
        self.assertEqual(vouchers_negative, 0)

    def test_cv_STAND_5_0_7(self):
        print("test_cv_STAND_5_0_7")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user,role=1, auction=auction, group=group)[0]
        player.save()
        player_id = player.id

        vouchers_used = 5
        vouchers_negative = 0
        unitsCleared = 7

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,role=1, period=period,
                                                     vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)




        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_STAND(p_stats, unitsCleared, treatment)
        new_vouchers_used, vouchers_negative = cv_STAND(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_RE(new_vouchers_used, p_stats.player_demand, treatment.retail_price)

        # print("result: ", new_vouchers_used, value_cum, vouchers_negative)
        self.assertEqual(new_vouchers_used, 12)
        # self.assertEqual(value_cum, 0)
        self.assertEqual(vouchers_negative, 0)


    def test_cv_STAND_0_2_4(self):
        print("*" * 50)
        print("test_cv_STAND_0_2_4")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user, auction=auction, group=group,role=1)[0]
        player.save()
        player_id = player.id

        vouchers_used = 0
        vouchers_negative = 2
        unitsCleared = 4

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,role=1, period=period,
                                                     vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)




        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_STAND(p_stats, unitsCleared, treatment)
        new_vouchers_used, vouchers_negative = cv_STAND(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_RE(new_vouchers_used, p_stats.player_demand, treatment.retail_price)

        # print("result: ", new_vouchers_used, value_cum, vouchers_negative)
        # print("p_stats ",p_stats )
        self.assertEqual(new_vouchers_used, 2)
        # self.assertEqual(value_cum, 0)
        self.assertEqual(vouchers_negative, 0)
        print("*" * 50)
        print("SUCCESS 11")
        print("*"*50)
        print("*" * 50)

    def test_cv_STAND_10_0_4(self):
        print("*" * 50)
        print("test_cv_STAND_10_0_4")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id
        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user, auction=auction, group=group,role=1)[0]
        player.save()
        player_id = player.id

        vouchers_used = 10
        vouchers_negative = 0
        unitsCleared = 4

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,role=1, period=period,
                                                     vouchers_used=vouchers_used, vouchers_negative=vouchers_negative, player_demand=20)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)

        new_vouchers_used, vouchers_negative = cv_STAND(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_RE(new_vouchers_used, p_stats.player_demand, treatment.retail_price)

        # new_vouchers_used, value_cum, vouchers_negative = cv_STAND(p_stats, unitsCleared, treatment)

        # print("result: ", new_vouchers_used, value_cum, vouchers_negative)
        # print("p_stats ",p_stats )
        self.assertEqual(new_vouchers_used, 14)
        # self.assertEqual(value_cum, 0)
        self.assertEqual(value_cum, new_vouchers_used * treatment.retail_price)
        self.assertEqual(vouchers_negative, 0)
        print("*" * 50)
        print("SUCCESS 11")
        print("*"*50)
        print("*" * 50)

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,role=1, period=period,
                                                     vouchers_used=vouchers_used, vouchers_negative=vouchers_negative, player_demand=3)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)




        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_STAND(p_stats, unitsCleared, treatment)
        new_vouchers_used, vouchers_negative = cv_STAND(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_RE(new_vouchers_used, p_stats.player_demand, treatment.retail_price)

        # print("result: ", new_vouchers_used, value_cum, vouchers_negative)
        # print("p_stats ",p_stats )
        self.assertEqual(new_vouchers_used, 14)
        # self.assertEqual(value_cum, 0)
        self.assertEqual(value_cum, 3 * treatment.retail_price)
        self.assertEqual(vouchers_negative, 0)
        print("*" * 50)
        print("SUCCESS 11")
        print("*"*50)
        print("*" * 50)

class test_cv_STAND_PR(TransactionTestCase):
    def setUp(self):
        print("+" * 40)
        print("test_set_offer_quick_succession1(TransactionTestCase):")
        delete_all(self)
        function_in_FS_views_with_auction_setup.setUp(self)
        print("**********************")
        print("setUp")
        print("**********************")

    def tearDown(self):
        delete_all(self)
        print("**********************")
        print("tearDown --- DELETED")
        print("**********************")

    def test_cv_STAND_PR_5_0_5(self):
        print("test_cv_STAND_PR_5_0_5")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id=auction.id
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        period = Period.objects.get_or_create(idd=1,auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period,auction=auction,idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id=user.id
        group= Group.objects.get_or_create(idd=1,auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user,auction=auction,group=group,role=0)[0]
        player.save()
        player_id = player.id

        vouchers_used = 5
        vouchers_negative = 0
        unitsCleared = 5

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,period=period,role=0, vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)
        


        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_STAND_PR(p_stats, unitsCleared, auction)
        new_vouchers_used, vouchers_negative = cv_STAND(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_PR(auction, new_vouchers_used)

        print ("result: ",new_vouchers_used, value_cum, vouchers_negative )
        self.assertEqual(new_vouchers_used, 10)
        # self.assertEqual(value_cum, 0)
        self.assertEqual(vouchers_negative, 0)

    def test_cv_STAND_PR_5_0_7(self):
        print("test_cv_STAND_PR_5_0_7")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user, auction=auction, group=group,role=0)[0]
        player.save()
        player_id = player.id

        vouchers_used = 5
        vouchers_negative = 0
        unitsCleared = 7

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group, period=period,role=0,vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)



        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_STAND_PR(p_stats, unitsCleared, auction)
        new_vouchers_used, vouchers_negative = cv_STAND(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_PR(auction, new_vouchers_used)

        print("result: ", new_vouchers_used, value_cum, vouchers_negative)
        self.assertEqual(new_vouchers_used, 12)
        # self.assertEqual(value_cum, 0)
        self.assertEqual(vouchers_negative, 0)


    def test_cv_STAND_PR_0_2_4(self):
        print("test_cv_STAND_PR_0_2_4")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id
        # experiment = Experiment.objects.get_or_create()[0]
        # experiment.save()
        # treatment = Treatment.objects.get_or_create(experiment=experiment)[0]

        voucher_list= Voucher.objects.all()
        # for voucher in voucher_list:
        #     print("voucher: {} {}".format(voucher, voucher.value_cum))


        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user, auction=auction, group=group,role=0)[0]
        player.save()
        player_id = player.id

        vouchers_used = 0
        vouchers_negative = 2
        unitsCleared = 4

        p_stats = Player_stats.objects.get_or_create(player=player, auction=auction, group=group,role=0, period=period,vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        result_voucher = Voucher.objects.get(idd=2)

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)




        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_STAND_PR(p_stats, unitsCleared, auction)
        new_vouchers_used, vouchers_negative = cv_STAND(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_PR(auction, new_vouchers_used)

        # print("result: ", new_vouchers_used, value_cum, vouchers_negative)
        self.assertEqual(new_vouchers_used, 2)
        self.assertEqual(value_cum, result_voucher.value_cum )
        self.assertEqual(vouchers_negative, 0)

    def test_cv_STAND_PR_10_0_4(self):
        print("test_cv_STAND_PR_10_0_4")
        experiment = Experiment.objects.get_or_create()[0]
        experiment.save()
        auction, treatment = Auction.cache_or_create_auction()
        auction_id = auction.id

        period = Period.objects.get_or_create(idd=1, auction=auction)[0]
        phase = Phase.objects.get_or_create(period=period, auction=auction, idd=1)[0]
        user = User.objects.get_or_create()[0]
        user_id = user.id
        group = Group.objects.get_or_create(idd=1, auction=auction)[0]
        group_id = group.id
        player = Player.objects.get_or_create(user=user, auction=auction, group=group, role=0)[0]
        player.save()
        player_id = player.id

        vouchers_used = 10
        vouchers_negative = 0
        unitsCleared = 4

        p_stats = \
        Player_stats.objects.get_or_create(player=player, auction=auction, group=group, role=0, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]

        userf = User.objects.get_or_create(username="f")[0]
        playerf = Player.objects.get_or_create(user=userf, role=1, auction=auction, group=group)[0]
        playerf.save()
        f_stats = \
        Player_stats.objects.get_or_create(player=playerf, role=1, auction=auction, group=group, period=period,
                                           vouchers_used=vouchers_used, vouchers_negative=vouchers_negative)[
            0]
        first_offer_tiepe = 0  # SELL
        hh = set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment)



        # new_vouchers_used, value_cum, vouchers_negative = hh.cv_STAND_PR(p_stats, unitsCleared, auction)
        new_vouchers_used, vouchers_negative = cv_STAND(vouchers_used, vouchers_negative, unitsCleared)
        value_cum = get_value_cum_PR(auction, new_vouchers_used)

        # print("result: ", new_vouchers_used, value_cum, vouchers_negative)
        self.assertEqual(new_vouchers_used, 14)
        value=Voucher.objects.get(idd=new_vouchers_used).value_cum
        self.assertEqual(value_cum, value)
        self.assertEqual(vouchers_negative, 0)

            # self.assertEqual(value_cum, new_vouchers_used * auction.retail_price )
