import os

class Notice:
    EVENT_NAME = 'notice_python'
    TOKEN = '{your IFTTT TOKEN}'
    KEY = '{your notice key}'

class Zengr:
    APP_CODE = '{your app code}}'

class PATH:
    PATH_JSON = os.getcwd().replace('\\', '/') + '/coin_list.json'

class WECHAT:
    TOKEN = '{your wechaty token}'
