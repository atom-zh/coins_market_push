# coins_market_push  
虚拟币行情推送
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
---
# TODO
- 通过合适的算法，计算币价的波动，然后推送
---
# 特别鸣谢
[python-wechaty](https://github.com/wechaty/python-wechaty)
