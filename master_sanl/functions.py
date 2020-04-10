import gzip
import json
import logging
log = logging.getLogger(__name__)
try:
    import pandas as pd
    from pandas import Series
except ImportError:
    log.info("Pandas not installed")

import gzip
import json
import os


# from dAuction2.settings.base import BASE_DIR


# def load_data(auction_id_list,model_list):
def load_data(auction_file,model_list):
    """Load data from file in directory, loads tables present on model list
    """

    def get_models(model_list, data):
        d = {}
        for m in model_list:
            content = []
            for i in range(0, len(data)):
                # if data[i]['model'] == ("dAuction2." + m):
                if data[i]['model'] == m:
                    content.append(data[i])
            if len(content) is not 0:
                d[m] = content
        return d

    # print("BASE_DIR:{}".format(BASE_DIR))

    auction_file_path = os.path.join('dbs_saved_json', "{}".format(auction_file))
    # print("3. os.getcwd():{}".format(os.getcwd()))

    # unzip the file, decode and load as list of dict
    with gzip.open(auction_file_path, 'rb') as f:
        file_content = f.read()
    data = json.loads(file_content.decode('utf-8'))
    d = get_models(model_list, data)

    # clean up to leave only fields inside dicts
    for key in d:
        for i in range(0, len(d[key])):
            d[key][i]['fields']['pk'] = d[key][i]['pk']
            d[key][i] = d[key][i]['fields']

    # make pandas dataframes for each model on modellist
    for m in model_list:
        # print("m:{}".format(m))
        # print("d:{}".format(d))
        # print("d[m]):{}".format((d[m])))
        d[m] = pd.DataFrame.from_dict(d[m])
    return d


def feedback(auction_file, d):
    # d = load_data(auction_id,model_list)
    # load player table
    player = d['forward_and_spot.player']
    # print("pd_player:{}".format(player))

    # load auction table
    pd_auction = d['forward_and_spot.auction']
    # print("pd_auction:{}".format(pd_auction))
    # pd_result = pd.merge(player, pd_auction, on=['auction', 'pk_auction'], how='inner',suffixes=('_phase', '_offer'))
    # gives KeyError: 'auction'

    pd_result = player.merge(pd_auction, left_on='auction', right_on='pk', how='inner',suffixes=('_player', '_auction'))
    # print("pd_result:{}".format(pd_result))
    # sort by selected and testing errors
    player.sort_values(by=['selected', 'testing_errors'], inplace=True, ascending=(False, True))
    pd_result.sort_values(by=['selected', 'testing_errors'], inplace=True, ascending=(False, True))
    # limit output to only selected columns
    # result = player[['auction','selected', 'testing_errors', 'comments', 'do_better_what']]
    # if 'itype' in pd_result.columns:
    #     print("itype in pd_result!")
    #     pass

    if not 'is_part_experiment' in pd_result:
        # print("is_part_experiment not in pd_result")
        pd_result['is_part_experiment'] = Series(True, index=pd_result.index)
        # add 'is_part_experiment' to result with value True

    # limit output to only selected columns
    result = pd_result[
            ['auction','pk_player', 'is_part_experiment', 'selected', 'testing_errors', 'comments', 'do_better_what']]

    # result = pd_result[['auction','is_part_experiment', 'selected', 'testing_errors', 'comments', 'do_better_what']]
    auction_id = auction_file.split("_", 2)[1]
    filename = "dbs_saved_json_helper_files/feedback/" + "f_" + auction_id + '.csv'
    result.to_csv(filename)
    # print("pd_result:{}".format(pd_result))
    return result
