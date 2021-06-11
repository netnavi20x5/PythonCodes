import time 
import datetime
import pandas as pd
import requests
from pycoingecko import CoinGeckoAPI
import configparser
import python_import_function as pif

cg = CoinGeckoAPI()
coins =['bitcoin', 'bitcoin-cash', 'ethereum', 'litecoin', 'ripple']
currency="MYR"

current_price=cg.get_price(ids=coins, vs_currencies=currency)
message="Current coin price in MYR is :\n"
for i in current_price:
    message = message+(i+": MYR "+str(current_price[i]['myr'])+"\n")
print(message)
test = pif.telegram_bot_sendtext(message)