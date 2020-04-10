#!python3
import bisect
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from forward_and_spot.models import Auction,  Treatment, Player, Voucher, VoucherRE
from .functions import  get_all_pageurls, get_rendered_page

import logging
from master.models import MasterMan
log = logging.getLogger(__name__)
# from django.contrib.auth import get_user_model


@login_required(redirect_field_name="login_user", login_url='master-login_user')
def main(request, tmpl='instructions/subject_intro.html', data={}):
    # log.info("instructions_main")
    user = request.user
    if not user.logged_in:
        log.info("user {} not logged in".format(user))
        return redirect("master-main")

    # treatment = Treatment.cache_or_create_treatment()
    auction, treatment = Auction.cache_or_create_auction()
    if auction:
        if auction.removing:
            player = user.player.get(auction=auction)

            if not player.selected:
                player.app = Player.QUEST
                player.save()
                return redirect('questionnaire-main')

        if auction.app == Auction.FS:
            player = user.player.get(auction=auction)
            if player.selected:
                return redirect('forward_and_spot-main')
        elif auction.app == Auction.DISTR:
            return redirect('distribution-main')
        elif auction.app == Auction.TESTING:
            return redirect('testing-main')

        elif auction.app == Auction.QUEST:
            return redirect('questionnaire-main')
        elif auction.app == Auction.PAYOUT:
            log.info("elif auction.app == Auction.PAYOUT:")
            return redirect('payout-main')
    else:
        log.info('redirect')
        return redirect('master-main')
    if user.username == 'admin':
        raise ValueError('Admin got into instructions')
    else:
        try:
            player = user.player.get(auction=auction)
        except Player.DoesNotExist:
            return redirect("master-main")

    log.info("landed on main, user:{}, playerid:{}, group:{}".format(user, player, player.group))
    if auction.removing and not player.selected:
        return redirect('master-main')

    if auction.app == Auction.INSTR:
        page_list = cache.get("page_list")
        if not page_list:
            # Specify here the pages for full (all of them) and a part of them
            # log.info("itype:{}".format(auction.itype))
            if auction.itype == auction.FULL_INSTR:
                if treatment.only_spot:
                    page_list = (1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,  27,28, 29, 30, 31, 32, 33, 34, 35)
                else:
                    page_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35)
            else:
                if treatment.only_spot:
                    page_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 18, 19, 20, 25, 27, 28, 33, 34, 35)
                else:
                    page_list = (1, 2, 3, 5, 6, 7, 8, 9, 12, 13, 18, 19, 20, 25, 26, 27, 28, 33, 34, 35)
            MasterMan.cache_me(page_list, "page_list")
            log.info("made page_list")
            # print("made page_list")
            all_pages_list = get_all_pageurls(page_list, auction.itype,treatment.educational)
            MasterMan.cache_me(all_pages_list, "all_pages_list")
        if player.page == 0 or player.app != Player.INSTR:
            player.INSTR_app()
        render_object = get_rendered_page(treatment, auction, request, player)
        # print("render_object:{}".format(render_object))
        return render_object
    # player.save()

    data.update({'player': player, "auction": auction, 'treatment': treatment})
    tmpl = 'instructions/subject_intro.html'
    return render(request, tmpl, data)


def page(request, tmpl='instructions-main', data={}):
    if request.GET:
        page_list = cache.get("page_list")
        if not page_list:
            tmpl = 'instructions-main'
            return redirect(tmpl)
        # treatment = Treatment.cache_or_create_treatment()
        auction, treatment = Auction.cache_or_create_auction()
        user = request.user
        player = user.player.get(auction=auction)
        if "Next" in request.GET:
            if player.page < page_list[-1]:
                player.page = page_list[bisect.bisect_right(page_list, player.page, lo=1)]
        elif "Previous" in request.GET:
            if player.page > 1:
                player.page = page_list[bisect.bisect_right(page_list, player.page-1, lo=1)-1]
        elif "FINISH" in request.GET:
            log.info("finish!")
            player.state=3
            player.save(update_fields=['state'])
            return redirect(tmpl)
        else:
            if "value" in request.GET:
                i = int (request.GET["value"])
                player.page = i
                player.save(update_fields=['page'])
        player.save()
    # log.info("page.idd",page.idd)
    # log.info("player.page", player.page)
    return redirect(tmpl)