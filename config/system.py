import os
# 项目的根目录
path_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
path_root = path_root.replace('\\', '/')

class Notice:
    EVENT_NAME = 'notice_python'
    TOKEN = '{your IFTTT TOKEN}'
    KEY = '{your notice key}'

class Zengr:
    APP_CODE = '{your app code}}'

class PATH:
    PATH_JSON = path_root + '/coin_list.json'

class WECHAT:
    TOKEN = '{your wechaty token}'
