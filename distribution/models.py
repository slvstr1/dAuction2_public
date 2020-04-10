import random, logging
from django.db import models
# from django.utils import timezone
from dAuction2.models import BaseMethods, myround
from forward_and_spot.models import Auction, Treatment
# should run from /home/vagrant/venv/bin/python
# run manage.py loaddata deployment/db_users.json
#from master.models import *
log = logging.getLogger(__name__)


class Distribution(BaseMethods, models.Model):
    """
    """
    id = models.BigAutoField(primary_key=True, null=False)
    auction = models.ForeignKey(Auction, default=None,on_delete=models.CASCADE)
    idd = models.PositiveSmallIntegerField(default = 1, db_index=True)
    demand_draw = models.FloatField(default= 0)
    price_draw  = models.FloatField(default= 0)
    DP = models.FloatField(default=0)
    test = models.BooleanField(default=True)

    @classmethod
    def get_draws(cls, auction,treatment, x):
        # treatment=auction.treatment
        if treatment.distribution_used == Treatment.UNIFORM:
            dd = random.uniform(treatment.uniform_min, treatment.uniform_max)
            # print("distribution_UNIFORM!!!")
            # log.info("distribution_UNIFORM!!!")
        else:
            dd = random.normalvariate(treatment.mu, treatment.sigma)
            # print("distribution_NORMAL!!!")
            log.info("distribution_NORMAL!!!")
        price_draw = myround(treatment.a * pow((dd / treatment.PR_per_group), (treatment.convexity_parameter - 1)), 0.1)
        draw = cls(auction=auction, idd=x, test=True, demand_draw=myround(dd, 0.1), price_draw=price_draw,
                            DP=int(dd * price_draw))

        # period.total_demand = draw.demand_draw
        return draw, price_draw

    @classmethod
    def demand_draws_create(cls, auction, treatment):
        log.info("b_auction_at_create_draws:{}".format(auction))
        log.info("distribution_auction_created:{}".format(auction.distribution_auction_created))
        log.info("call_demand_draws_create")
        from forward_and_spot.models import Voucher
        # Player_stats.objects.filter(auction=auction).delete()
        # AuctionManager.remove_player_stats(auction, "Player_stats")
        # from F&S delete PS
        auction.remove_all_objects_in_class(["forward_and_spot.Player_stats","distribution.distribution",])

        auction.player_stats_created = False
        auction.save_and_cache()
        # cls.objects.filter(auction=auction).delete()
        to_insert = []
        random.seed(auction.id)
        for x in range(1, 1 + (treatment.d_draws_needed * 5)):
            draw, price_draw = cls.get_draws(auction, treatment, x)
            to_insert.append(draw)
        msg = cls.objects.bulk_create(to_insert)
        auction.distribution_auction_created = True
        Voucher.createVoucher(auction, treatment)
        log.info("e_auction_at_create_draws:{}".format(auction))
        log.info("distribution_auction_created in demand draws create:{}".format(auction.distribution_auction_created))
        auction.save_and_cache()


    def __str__(self):
        return "Distribution {0}".format(self.id)