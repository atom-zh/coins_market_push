# pylint: disable=R0801
import os
import sys
import asyncio
import logging
import pathlib
project_path = str(pathlib.Path(os.path.abspath(__file__)).parent.parent)
sys.path.append(project_path)

from market.fxh import get_price, get_conin_seq
from config.system import WECHAT
from wechaty import (
    Contact,
    Message,
    Wechaty,
    ScanStatus,
    Room,
)

from typing import Optional, Union
from wechaty_puppet import FileBox, ScanStatus  # type: ignore

os.environ['WECHATY_PUPPET'] = "wechaty-puppet-service"
os.environ['WECHATY_PUPPET_SERVICE_TOKEN'] = WECHAT.TOKEN


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

async def on_message(msg: Message):
    """
    Message Handler for the Bot
    """
    """
    if msg.text() == 'ding':
        await msg.say('dong')

        file_box = FileBox.from_url(
            'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/'
            'u=1116676390,2305043183&fm=26&gp=0.jpg',
            name='ding-dong.jpg'
        )
        await msg.say(file_box)
    """
    text: str = msg.text()
    room: Optional[Room] = msg.room()
    print(text)
    print(room)
    if text.startswith('@Robot'):
        rev_str = text.replace(' ', '')
        symbol = rev_str.split(' ')[-1]
    else:
        symbol = text
    talker = msg.talker()

    if symbol == '多空':
        await room.say('\n抱歉！【多空】正在开发中...', mention_ids=[talker.contact_id])
    elif symbol == '灰度':
        await room.say('\n抱歉！【灰度】正在开发中...', mention_ids=[talker.contact_id])
    elif get_conin_seq(symbol) > 0:
        send_msg = get_price(symbol)
        print(send_msg)
        await room.say(send_msg, mention_ids=[talker.contact_id])

async def on_scan(
        qrcode: str,
        status: ScanStatus,
        _data,
):
    """
    Scan Handler for the Bot
    """
    print('Status: ' + str(status))
    print('View QR Code Online: https://wechaty.js.org/qrcode/' + qrcode)


async def on_login(user: Contact):
    """
    Login Handler for the Bot
    """
    print(user)
    # TODO: To be written

async def main():
    """
    Async Main Entry
    """
    #
    # Make sure we have set WECHATY_PUPPET_SERVICE_TOKEN in the environment variables.
    # Learn more about services (and TOKEN) from https://wechaty.js.org/docs/puppet-services/
    #
    if 'WECHATY_PUPPET_SERVICE_TOKEN' not in os.environ:
        print('''
            Error: WECHATY_PUPPET_SERVICE_TOKEN is not found in the environment variables
            You need a TOKEN to run the Python Wechaty. Please goto our README for details
            https://github.com/wechaty/python-wechaty-getting-started/#wechaty_puppet_service_token
        ''')

    bot = Wechaty()

    bot.on('scan',      on_scan)
    bot.on('login',     on_login)
    bot.on('message',   on_message)

    await bot.start()
    print('[Python Wechaty] Ding Dong Bot started.')

asyncio.run(main())

