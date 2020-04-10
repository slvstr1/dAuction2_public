#!python3
# import time
import logging, random
from django.utils import timezone
from django_bulk_update.helper import bulk_update
from forward_and_spot.models import Offer, Player, Voucher
# from forward_and_spot.models.offer import Offer

log = logging.getLogger(__name__)


def set_total_cost_value(stats, value_cum):
    if stats.role == Player.PR:
        stats.total_cost = value_cum
        stats.profit = stats.trading_result - value_cum
    else:
        stats.total_values = value_cum
        stats.profit = stats.trading_result + value_cum


def get_value_cum_PR(auction, vouchers_used, vouchers_negative):
    if vouchers_negative > 0:
        value_cum = 0
    else:
        value_cum = Voucher.objects.values_list('value_cum', flat=True).get(auction=auction,idd=vouchers_used)
    return value_cum

# cv_REV(stats.vouchers_used, stats.vouchers_negative, unitsCleared)
def cv_REV(vouchers_used, vouchers_negative, unitsCleared):
    # real_vouchers_used = max(vouchers_used - unitsCleared - vouchers_negative, 0)  # OK
    new_vouchers_used = max(vouchers_used - unitsCleared, 0)  # OK
    vouchers_negative = max(vouchers_negative + unitsCleared - vouchers_used, 0)  # OK
    return new_vouchers_used, vouchers_negative

# get_value_cum_RE(stats.vouchers_used, stats.player_demand, treatment.retail_price)
def get_value_cum_RE(vouchers_used, player_demand, retail_price):
    value_cum = min(vouchers_used, player_demand) * retail_price
    # print("value_cum:{}".format(value_cum))
    return value_cum

# cv_STAND(stats.vouchers_used, stats.vouchers_negative, unitsCleared)
def cv_STAND(vouchers_used, vouchers_negative, unitsCleared):
    vouchers_used = max(vouchers_used + unitsCleared - vouchers_negative, 0)  # OK
    vouchers_negative = max(vouchers_negative - unitsCleared, 0)  # OK
    # ToDo: check - shouldnt be max of units req?
    return vouchers_used, vouchers_negative

def get_value_cum_PR(auction, vouchers_used):
    if vouchers_used == 0:
        value_cum = 0
    else:
        value_cum = Voucher.objects.values_list('value_cum', flat=True).get(auction=auction,idd=vouchers_used)
    return value_cum

def set_voucher(p_stats, f_stats, first_offer_tiepe, unitsCleared, auction, treatment):
    # set_voucher(p_stats, f_stats, first, c.unitsCleared, period,auction)
    # this writes the changes to the vouchers of players after they have made a transaction
    # For Producers (Retailers), vouchers are used as they sell (buy).
    # For Producers (Retailers), vouchers are released if they buy (sell).
    # If a Producer (Retailers) buys (sells) more than he has sold (bought) extra vouchers are created for him
    # #p is the player that is treated, #first_player is the best match (the first in the list)
    # #first is the offer of #first_player, #unitsCleared is the number of units in the transaction between
    # #p and #first_player

    # log.debug("BEGIN set_voucher(p,first_offer_tiepe,unitsCleared): %s, %s, %s " % (
    #     p_stats.player, first_offer_tiepe, unitsCleared))
    # log.info("BEGIN set_voucher(p,first_offer_tiepe,unitsCleared): %s, %s, %s " % (
    #     p_stats.player, first_offer_tiepe, unitsCleared))
    # print("BEGIN set_voucher(p,first_offer_tiepe,unitsCleared): %s, %s, %s " % (
    #     p_stats.player, first_offer_tiepe, unitsCleared))
    # print("f_stats.role:{}".format(f_stats.role))
    # print("p_stats.role:{}".format(p_stats.role))
    if p_stats.role == Player.RE:
        # log.info("RE! Player:{}".format(p_stats.player))
        if first_offer_tiepe == Offer.SELL:
            # STAND RE for p: p is a REtailer, and the counterparty sold, so REtailer p bought
            # log.debug("standard case for p")
            # log.info("standard case for p")
            # print("standard case for p")
            p_stats.vouchers_used, p_stats.vouchers_negative = cv_STAND(p_stats.vouchers_used, p_stats.vouchers_negative, unitsCleared)
            value_cum = get_value_cum_RE(p_stats.vouchers_used, p_stats.player_demand, treatment.retail_price)
            # log.info("Player.RE, stand, value_cum:{}".format(value_cum))
            set_total_cost_value(p_stats, value_cum)
            if f_stats.role == Player.PR:
                # log.info("PR! Player:{}".format(f_stats.player))
                # STAND PR for f: fp is a PRoducer, and sold
                # log.debug("standard case for first_player")
                f_stats.vouchers_used, f_stats.vouchers_negative = cv_STAND(f_stats.vouchers_used, f_stats.vouchers_negative, unitsCleared)
                value_cum = get_value_cum_PR(auction, f_stats.vouchers_used)
                set_total_cost_value(f_stats, value_cum)
            else:
                # log.info("RE! Player:{}".format(f_stats.player))
                # REV RE for f: first_player is a REtailer, and the counterparty bought, so REtailer first_player sold
                # log.debug("reversed case for for first_player")
                # log.info("reversed case for for first_player")
                # print("reversed case for for first_player")
                f_stats.vouchers_used, f_stats.vouchers_negative = cv_REV(f_stats.vouchers_used, f_stats.vouchers_negative, unitsCleared)
                value_cum = get_value_cum_RE(f_stats.vouchers_used, f_stats.player_demand, treatment.retail_price)
                # log.info("Player.RE,rev, value_cum:{}".format(value_cum))
                set_total_cost_value(f_stats, value_cum)
        elif first_offer_tiepe == Offer.BUY:
            # REV RE for p: p is a REtailer, and the counterparty bought, thus p sold
            # log.info("unitsCleared",unitsCleared)
            p_stats.vouchers_used, p_stats.vouchers_negative = cv_REV(p_stats.vouchers_used, p_stats.vouchers_negative, unitsCleared)
            value_cum = get_value_cum_RE(p_stats.vouchers_used, p_stats.player_demand, treatment.retail_price)
            set_total_cost_value(p_stats, value_cum)
            if f_stats.role == Player.PR:
                # log.info("PR! Player:{}".format(f_stats.player))
                # REV PR for f: f is a PR and bought
                f_stats.vouchers_used, f_stats.vouchers_negative = cv_REV(f_stats.vouchers_used, f_stats.vouchers_negative, unitsCleared)
                value_cum = get_value_cum_PR(auction, f_stats.vouchers_used)
                # log.info("Player.PR, stand, value_cum:{}".format(value_cum))
                set_total_cost_value(f_stats, value_cum)
            else:
                # log.info("RE! Player:{}".format(f_stats.player))
                # STAND RE for f: f is a RE and bought
                f_stats.vouchers_used, f_stats.vouchers_negative = cv_STAND(f_stats.vouchers_used, f_stats.vouchers_negative, unitsCleared)
                value_cum = get_value_cum_RE(f_stats.vouchers_used, f_stats.player_demand, treatment.retail_price )
                # log.info("Player.PR, rev, value_cum:{}".format(value_cum))
                set_total_cost_value(f_stats, value_cum)

    else: # p_stats.role == Player.PR:
        # log.info("PR! Player:{}".format(p_stats.player))

        if first_offer_tiepe == Offer.BUY:
            # log.info("first_offer_tiepe:{} (BUY)".format(first_offer_tiepe))
            # STAND PR for p: p is a PR, and the counterparty bought, so PR p sold
            p_stats.vouchers_used, p_stats.vouchers_negative = cv_STAND(p_stats.vouchers_used, p_stats.vouchers_negative, unitsCleared)
            value_cum = get_value_cum_PR(auction, p_stats.vouchers_used)
            set_total_cost_value(p_stats, value_cum)
            if f_stats.role == Player.PR:
                # log.info("PR! Player:{}".format(f_stats.player))
                # REV PR for f: f is a PR and bought
                f_stats.vouchers_used, f_stats.vouchers_negative = cv_REV(f_stats.vouchers_used, f_stats.vouchers_negative, unitsCleared)
                value_cum = get_value_cum_PR(auction, f_stats.vouchers_used)
                set_total_cost_value(f_stats, value_cum)
            else:
                # STAND RE for f: f is a RE and bought
                # log.info("RE! Player:{}".format(f_stats.player))
                f_stats.vouchers_used, f_stats.vouchers_negative = cv_STAND(f_stats.vouchers_used, f_stats.vouchers_negative, unitsCleared)
                value_cum = get_value_cum_RE(f_stats.vouchers_used, f_stats.player_demand, treatment.retail_price)
                # cv_STAND_RE(f_stats, unitsCleared,treatment)
                set_total_cost_value(f_stats, value_cum)
        else:
            # log.info("first_offer_tiepe:{} (SELL)".format(first_offer_tiepe))
            #first_offer_tiepe == Offer.SELL:
            # REV PR for p: p is a PR, and the counterparty sold, so PR p bought
            p_stats.vouchers_used, p_stats.vouchers_negative = cv_REV(p_stats.vouchers_used, p_stats.vouchers_negative, unitsCleared)
            value_cum = get_value_cum_PR(auction,p_stats.vouchers_used)
            set_total_cost_value(p_stats, value_cum)
            if f_stats.role == Player.PR:
                # REV PR for f: f is a PR and bought WRONG!!!
                # STAND PR for f: f is a PR and bought
                f_stats.vouchers_used, f_stats.vouchers_negative = cv_STAND(f_stats.vouchers_used, f_stats.vouchers_negative, unitsCleared)
                value_cum = get_value_cum_PR(auction,f_stats.vouchers_used)
                set_total_cost_value(f_stats, value_cum)
            else:
                # STAND RE for f: f is a RE and bought WRONG!!!
                # REV RE for f: f is a RE and bought
                f_stats.vouchers_used, f_stats.vouchers_negative = cv_REV(f_stats.vouchers_used, f_stats.vouchers_negative, unitsCleared)
                value_cum = get_value_cum_RE(f_stats.vouchers_used, f_stats.player_demand, treatment.retail_price)
                set_total_cost_value(f_stats, value_cum)
    f_stats.units_missing = f_stats.get_units_missing_tot()
    p_stats.units_missing = p_stats.get_units_missing_tot()

    to_update = [f_stats, p_stats]
    # log.info("bulk_update")
    bulk_update(to_update, exclude_fields=['created', 'auction_id', 'group_id', 'period_id', 'player_id'])
    return p_stats, f_stats
    # f_stats.save()
    # p_stats.save()
    # log.info("missing units p:{}".format(p_stats))
    # log.info("missing units f:{}".format(f_stats))


def clear_offer_smaller(smaller_one, larger_one):
    # to_be_set.cleared = True
    # to_be_set.unitsCleared = to_be_set.unitsAvailable
    # to_be_set.priceCleared = first.priceOriginal
    # to_be_set.unitsAvailable = 0  # this is the part of the original offer that is cleared
    # to_be_set.timeCleared = timezone.now()
    return True, smaller_one.unitsAvailable, larger_one.priceOriginal, 0 , timezone.now()
# to_be_set.cleared, to_be_set.unitsCleared,to_be_set.priceCleared,to_be_set.unitsAvailable,to_be_set.timeCleared =


def clear_offer_larger(larger_one, smaller_one):
    # to_be_set.cleared = True
    # to_be_set.unitsCleared = smaller.unitsCleared
    # to_be_set.priceCleared = first.priceOriginal
    # to_be_set.unitsAvailable = 0  # this is the part of the original offer that is cleared
    # to_be_set.timeCleared = timezone.now()
    return True, smaller_one.unitsCleared, larger_one.priceOriginal,0,timezone.now()
# to_be_set.cleared, to_be_set.unitsCleared,to_be_set.priceCleared,to_be_set.unitsAvailable,to_be_set.timeCleared =


# set_products(c.offer_tiepe, first.unitsCleared, first.priceCleared)
def set_products(offer_tiepe, unitsCleared, priceCleared):
    if offer_tiepe == Offer.SELL:
        c_product = unitsCleared * priceCleared
    else:
        c_product = -1 * unitsCleared * priceCleared
    first_product = -1 * c_product
    return c_product,first_product

# # p_stats.trading_result, f_stats.trading_result, c.product, first.product = stats_calculations(c.offer_tiepe, first.unitsCleared, first.priceCleared, p_stats_trading_results, f_stats_trading_results)
# def stats_calculations(c_offer_tiepe, unitsCleared, priceCleared):
#     if c_offer_tiepe == Offer.SELL:  # thus player p is selling and thus first is a buying offer
#         p_stats_trading_result_change = unitsCleared * priceCleared
#     else:
#         p_stats_trading_result_change = -1 * unitsCleared * priceCleared
#     f_stats_trading_result_change = -1 * p_stats_trading_result_change
#     return p_stats_trading_result_change , f_stats_trading_result_change
#
#
#     c_product = p_stats_trading_result_change
#     first_product = -1 * p_stats_trading_result_change
# # p_stats.trading_result, f_stats.trading_result, c.product, first.product = stats_calculations(c.offer_tiepe, first.unitsCleared, first.priceCleared, p_stats_trading_results, f_stats_trading_results)
#
# def stats_calculations(c_offer_tiepe, unitsCleared, priceCleared):
#     if c_offer_tiepe == Offer.SELL:  # thus player p is selling and thus first is a buying offer
#         c_product = unitsCleared * priceCleared
#     else:
#         c_product = -1 * unitsCleared * priceCleared
#     first_product = -1 * c_product
#     return c_product, first_product


# def stats_calculations(c, first, p_stats, f_stats):
#     p_stats_trading_result = Offer.setproducts(c, first)
#     # log.info('p_stats_trading_result 1',p_stats_trading_result)
#     p_stats.trading_result += p_stats_trading_result
#     # log.info('p_stats_trading_result 2', p_stats_trading_result)
#     c.product = p_stats_trading_result
#     # log.info('p_stats_trading_result 3', p_stats_trading_result)
#     # log.info('c.product', c.product )
#     f_stats.trading_result -= p_stats_trading_result
#     first.product = -1 * p_stats_trading_result
#     # c.save()
#     # first.save()

def assign_leftover(RE_per_group,leftover_RE, demand_share_RE):
    demand_share_list_RE = []
    # print(f"RE_per_group +1:{RE_per_group +1}")
    for i in range(1,RE_per_group +1):
        # print(f"i:{i}")
        if leftover_RE > 0:
            demand_share_list_RE.append(demand_share_RE + 1)
            leftover_RE -= 1
        else:
            demand_share_list_RE.append(demand_share_RE)
    random.shuffle(demand_share_list_RE)
    # print(f"demand_share_list_RE:{demand_share_list_RE}")
    return demand_share_list_RE

# demand_share_PR, leftover_PR  =
def divideTotal(demand_draw, PR_per_group ):
    return demand_draw // PR_per_group, demand_draw % PR_per_group
    # return demand_share, leftover

def checkMaxObey(demand_share_elt_RE,max_vouchers, demand_curtailment_warning):
    return min(demand_share_elt_RE,max_vouchers),(demand_share_elt_RE >  max_vouchers) or demand_curtailment_warning
    #
    # if demand_share_elt_RE >  max_vouchers:
    #     return max_vouchers, True
    #     # player_stats.player_demand = treatment.max_vouchers
    #     # # log.info("WARNING!!! Demand has been curtailed!!!")
    #     # auction.demand_curtailment_warning = True
    # else:
    #     return demand_share_elt_RE, False
