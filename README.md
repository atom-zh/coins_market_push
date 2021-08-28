# coins_market_push  
[![Powered by Wechaty](https://img.shields.io/badge/Powered%20By-Wechaty-green.svg)](https://wechaty.js.org)
[![Wechaty Contributor Program](https://img.shields.io/badge/Wechaty-Contributor%20Program-green.svg)](https://wechaty.js.org/docs/contributor-program)
[![Juzi.BOT Developer Program](https://img.shields.io/badge/Wechaty%Contributor%20Program-Juzi.BOT-orange.svg)](https://github.com/juzibot/Welcome/wiki/Everything-about-Wechaty/)

虚拟币行情推送

[Blog地址](https://wechaty.js.org/2021/08/26/wechaty-bot-of-coins/)
---

## 目录介绍

- config/ 参数配置相关的目录
- utils/ 通用接口提取
- market/ 获取市场行情的接口目录 
- wechat/ 微信机器人接口

## 已实现功能

* 从网站获取数字货币行情，包括现价、涨跌幅、换手率等
* 将数字货币行情推送到手机提醒
* 当机器人在群里被@后，根据@内容，回复相应数字货币的行情

## 使用方法

[使用方法介绍:WIKI](https://github.com/atom-zh/coins_market_push/wiki/%E5%9F%BA%E4%BA%8Epython-Wechaty%E7%9A%84%E5%BE%AE%E4%BF%A1%E7%BE%A4%E8%99%9A%E6%8B%9F%E5%B8%81%E6%8A%A5%E4%BB%B7%E6%9C%BA%E5%99%A8%E4%BA%BA)

---
# TODO
- 通过合适的算法，计算币价的波动，然后推送
---

# 特别鸣谢

[python-wechaty](https://github.com/wechaty/python-wechaty)
