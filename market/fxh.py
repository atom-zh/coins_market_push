import os
import sys
import pathlib
import requests
import json
project_path = str(pathlib.Path(os.path.abspath(__file__)).parent.parent)
sys.path.append(project_path)

from config.system import Notice, PATH
from utils.notice2iphone import send_notice
from utils.utils import save_json, load_json

symbol = 'ethereum'
url1 ='https://dncapi.bqiapp.com/api/coin/web-charts?code=' + symbol +'&type=d&webp=0'
url3 ='https://fxhapi.feixiaohao.com/public/v1/ticker?start=99&limit=99&convert=USD'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    #'Accepts': 'application/json',
}

def gen_coin_list():
    url = 'https://dncapi.bqiapp.com/api/coin/web-coinrank?pagesize=100&page=1&type=-1&webp=1'
    response = requests.get(url, headers=headers)
    result = json.loads(response.content)
    coin_lists = {'data': []}
    id = 0
    for list in result['data']:
        print(list)
        tmp = dict()
        id = id + 1
        tmp['id'] = id
        tmp['code'] = list['code']
        tmp['name'] = list['name']
        tmp['fullname'] = list['fullname']
        coin_lists['data'].append(tmp)
    save_json(coin_lists, PATH.PATH_JSON)

def get_coin(seq):
    # pagesize: 每页有多少个
    # page :第几页, 当 pagesize==1 时，代表第几个币
    url = 'https://dncapi.bqiapp.com/api/coin/web-coinrank?pagesize=1&page=' + str(seq) + '&type=-1&webp=1'
    response = requests.get(url, headers=headers)
    result = json.loads(response.content)
    print(result)
    #print('币种：' + result['data'][0]['fullname'] + ' ' + result['data'][0]['name'])
    #print('当前价格￥: ' + str(result['data'][0]['current_price']))
    #print('当前价格$: ' + str(result['data'][0]['current_price_usd']))
    #print('24H涨跌幅: ' + str(result['data'][0]['change_percent']))
    #print('24H换手率: ' + str(result['data'][0]['turnoverrate']))
    return result

def get_conin_seq(symbol):
    print(PATH.PATH_JSON)
    coin_dict = load_json(PATH.PATH_JSON)
    for list in coin_dict['data']:
        # print(list)
        if list['name'] == symbol.upper():
            return list['id']

def get_name_list():
    print(PATH.PATH_JSON)
    coin_dict = load_json(PATH.PATH_JSON)
    name_list = []
    for list in coin_dict['data']:
        name_list.append(list['name'])
    return name_list

def get_market(symbol):
    #symbol = 'eth'
    idx = get_conin_seq(symbol)
    result = get_coin(idx)
    if result['data'][0]['name'] != symbol:
        gen_coin_list()
        idx = get_conin_seq(symbol)
        result = get_coin(idx)

    ret = result['data'][0]['fullname'] + ' ' + result['data'][0]['name'] + '\n' \
            '当前价格￥: ' + str(result['data'][0]['current_price']) + '\n' \
            '当前价格$: ' + str(result['data'][0]['current_price_usd']) + '\n' \
            '24H涨跌幅: ' + str(result['data'][0]['change_percent']) + '%\n' \
            '24H换手率: ' + str(result['data'][0]['turnoverrate'])
    return ret
    #send_notice(Notice.EVENT_NAME, Notice.KEY, result['data'][0]['fullname']+' $'+str(result['data'][0]['current_price_usd']))
