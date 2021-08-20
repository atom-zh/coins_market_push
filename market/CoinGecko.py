import os
import sys
import pathlib
project_path = str(pathlib.Path(os.path.abspath(__file__)).parent.parent)
sys.path.append(project_path)

from config.system import CoinGK
from utils.utils import save_json, load_json
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
coin_dict = {}

def gen_coin_list():
    coin_lists = {'data': []}
    lists = cg.get_coins_list()
    for line in lists:
        tmp = dict()
        tmp['id'] = line['id']
        tmp['symbol'] =  line['symbol']
        tmp['name'] = line['name']
        coin_lists['data'].append(tmp)
    save_json(coin_lists, CoinGK.PATH_JSON)

def get_conin_seq(symbol):
    global coin_dict
    if not os.path.isfile(CoinGK.PATH_JSON):
        gen_coin_list()
    coin_dict = load_json(CoinGK.PATH_JSON)
    for list in coin_dict['data']:
        if list['symbol'] == symbol.lower():
            return list['id']
    return -1

def get_market(symbol):
    ids = get_conin_seq(symbol)
    print(ids)
    ret = cg.get_price(ids=ids, vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)
    print(ret)
    send_msg = symbol.upper() + '\n' +\
                '价格 :' + ' $' + str(ret[ids]['usd']) + '\n' + \
                '24H涨跌幅: ' + str('%.2f' % ret[ids]['usd_24h_change']) + '%'
    print(send_msg)
