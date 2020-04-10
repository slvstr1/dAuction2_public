#!python3
from django.shortcuts import render, redirect
from django.core.cache import cache
from api.serializers import sVSerializer, sTreatmentSerializer
from forward_and_spot.models import Auction,  Treatment, Player, Voucher, VoucherRE
import logging
from master.models import MasterMan

log = logging.getLogger(__name__)



def get_all_pageurls(page_list, itype, educational):
    all_pageurls = []
    for page in page_list:
        # pageurls += [[page,str(assing_pageurl(page, itype, educational)).split()[0],]]
        all_pageurls += [assing_pageurl(page, itype, educational)]
    # print("all_pageurls:{}".format(all_pageurls))
    return all_pageurls


def assing_pageurl(player_page, itype, educational):
    if educational:
        # basestring="instructions/pages_context/page"
        basestring = "instructions/pages/page"
        if player_page < 10:
            basestring = "{}0".format(basestring)
    else:
        basestring = "instructions/pages/page"
        if player_page < 10:
            basestring = "{}0".format(basestring)
    return [player_page,"{}{}.html".format(basestring, player_page)]

# def multiply(qty, unit_price, *args, **kwargs):
#     # you would need to do any localization of the result here
#     return qty * unit_price


def get_rendered_page(treatment, auction, request, player):

    def total_of_list(voucher_list):
        # from django.db.models import Sum
        voucher_calc = 0
        if voucher_list:
            for voucher in voucher_list:
                voucher_calc += voucher.value
        return voucher_calc

    page_list = cache.get("page_list")
    if not page_list:
        tmpl = 'instructions-main'
        log.info("page_list empty")
        # print("page_list empty")
        return redirect(tmpl)

    instruction_totalPages = page_list[-1]
    pageurl = assing_pageurl(player.page, auction.itype, treatment.educational)
    # print("pageurl:{}".format(pageurl))
    # ToDo: pageurl should be replaced with standard solution, see: https://stackoverflow.com/questions/23114648/django-url-template-tag-with-variable
    voucher_list = Voucher.get_voucher_list(auction, "voucher_list")
    # print("voucher_list:{}".format(voucher_list))
    # for voucher in voucher_list:
    #     print("voucher:{}, type:{}".format(voucher, type(voucher)))
    voucher_list7 = voucher_list[1:7]
    voucher_list_1 = voucher_list[0:10]
    voucher_list_2 = voucher_list[10:35]
    voucher_list5 = voucher_list[1:5]

    voucher_calc = total_of_list(voucher_list7)
    voucher_calc5 = total_of_list(voucher_list5)

    voucher_listRE = VoucherRE.get_voucher_list(auction, "voucher_listRE")

    treatment_ser_data = cache.get("treatment_ser_data")
    if not treatment_ser_data:
        treatment = Treatment.cache_get()
        treatment_ser = sTreatmentSerializer(treatment)
        treatment_ser_data = treatment_ser.data
        MasterMan.cache_it("treatment_ser_data", treatment_ser_data)

    if treatment.educational:
        forward_market="the Forward Market"
        spot_market = "the Spot Market"
        Forward_market = "The Forward Market"
        Spot_market = "The Spot Market"
        # experiment = "Business Game"
    else:
        forward_market = "Stage 1"
        spot_market = "Stage 2"
        Forward_market = forward_market
        Spot_market = spot_market


    src_file_exists, src_name_list = treatment.hardcoded_pics

    src_file02b = src_name_list[0]
    src_file18 = src_name_list[1]
    src_file19 = src_name_list[2]

    tmpl = 'instructions/subject_intro.html'
    group_id = player.group_id
    # player_list = Player.objects.filter(auction=auction, user__isnull=False)
    # log.info("player.pageurl:{}".format(player.pageurl))
    filename = "data_auction_{}_ {}".format(auction.id, MasterMan.get_time_stamp())
    # print("filename:{}".format(filename))

    data = {'src_name_list':src_name_list,'src_file02b':src_file02b, 'src_file18':src_file18,'src_file19':src_file19,
            # 'thispage': thispage,
            # 'page_list': page_list,
            'forward_market':forward_market,
            'Forward_market':Forward_market,
            'spot_market':spot_market,
            'Spot_market': Spot_market,
            'filename':filename,
            'player': player,
            # 'group_id': group_id,
            # 'players': player_list,
            "auction": auction, "voucher_calc": voucher_calc,"voucher_calc5": voucher_calc5, "vouchers_1": voucher_list_1,
            "vouchers_2": voucher_list_2, "vouchersRE": voucher_listRE,
            "instruction_totalPages": instruction_totalPages, 'treatment': treatment,
            "vouchers_js": sVSerializer(voucher_list, many=True).data,
            # "auction_js": merged_auction_ser_data,
           "treatment_js": treatment_ser_data,'pageurl':pageurl
            }
    all_pages_list = cache.get("all_pages_list")
    if not all_pages_list:
        tmpl = 'instructions-main'
        log.info("page_list empty")
        # print("page_list empty")
        return redirect(tmpl)

    data.update({'all_pages_list':all_pages_list})
    # log.info("")
    # log.info("")
    render_object = render(request, tmpl, context=data)
    return render_object