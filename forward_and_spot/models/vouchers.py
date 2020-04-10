import logging
log = logging.getLogger(__name__)
logger = logging.getLogger(__name__)

from django.core.cache import cache
from django.db import models
from .auction import Auction
# from .offer import Offer
# from .models import Player
from dAuction2.models import BaseMethods
from dAuction2.models import myround
log = logging.getLogger(__name__)


class BaseVoucher(BaseMethods, models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    auction = models.ForeignKey(Auction, default=None, on_delete=models.CASCADE)
    idd = models.CharField(max_length=30, default="<i>UNITS DEMANDED</i>", db_index=True)
    value_cum = models.FloatField(default=-1)
    value = models.FloatField(default=-1)
    class Meta:
        abstract = True
        ordering = ['id']

    def __str__(self):  # For Python 2, use __str__ on Python 3
        return str(self.id)


    @classmethod
    def get_voucher_list(cls,auction, voucher_list_name):
        voucher_list = cache.get(voucher_list_name)
        if not voucher_list:
            from master.models import MasterMan
            voucher_list = cls.objects.filter(auction=auction)
            MasterMan.cache_it(voucher_list_name, voucher_list)
        return voucher_list


class Voucher(BaseVoucher):
    """ a "voucher" is a unit of the good that is held by players in their stock
    Producers may produce units against incurring a cost. Vouchers is for producers the object that
    gives the details of the number of units that can be produced by a producer and against what costs.
    Retailers earn money by buying units - it can be thought of that producers again sell the units
    Vouchers is for Retailers the object that gives the details on the number of units that Retailers
    can purchase and how much earnings this brings
    """

    @classmethod
    def createVoucher(cls, auction, treatment):
        from forward_and_spot.models import VoucherRE
        def rounder(value2_cumm):
            if value2_cumm < 30:
                value2_cumm = myround(value2_cumm, 0.1)
            elif value2_cumm < 400:
                value2_cumm = int(myround(value2_cumm, 1))
            elif value2_cumm < 4000:
                value2_cumm = int(myround(value2_cumm, 5))
            else:
                value2_cumm = int(myround(value2_cumm, 10))
            return value2_cumm

        value2_cumm_previous = 0
        number_list = range(1, int(treatment.max_vouchers + 1))
        to_insert = []
        for i in number_list:
            # log.info("i:", i)
            value2_cumm = treatment.F + (treatment.a / treatment.convexity_parameter) * pow(i,
                                                                                            treatment.convexity_parameter)
            value2_cumm = rounder(value2_cumm)
            valPR = value2_cumm - value2_cumm_previous
            value2_cumm_previous = value2_cumm
            # log.info("value2_cumm",value2_cumm)

            # creates a list with marginal values. The values are strictly increasing and convex
            # with a maximum of 1200. This construction avoids needing to sort.
            v = cls(auction=auction, idd=i, value_cum=value2_cumm, value=valPR)
            to_insert.append(v)
            # v.save()
        msg = cls.objects.bulk_create(to_insert)
        log.info("msg:{}".format(msg))
        auction_retail_price = str(treatment.retail_price)

        to_insert = []
        for i in range(1, 6):
            to_insert.append(VoucherRE(auction=auction, idd=str(i), value_cum=treatment.retail_price * i,value=auction_retail_price))
        # msg = Voucher.objects.bulk_create(to_insert)
        for i in range(6, 7):
            to_insert.append(
                VoucherRE(auction=auction, idd="...", value_cum=treatment.retail_price * i, value=auction_retail_price))
        to_insert.append(VoucherRE(auction=auction,value_cum=treatment.retail_price * i,value=auction_retail_price))
        for i in range(1, 4):
            to_insert.append(
                VoucherRE(auction=auction, idd="<i>UNITS DEMANDED</i> + {}".format(i), value_cum=0, value="0"))
            # vRE.save()
        to_insert.append(VoucherRE(auction=auction, idd="<i>UNITS DEMANDED</i> + ...", value_cum=int(0), value="0"))
        msg = VoucherRE.objects.bulk_create(to_insert)
        auction.save_and_cache()



    # @classmethod
    #

class VoucherRE(BaseVoucher):
    """ a "voucher" is a unit of the good that is held by players in their stock
    Producers may produce units against incurring a cost. Vouchers is for producers the object that
    gives the details of the number of units that can be produced by a producer and against what costs.
    Retailers earn money by buying units - it can be thought of that producers again sell the units
    Vouchers is for Retailers the object that gives the details on the number of units that Retailers
    can purchase and how much earnings this brings
    """
    # id = models.BigAutoField(primary_key=True, null=False)
    # auction = models.ForeignKey(Auction, default=None,on_delete=models.CASCADE)
    idd = models.CharField(max_length=30, default="<i>UNITS DEMANDED</i>", db_index=True)
    value = models.CharField(max_length=30, default="")
    # value_cum = models.FloatField(default=-1)
    # value = models.CharField(max_length=30,default="")
    #
    # class Meta:
    #     ordering = ['id']
    # def __str__(self):
    #     return str(self.id)