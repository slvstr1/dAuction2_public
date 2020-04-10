from django.shortcuts import render
# from dAuction2.models import Offer, Player, Voucher
import logging, time, random
from forward_and_spot.views import set_offer
from django.http import JsonResponse

from distribution.models import Distribution
from forward_and_spot.models import  Treatment, Offer, Voucher, Player_stats,Phase, Timer, Auction, Player
# from forward_and_spot.models import  User
from master.functions import merge_dicts
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# from master.models import MasterMan
from django.core.cache import cache

debug_logger = logging.getLogger('debug_logger')
log = logging.getLogger(__name__)


# DATAANALYSIS
# put ANL in its own app?
from .serializers import AnlGroupStatsSer, AnlPeriodSer, AnlOfferSer, AnlPlayerStatsSer, AnlPlayerSer,AnlTreatmentSer, AnlPhaseSer, AnlAuctionSer
from forward_and_spot.models import Period, Group
# get data about passed auction for ANL spp
def analysis_data(request):
    if request.method == 'GET':
        # only results from the active auction are send!
        auction = Auction.objects.get(active=True)
        auction_ser = AnlAuctionSer(auction)
        offers = AnlOfferSer(Offer.objects.all().filter(auction=auction.id), many=True)
        periods = AnlPeriodSer(Period.objects.all().filter(auction=auction.id), many=True)
        phase = AnlPhaseSer(Phase.objects.all().filter(auction=auction.id), many=True)
        player = AnlPlayerSer(Player.objects.all().filter(auction=auction.id), many=True)
        treatment = AnlTreatmentSer(Treatment.objects.all().filter(id=auction.treatment_id), many=True)
        player_stats = AnlPlayerStatsSer(Player_stats.objects.all().filter(auction=auction.id), many=True)
        group = AnlGroupStatsSer(Group.objects.all().filter(auction=auction.id), many=True)

        data = {"group": group.data, "player_stats": player_stats.data, "auction": auction_ser.data,
                'offers': offers.data, 'periods': periods.data, 'phase': phase.data, 'player': player.data,
                'treatment': treatment.data[0]}
        return JsonResponse(data)


def market(request):
    return render(request, 'anl/market.html', {})

def results(request):
    return render(request, 'anl/results.html', {})




