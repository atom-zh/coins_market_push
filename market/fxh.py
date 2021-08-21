import os
import sys
import pathlib
import requests
import json
import time
project_path = str(pathlib.Path(os.path.abspath(__file__)).parent.parent)
sys.path.append(project_path)

from config.system import PATH
from utils.utils import save_json, load_json

symbol = 'ethereum'
url1 ='https://dncapi.bqiapp.com/api/coin/web-charts?code=' + symbol +'&type=d&webp=0'
url3 ='https://fxhapi.feixiaohao.com/public/v1/ticker?start=99&limit=99&convert=USD'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    #'Accepts': 'application/json',
}

coin_dict = load_json(PATH.PATH_JSON)

def gen_coin_list():
    page_num = 5
    id = 0
    coin_lists = {'data': []}
    for page in range(page_num):
        url = 'https://dncapi.bqiapp.com/api/coin/web-coinrank?pagesize=100&page='+str(page+1)+'&type=-1&webp=2'
        response = requests.get(url, headers=headers)
        result = json.loads(response.content)
        for list in result['data']:
            tmp = dict()
            id = id + 1
            tmp['id'] = id
            tmp['code'] = list['code']
            tmp['name'] = list['name']
            tmp['fullname'] = list['fullname']
            coin_lists['data'].append(tmp)
        time.sleep(1)
    save_json(coin_lists, PATH.PATH_JSON)

def get_coin(seq):
    # pagesize: 每页有多少个
    # page :第几页, 当 pagesize==1 时，代表第几个币
    url = 'https://dncapi.bqiapp.com/api/coin/web-coinrank?pagesize=1&page=' + str(seq) + '&type=-1&webp=1'
    response = requests.get(url, headers=headers)
    result = json.loads(response.content)
    print(result)
    return result

def get_conin_seq(symbol):
    global coin_dict
    for list in coin_dict['data']:
        # print(list)
        if list['name'] == symbol.upper():
            return list['id']
    return -1

def get_price(symbol):
    #symbol = 'eth'
    symbol = symbol.upper()
    idx = get_conin_seq(symbol)
    result = get_coin(idx)
    if result['data'][0]['name'] != symbol:
        print('Symbol not match. Regenerate the json file')
        gen_coin_list() # 重新生成
        global coin_dict
        coin_dict = load_json(PATH.PATH_JSON) # 重新加载json文件
        idx = get_conin_seq(symbol)
        result = get_coin(idx)

    ret = '【名称】 ' + result['data'][0]['fullname'] + '-' + result['data'][0]['name'] + '\n' \
            '【USD价格】 ' +'$' + str(result['data'][0]['current_price_usd']) + '\n' \
            '【CNY价格】 ' +'¥' + str(result['data'][0]['current_price']) + '\n' \
            '【全球市值】 ' + '$' + str('%.2f' % (result['data'][0]['marketcap']/100000000)) + '亿\n' \
            '【24H涨幅】 ' + str(result['data'][0]['change_percent']) + '%\n' \
            '【24H换手】 ' + str(result['data'][0]['turnoverrate']) + '%\n\n' \
            + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ) + '\n' \
            '数据来源：非小号'

    print(ret)
    return ret
    #send_notice(Notice.EVENT_NAME, Notice.KEY, result['data'][0]['fullname']+' $'+str(result['data'][0]['current_price_usd']))