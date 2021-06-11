import time 
import datetime
import pandas as pd
import requests
from pycoingecko import CoinGeckoAPI
import configparser
from tabulate import tabulate
import python_import_function as pif

cg = CoinGeckoAPI()
coins =['bitcoin', 'bitcoin-cash', 'ethereum', 'litecoin', 'ripple']
currency="MYR"
coin_market=dict()
coin_market_hourly=dict()
for coin in coins:
    print (coin)
    coin_market[coin]=(cg.get_coin_market_chart_by_id(id=coin,vs_currency="MYR",days="90",interval="daily"))
    coin_market_hourly[coin]=(cg.get_coin_market_chart_by_id(id=coin,vs_currency="MYR",days="90",interval="hourly"))
    
    
from tabulate import tabulate
for coin in coins:
    df=pif.convert_data_frame(coin_market_hourly[coin]).tail()[["date","price","change"]]
    message="""coin+"\n"+tabulate(df.values.tolist(), headers=["date","price","change"], tablefmt='psql')"""
    pif.telegram_bot_sendtext(message)
