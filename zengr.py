import json
import urllib.request
import time
from system import Zengr

symbol = 'ETH'

host = 'http://alirmgbdc.market.alicloudapi.com'
path = '/query/com'
method = 'GET'
appcode = Zengr.APP_CODE
querys = 'symbol=' + symbol + '&withks=0&withticks=0'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib.request.urlopen(request)
content = response.read().decode('utf8')
print(content)

content=json.loads(content)
loc_time = time.localtime(content['Obj']['Tick'])
time = time.strftime("%Y-%m-%d %H:%M:%S",loc_time)

print('时间：' + time)
print('币种：'+ str(content['Obj']['S']) + ' ' + content['Obj']['N'])
print('最新价格：' + str(content['Obj']['P']))
print('24H最高：' + str(content['Obj']['H']))
print('24H最低：' + str(content['Obj']['L']))
print('24H涨跌幅：' + str(content['Obj']['ZF']))
print('24H成交量：' + str(content['Obj']['V']))
print('24H成交额：' + str(content['Obj']['A']))
