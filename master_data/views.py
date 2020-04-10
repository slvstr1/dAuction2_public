#!python3
import os.path
import logging
# from dAuction2.settings import *
import gzip, time, random
import os
import csv
from dAuction2.settings import BASE_DIR
from django.http import HttpResponse

from dAuction2.settings.base import BASE_DIR
# import pandas as pd
import glob
from master.models import MasterMan
log = logging.getLogger(__name__)
from django.shortcuts import render
from django.core.cache import cache
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms_data import DataForm
from forward_and_spot.models import Treatment
from django.core import management
from django.db import transaction
from .functions import get_list_sizedir, populate_uid,  make_excel_csv
from forward_and_spot.models import Auction
from dAuction2.models import User
from master.models import MasterMan

logger = logging.getLogger(__name__)
debug_logger = logging.getLogger('debug_logger')




@login_required(redirect_field_name="login", login_url='master-login_user')
def main2(request, tmpl='', data={}):
    # print("on master data main2")

    # log.info('master-main(request): ', request)
    # preferably ONLY here the first auction is ever created!
    # listdir = os.listdir('dbs_saved_json')
    # print("BASE_DIR:{}".format(BASE_DIR))
    # print(os.path.join(BASE_DIR,'dbs_saved_json', "{}.json".format(filename))
    # listpath = [os.path.join(BASE_DIR, 'dbs_saved_json', name) for name in listdir]
    # somelist = [os.path.join(BASE_DIR,  name) for name in listdir]

    #
    # listdir = sorted(os.listdir('dbs_saved_json'), reverse=True)
    # list_sizedir = [[name, convert_size(os.path.getsize(os.path.join(BASE_DIR, 'dbs_saved_json', name)))] for name in listdir]

    # dir_name = 'dbs_saved_json'
    list_sizedir = get_list_sizedir(dir_name='dbs_saved_json')
    # log.info("listdir:{}".format(listdir))
    log.info("list_sizedir:{}".format(list_sizedir))
    log.info("no list_sizedir:{}".format(len(list_sizedir)))
    start = time.time()
    user = request.user
    log.info("sub on main: {} and logged_in:{}".format(user, user.logged_in))
    log.info("sub on main 1")
    need_refreshing_set = cache.get('need_refreshing_set')
    # log.info("need_refreshing_set_ main 1: {}".format(need_refreshing_set))

    admin = cache.get("admin")
    if not admin:
        admin = User.objects.get(pk=99)
        cache.set("admin", admin)
    # treatment= Treatment.cache_or_create_treatment()
    auction, treatment = Auction.cache_or_create_auction()

    log.info("auction: {}".format(auction))
    log.info("sub on main 3")
    if not auction:
        if Auction.objects.exists():
            auction = Auction.objects.get(active=True)
    log.info("auction.auction_created={}".format(auction.auction_created))
    log.info("sub on main 4")
    if user.pk != 99:  # thus not admin
        raise Exception("player in data!!!???")

    # beyond this point only Admin dwells (subjects have been redirected to Instructions-main)
    # gives:
    # CacheKeyWarning: Cache key contains characters that will cause errors if used with memcached: ':1:MasterMan object'   'used with memcached: %r' % key, CacheKeyWarning
    master_man = MasterMan.cache_or_create_mm()
    # print("master_man.view:{}".format(master_man.view))
    # print("type(master_man):{}".format(type(master_man)))
    if master_man.view == auction.SANL:

        BASE_DIR2 = os.path.dirname(os.path.abspath(__file__))

        # print("BASE_DIR2:{}".format(BASE_DIR2))
        # data = open()

        # with open(os.path.join(BASE_DIR2, "config.json")) as f:
        #     conf = json.load(f)
        #
        # print("conf:{}".format(conf))
        # conn_str = "host={} dbname={} user={} password={}".format(conf['host'], conf['database'],conf['user'] , conf['passw'])
        # print("conn_str:{}".format(conn_str))
        # import psycopg2
        # conn = psycopg2.connect(conn_str)
        # print("conn:{}".format(conn))
        # import pandas as pd
        # start = time.time()
        # df = pd.read_sql('SELECT * FROM "dAuction2_offer" WHERE cleared=TRUE'           , con=conn)
        # print("time:{}".format(time.time() - start))
        # df.info()
        #

        # from dbs_saved_json_helper_files.svk_example import load_data2, analyze
        # analyze_list = (558585, 567210, 471943)
        # for auction_id in analyze_list:
        #     d = load_data2(auction_id)
        #     analyze(a)
        data_update = {}
    auction_details = Auction.objects.all().order_by('-pk').select_related('treatment')
    dataForm = DataForm(initial={'pk': auction.pk, 'is_part_experiment': auction.is_part_experiment,
                                 'particular_info': auction.particular_info}, instance=auction)
    # time_now = int(time.time())
    master_man.view = auction.DATA
    master_man.save_and_cache()
    if master_man.view == auction.DATA:
        data = {
            "auction": auction,
            'view': master_man.view,
            'master_man':master_man
        }
        data.update({
            "auction_details": auction_details, 'list_sizedir': list_sizedir, 'dataForm': dataForm})
    # print("before the render")
    return render(request, 'master/master.html', context=data)




@login_required(redirect_field_name="login", login_url='master-login_user')
@transaction.atomic
def data_handler(request, tmpl='master_data_main', data={}):
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.
    start = time.time()
    log.info("POST---{}".format(request.POST))
    if request.POST:
        log.info("request.POST TRUE")
        log.info(request.POST)
        auction, treatment = Auction.cache_or_create_auction()

        if 'submit_dataForm' in request.POST:
            log.info("submit_dataForm")
            form = DataForm(request.POST or None, instance=auction)
            if form.is_valid():
                form.save()
                auction.save_and_cache()

                # MasterMan.cache_me("auction",auction)
                log.info("saved form of DataForm:{}".format(form))



        elif ('select_auction' in request.POST) or ('delete_auction' in request.POST):
            # print("request.POST:{}".format(request.POST))
            log.info("('select' or 'delete') in request.POST:")
            pk = int(request.POST['q'])
            # log.info('request.GET', request.GET)

            log.info("pk:{}".format(pk))
            selected_auction = Auction.objects.get(pk=pk)
            if 'select_auction' in request.POST:
                # log.info (request.POST)
                log.info("('select' in request.POST:")
                unselected_auctions = Auction.objects.filter(active=True)
                for ua in unselected_auctions:
                    ua.active = False
                    ua.save()
            elif "delete_auction" in request.POST:
                log.info("'delete' in request.POST:")
                # log.info("auction_delete1")
                selected_auction.auction_delete()
                cache.set('voucher_list', '')
                cache.set('vouchers_ser', '')
                MasterMan.invalidate_caches()

                # auction_delete(selected_auction)
                log.info("auction_delete2")
                if Auction.objects.exists():
                    selected_auction = Auction.objects.all().last()
                    log.info("auction=Auction.objects.all().last()")
                else:
                    log.info("auction=Auction.create()1")
                    # tr = Treatment.cache_or_create_treatment()
                    selected_auction = Auction.create()
                    log.info("auction=Auction.create()2")

            selected_auction.active = True
            # selected_master_man.view = 3
            selected_auction.save_and_cache()
            # MasterMan.cache_me("auction", selected_auction)

        elif 'session_new' in request.POST:
            # print("session_new2")
            Auction.session_new(auction, treatment)

        elif 'populate_uid' in request.POST:
            populate_uid(auction, treatment)


        elif 'db_save' in request.POST:
            # db_save(auction)
            log.info("db_save2!!!")
            auction.db_save()

        # elif "load_selected_pg" in request.POST:
        #     # pass

        elif ("load_pg" in request.POST) or ("load_selected_pg" in request.POST):

            # print("request.POST:{}".format(request.POST))
            if ("load_pg" in request.POST):
                listdir = sorted(os.listdir('dbs_saved_json'),reverse=True)
            else:
                listdir = request.POST.getlist('q')
                # print("listdir = request.POST['q']:{}".format(listdir ))

                # return redirect(tmpl)
            log.info("listdir ---:{}".format(listdir))
            if listdir:
                for file in listdir:
                    filename = os.path.join('dbs_saved_json',file)
                    log.info("filename:{}".format(filename))
                    management.call_command('loaddata', filename)

                treatment.active = True
                auction.active = True
                auction.save_and_cache()
                treatment.save_and_cache()
                auction_list = Auction.objects.prefetch_related('treatment').all()
                for auction in auction_list:
                    auction.add_au_id_to_treatment()
                Auction.objects.exclude(pk=auction.pk).update(active=False)
                # Treatment.objects.exclude(pk=treatment.pk).update(active=False)
            return redirect(tmpl)

        elif "db_save" in request.POST:
            log.info("db_save2!!!")
            auction.db_save()
            return redirect(tmpl)

        elif "excel_csv_active" in request.POST or "excel_csv_all" in request.POST:
            if "excel_csv_active" in request.POST:
                auction_list = [auction,]
                filename = "data_auction_{}_ {}".format(auction.id, MasterMan.get_time_stamp())
                # filename = os.path.join('dbs_saved_json',"data_auction_{}".format(auction.id))
                # os.path.join('dbs_saved_json', file)
            elif "excel_csv_all" in request.POST:

                auction_list = list(Auction.objects.all())
                filename = "data_multi_auction_{}".format(MasterMan.get_time_stamp())

            response = make_excel_csv(treatment, auction_list,filename,tmpl)

            end = time.time() - start
            log_string = "def data_handler:{}".format(round(end, 4))
            log.info(log_string)

            return response
    return redirect(tmpl)



def subject_select(request, tmpl='master-main', data={}):
    # from forward_and_spot.models import Player
    start = time.time()
    # print("subject_select__")
    if request.POST:
        log.info("POST:".format(request.POST))
        # print("POST:".format(request.POST))
        auction= Auction.cache_get()
        # auction = Auction.objects.get(active=True)
        if 'q' in request.POST:
            try:
                pk = int(request.POST['q'])
                selected_user = User.objects.get(pk=pk)
            except:
                selected_user=None
                # log.info("NONE")
        else:
            selected_user =None
        master_man = MasterMan.cache_or_create_mm()

        master_man.toggler(request.POST)

        if 'logout' in request.POST and selected_user:
            # log.info("delete is in request.oist")
            log.info("logout, selected_user.pk:{}".format(selected_user.pk))
            # selected_user.LOGGED_OUT(auction)

            # player=Player.objects.filter(auction=auction,user=selected_user).update(user=None)

            if not (selected_user.id == 99):
                selected_user.logged_in = False
                # print("self.logged_in = False__ in subject_select")
                selected_user.fail = False
                selected_user.ip = ""
                selected_user.last_player = None

            selected_user.save()
            key_user = str(selected_user.id)
            # key_user = selected_user.id
            need_refreshing_set = cache.get("need_refreshing_set")
            if not need_refreshing_set:
                need_refreshing_set = set()
            need_refreshing_set.add(key_user)
            # log.info("user",user)
            # log.info("key_player:{}".format(key_user))
            cache.set('need_refreshing_set', need_refreshing_set, 35)
        # elif 'show_table' in request.POST:
        #     # auction.show_table = not auction.show_table
        #     print("masterman")
        #     raise Exception ("should not be called show_table")
        #     # master_man = MasterMan.cache_or_create_mm()
        #     # master_man.show_table()
        #     # master_man.show_table = not master_man.show_table
        #     # master_man.save_and_cache()
        elif 'name' in request.POST:

            if 'show_selection_toggle' in request.POST['name']:
                master_man = MasterMan.cache_or_create_mm()
                master_man.show_selection_toggle()
                # print("toggle_")
            # raise Exception("should not be called show_selection_toggle")
            # master_man = MasterMan.cache_or_create_mm()
            # # master_man.show_unselected = not master_man.show_unselected
            # master_man.show_payments_int = (master_man.show_payments_int + 1) // 3
            # master_man.save_and_cache()
        # elif 'sh_show_selected' in request.POST:
        #     master_man = MasterMan.cache_or_create_mm()
        #     master_man.show_selected = not master_man.show_selected
        #     master_man.save_and_cache()
        auction.save()
        auction.save_and_cache()
    end = time.time() - start
    log_string = "def subject_select: " + str(round(end, 4)) + "for user_id: " + str(request.user.id)
    log.info(log_string)
    return redirect(tmpl)