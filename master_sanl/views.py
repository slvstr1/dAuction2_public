#!python3
import logging, os
log = logging.getLogger(__name__)
try:
    import pandas as pd
    pandas_installed = True
except ImportError:
    log.info("Pandas not installed")
    pandas_installed = False


from django.shortcuts import render
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from dAuction2.settings.base import BASE_DIR
from master_data.functions import get_list_sizedir
from forward_and_spot.models import Auction
from master.models import MasterMan
from dAuction2.models import User
from .functions import load_data, feedback

logger = logging.getLogger(__name__)
debug_logger = logging.getLogger('debug_logger')
# from master_data.functions import convert_size


@login_required(redirect_field_name="login", login_url='master-login_user')
def main_sanl(request, tmpl='', data={}):
    log.info("on sanl")

    master_man = MasterMan.cache_or_create_mm()
    # treatment = Treatment.cache_or_create_treatment()
    auction, treatment = Auction.cache_or_create_auction()
    log.info("master_man.view:{}".format(master_man.view))
    list_sizedir = get_list_sizedir(dir_name='dbs_saved_json_helper_files/feedback')
    # log.info("listdir:{}".format(listdir))
    log.info("list_sizedir:{}".format(list_sizedir))

    context = {
        'list_sizedir': list_sizedir,
        "auction": auction,
        'treatment': treatment,
        'view': master_man.view,
        'master_man':master_man,
        'pandas_installed':pandas_installed
        # 'df': df,
    }

    log.info("master_man.view:{}".format(master_man.view))
    tmpl = 'master/master.html'
    # master_sanl
    return render(request, tmpl, context=context)

def master_sanl_handler(request, tmpl='master-main', data={}):
    if request.POST:
        # auction = Auction.objects.get(active=True)
        master_man = MasterMan.cache_or_create_mm()
        if 'create_xls' in request.POST:
            log.info("BASE_DIR:{}".format(BASE_DIR))
            file_list = sorted(os.listdir('dbs_saved_json'), reverse=True)

            log.info("1. os.getcwd():{}".format(os.getcwd()))

            auction_ids = [file_name.split("_", 2)[1] for file_name in file_list]
            log.info("auction_ids:{}".format(auction_ids))
            log.info("file_list:{}".format(file_list))
            user = request.user
            need_refreshing_set = cache.get('need_refreshing_set')
            # log.info("need_refreshing_set_ main 1: {}".format(need_refreshing_set))

            admin = cache.get("admin")
            if not admin:
                admin = User.objects.get(pk=99)
                cache.set("admin", admin)
            # treatment = Treatment.cache_or_create_treatment()
            auction, treatment = Auction.cache_or_create_auction()
            log.info("treatment: {}".format(treatment))
            log.info("auction: {}".format(auction))

            master_man = MasterMan.cache_or_create_mm()
            master_man.view = MasterMan.SANL
            master_man.save_and_cache()

            pd.set_option('display.expand_frame_repr', False)
            model_list = ['forward_and_spot.player', 'forward_and_spot.auction']
            # file_list = glob.glob('dbs_saved_json/*auction_*.json.gz')
            log.info("file_list:{}".format(file_list))
            log.info("auction_ids:{}".format(auction_ids))

            # execute feedback function for each auction_id
            # ! assumed to be string in this case
            # dataframe with collected feedback from all auctions
            df = pd.DataFrame()
            for auction_file in file_list:
                log.info("just before load_data")
                log.info("auction_file:{}".format(auction_file))
                d = load_data(auction_file, model_list)
                f = feedback(auction_file, d)

                # append to all auctions dataframe
                df = df.append(f, ignore_index=True)

            # resort and output
            df.sort_values(by=['selected', 'testing_errors'], inplace=True, ascending=(False, True))
            filename = "dbs_saved_json_helper_files/feedback/" + "f_all" + '.csv'
            df.to_csv(filename)
            # print("done")
            context = {
                "auction": auction,
                'treatment': treatment,
                'view': master_man.view,
                'df': df,
            }

            return render(request, tmpl, context=context)


