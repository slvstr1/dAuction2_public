import logging, time, random, os, uuid
from django.utils import timezone
from django.db import models
from .models import Phase, Player,  Group
from .auction import Auction
from dAuction2.models import BaseMethods

log = logging.getLogger(__name__)
logger = logging.getLogger(__name__)


class Offer(BaseMethods, models.Model):
    """ An offer is a triple of price, number of units, and indication if you want to buy or sell
     An offer can be original as given by a player
     However, an offer may only be partly matched (eg, I offer 2 units for 10, and there is a buyer who
     only wants 1 unit. The offer is than split into two parts, the original one, and a new one that
     is marked as "updated". The original one is matched (made into a transaction) and deleted (cleared),
     the new, "updated" offer lives on until it is matched, cancelled or the game ends.
     """
    SELL = 0
    BUY = 1
    OFFER_TIEPES = \
        (
            (SELL, 'SELL'),
            (BUY, 'BUY'),
        )

    PR = 0
    RE = 1
    ROLES = \
        (
            (PR, 'PR'),
            (RE, 'RE'),
        )

    id = models.BigAutoField(primary_key=True, null=False)
    auction = models.ForeignKey(Auction, default=None,on_delete=models.CASCADE, db_index=True)
    player = models.ForeignKey(Player,on_delete=models.CASCADE, db_index=True)
    #role = models.PositiveSmallIntegerField(choices=ROLES, default=PR)
    phase = models.ForeignKey(Phase,on_delete=models.CASCADE, db_index=True)
    group = models.ForeignKey(Group,null=True,on_delete=models.CASCADE)
    # offers are owned by the players
    created = models.DateTimeField(auto_now_add=True, null=True)
    updatedTime = models.DateTimeField(auto_now=True, null=True)
    timeCleared = models.DateTimeField(auto_now=True, null=True)
    # time the offer was created
    # updated = models.DateTimeField(auto_now=True)
    offer_tiepe = models.PositiveSmallIntegerField(choices=OFFER_TIEPES, default=SELL, db_index=True)
    canceled = models.BooleanField(default=False)
    # true if the offer was cancelled by the player
    cleared = models.BooleanField(default=False, db_index=True)
    # true if the offer was matched with a counteroffer and cleared
    updated = models.BooleanField(default=False)
    # true if the offer has been split off from an earlier one / so if the offer is new and has never been matched, this value will be False
    # In a better world, this Boolean would have been named "splitoff"
    unitsAvailable = models.SmallIntegerField(default=0)
    # the number of units that are still available (0 after clearing)
    unitsCleared = models.SmallIntegerField(default=0)
    # the number of units inherited from the direct parent offer
    priceCleared = models.SmallIntegerField(default=0)
    # the price for the offer has been traded (can be different from priceOriginal
    priceOriginal = models.SmallIntegerField(default=10)
    # the price in the original offer
    product = models.SmallIntegerField(default= 0)

    class Meta:
        # app_label = 'dAuction2'
        ordering = ["id"]
        get_latest_by = 'id'

    def __str__(self):  # For Python 2, use __str__ on Python 3
        return "id:{} type:{} pOr:{} uAV:{} pCl:{} uCl:{} player:{} group:{} user:{} auction:{}".format(self.id, self.offer_tiepe, self.priceOriginal,self.unitsAvailable,self.priceCleared,self.unitsCleared,self.player_id,self.group_id,self.player.user_id, self.auction_id)

    @classmethod
    def create_present_offer(cls, treatment, auction_id, phase, player_id, posedc_type, postedc_quantity,postedc_price, group_id, player):
        reuse = False
        cc = None
        if not treatment.allow_multiple_offers:
            previous_offer_same_type_list = Offer.objects.filter(player_id=player_id, phase=phase,offer_tiepe=posedc_type, cleared=False, canceled=False)
            # if False: # always make a new offer!!!
            if previous_offer_same_type_list.exists():
                if treatment.register_cancelled:
                    cc = previous_offer_same_type_list.last()
                    cc.canceled = True
                    # ccancel.save(update_fields=['canceled'])
                    c = cls(auction_id=auction_id, player_id=player_id, cleared=False, phase=phase,
                              offer_tiepe=posedc_type,
                              unitsAvailable=postedc_quantity, priceOriginal=postedc_price, group_id=group_id)
                else:
                    c = previous_offer_same_type_list.last()
                    c.offer_tiepe = posedc_type
                    c.unitsAvailable = postedc_quantity
                    c.priceOriginal = postedc_price
                    reuse = True
            else:
                c = cls(auction_id=auction_id, player_id=player_id, cleared=False, phase=phase,
                          offer_tiepe=posedc_type,
                          unitsAvailable=postedc_quantity, priceOriginal=postedc_price, group_id=group_id)
        else:
            c = cls(auction_id=auction_id, player_id=player_id, cleared=False, phase=phase,
                      offer_tiepe=posedc_type,
                      unitsAvailable=postedc_quantity, priceOriginal=postedc_price, group_id=group_id)
        return c, reuse, cc


    def create_matching_offer_list(c, auction_id, phase, player_id, group_id):
        # set type from JS form
        if c.offer_tiepe == Offer.SELL:  # then the matcher must be a buy
            offer_list = Offer.objects.select_related("player").prefetch_related('player__player_stats_set').filter(
                auction_id=auction_id, group_id=group_id, phase=phase, priceOriginal__gte=c.priceOriginal,
                offer_tiepe=Offer.BUY, cleared=False, canceled=False).exclude(player_id=player_id).order_by(
                '-priceOriginal', 'created')
        else: # c.offer_tiepe == Offer.BUY:  # then the matcher must be a sell
            offer_list = Offer.objects.select_related('player').prefetch_related('player__player_stats_set').filter(
                auction_id=auction_id, group_id=group_id, phase=phase, priceOriginal__lte=c.priceOriginal,
                offer_tiepe=Offer.SELL, cleared=False, canceled=False).exclude(player_id=player_id).order_by(
                'priceOriginal', 'created')
        # else:
        #     raise ValueError('valType is neither SELL or BUY')
        # log.info("connection.queries()", connection.queries)
        return list(offer_list)



    def getnumber(self):
        return self.id

    @classmethod
    def split_offer(cls, auction_id, group_id, to_split, to_split_player, other_offer, phase):
        # creates a copy of the offer (real copy, not a damn second pointer to the same object).
        # This one will contain the remaining units
        # I think there is a standard Python command for this, but I somehow didnt manage to get it done
        # logger.debug("BEGIN copy_offer(c,p, first): (%s,%s,%s)" % (c, p, first))
        # c2 = Offer(auction_id=auction_id,player=p, phase=phase, parentId=c.id, group=c.group)
        c2 = cls(auction_id=auction_id, player=to_split_player, phase=phase, group_id=group_id,
                   created=timezone.now())
        c2.priceOriginal = to_split.priceOriginal
        c2.offer_tiepe = to_split.offer_tiepe
        c2.unitsAvailable = to_split.unitsAvailable - other_offer.unitsCleared
        c2.updated = True # updated is thus true for new offers that are split of an old offer.
        c2.cleared = False
        # logger.debug("END copy_offer(c,p, first): (%s,%s,%s)" % (c, p, first))
        return c2



    # @classmethod
    # def setproducts(cls, c, first):
    #     # calculates the revenue for a sale or total cost for a buy
    #     # the revenue is then added to the Trading Revenue (the income from trading for a player)
    #     if c.offer_tiepe == cls.SELL:  # thus player p is selling and thus first is a buying offer
    #         p_stats_trading_result = first.priceCleared * first.unitsCleared
    #     else:
    #         p_stats_trading_result = -1 * first.priceCleared * first.unitsCleared
    #     return (p_stats_trading_result)