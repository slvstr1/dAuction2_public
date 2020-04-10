#!python3
import time
import random
from django.contrib import messages
from django.shortcuts import render, render_to_response
# from django.http import HttpResponse, JsonResponse
# from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from forward_and_spot.models import Auction
from distribution.models import Distribution
from forward_and_spot.models import Player
#Transaction,
from django.core.cache import cache
# from django.contrib.auth.models import User
# from master.functions_main import merge_dicts
#logger = logging.getLogger(__name__)
import logging
log = logging.getLogger(__name__)
@login_required(redirect_field_name="login", login_url='master-login_user')
def main(request, tmpl='distribution/main.html', data={}):
    if not Auction.objects.exists():
        return redirect("master-main")
    auction, treatment = Auction.cache_or_create_auction()

    if not auction.app == Auction.DISTR:
        return redirect("master-main")
    user = request.user
    player = user.player.get(auction=auction)
    log.info("landed on main, user:{}, playerid:{}, group:{}".format(user, player, player.group))

    if auction.removing and not player.selected:
        return redirect('master-main')
    player.DISTR_app()
    # player.app = Player.DISTR
    # player.page = 0

    # player.save_and_cache()
    # player.save(update_fields=['state','page','app'])

    draws = Distribution.objects.filter(idd__lte=player.draw_id).order_by('-id')[:60]
    draws1 = draws[:30]
    draws2 = draws [31:60]

    # auction = Auction.cache_get()
    log.info(auction)
    treatment_ser_data = cache.get("treatment_ser_data")

    group_id = player.group_id

    data={'draws1':draws1,'draws2':draws2, "auction": treatment_ser_data, "player":player,'group_id': group_id, "treatment": treatment_ser_data }
    # log.info("draw?")

    return render(request, tmpl, context=data)