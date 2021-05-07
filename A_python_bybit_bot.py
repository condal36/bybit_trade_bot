#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/7 下午 10:52
# @Author : Condal36
# @Site : 
# @File : A_python_bybit_bot.py
# @Software: PyCharm
import bybit
import time
def time_report(i):
    print(f"The bot has been start for {i} mins long")
def SelndBuy(client,dis=100,qty=1):
    pricedata = client.Market.Market_symbolInfo().result()[0]
    Market_price = float(pricedata["result"][0]["last_price"])
    buy_price = (Market_price * 100 - dis) / 100
    sell_price = (Market_price * 100 + dis) / 100
    print(buy_price, sell_price)
    print(client.Order.Order_new(side="Buy", symbol="BTCUSD", order_type="Limit", qty=qty, price=buy_price,
                                 time_in_force="PostOnly").result()[0])
    print(client.Order.Order_new(side="Sell", symbol="BTCUSD", order_type="Limit", qty=qty, price=sell_price,
                                 time_in_force="PostOnly").result()[0])

welcommessage="Welcome trade bot !"
if __name__=="__main__":
    print(welcommessage)
    time.sleep(0.5)
    api_key = input("Input api key:\n")
    api_secret = input("Input api key:\n")
    client = bybit.bybit(test=False, api_key=api_key, api_secret=api_secret)
    print(client.Symbol.Symbol_get().result()[0]["result"][0])
    i = 0
    while True:
        SelndBuy(client)
        i = i + 1
        time_report(i)
        time.sleep(60)
