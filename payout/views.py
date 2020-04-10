#!python3

from django.shortcuts import render, render_to_response

## imports for user login
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
##
from forward_and_spot.models import Auction, Player, Period, Treatment
from .functions import determine_payment, auction_pay_removed
# from master.functions_main import  cache_me
# from master.functions_earnings import determine_payment_statistics
import logging
from master.models import MasterMan

log = logging.getLogger(__name__)

@login_required(redirect_field_name="login", login_url='master-login_user')
def main(request,tmpl='payout/main.html', data={}):
    log.info("payout here!!!")
    if not Auction.objects.exists():
        log.info("return redirect(master-main)")
        return redirect("master-main")
    auction, treatment = Auction.cache_or_create_auction()
    if not Player.objects.exists():
        auction.app=0
        auction.save_and_cache()
        log.info("not Player_stats.objects.exists()")
        return redirect("master-main")

    # no way back / way back
    user=request.user
    log.info("request.user:{}".format(request.user))
    try:
        player = user.player.get(auction=auction)
    except Player.DoesNotExist:
        log.info("not Player_stats.objects.exists()")
        auction.app = 0
        auction.save_and_cache()
        log.info("not Player_stats.objects.exists()")
        return redirect("master-main")

    # print("player.app:{}".format(player.app))
    # print("auction.app:{}".format(auction.app))
    if player.app != Player.PAYOUT and auction.app != Auction.PAYOUT:
        log.info("if player.app != Player.PAYOUT :1")
        return redirect('master-main')

    if auction.removing:
        if not player.selected:
            data = auction_pay_removed(request, treatment, auction, player)
            return render(request, 'payout/main.html', context=data)
        # auction_pay_removed()
    else:
        if player.app != Player.PAYOUT:
            log.info("player.app != Player.PAYOUT2")
            return redirect("master-main")

    player.PAYOUT_app()
    master_man = MasterMan.cache_or_create_mm()
    master_man.show_payments = False

    data ={'show_payments':master_man.show_payments,'after_message':"Please wait a moment, we are preparing the payments of the earnings of all participants. We will soon announce that the payment can start and you can, one by one, come and collect your payment in the experimentor room."}
    log.info("player:{}".format(player))
    last_round = Period.objects.filter(auction=auction, finished=True).last()

    if not last_round:
        log.info("round object does not exist")
    else:
        if player.payout_CZK== -1:
            determine_payment(treatment, auction, player)
            auction = auction.determine_payment_statistics()
            auction.save_and_cache()
            # MasterMan.cache_me('auction', auction)
            # group_id = player.group_id
        data.update({'treatment':treatment,'player':player,"auction":auction,"user": user})
        log.info("data: {}".format(data))

    log.info("data: {}".format(data))
    MasterMan.cache_it('context',data)
    return render(request, tmpl, context=data)