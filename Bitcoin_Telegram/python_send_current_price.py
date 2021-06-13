import time 
import datetime
import pandas as pd
import requests
from pycoingecko import CoinGeckoAPI
import configparser
import python_import_function as pif
import json
from tabulate import tabulate

cg = CoinGeckoAPI()
coins =['bitcoin', 'bitcoin-cash', 'ethereum', 'litecoin', 'ripple']
currency="MYR"

#current_price=cg.get_price(ids=coins, vs_currencies=currency)
#message="Current coin price in MYR is :\n"
#for i in current_price:
#    message = message+(i+": MYR "+str(current_price[i]['myr'])+"\n")
#print(message)
#test = pif.telegram_bot_sendtext(message)

try:
    input_file=open("previous_price.json","r")
    previous=input_file.read()
    previous_price=json.loads(previous.replace("'",'"'))
except IOError:
    initialize="""{"bitcoin": {"myr": 0}, "litecoin": {"myr": 0}, "ethereum": {"myr": 0}, "ripple": {"myr": 0}, "bitcoin-cash": {"myr": 0}}"""
    previous_price=json.loads(initialize.replace("'",'"'))    
#finally:
#    input_file.close()

current_price=cg.get_price(ids=coins, vs_currencies=currency)
#print(current_price)
with open("previous_price.json", "w") as outfile:
    outfile.write(str(current_price).replace("'",'"'))
#print(previous_price)
#print(current_price)
df_prev=pd.DataFrame(previous_price)
df_curr=pd.DataFrame(current_price)
df_new=(df_curr/df_prev-1)*100
df_new_t=df_new.T
df_new_t=df_new_t.round(3)
df_new_t=df_new_t.reset_index()
df_new_t["change"]=df_new_t["myr"]
df_new_t.loc[df_new_t.myr > 0, 'change'] = "🟢"
df_new_t.loc[df_new_t.myr < 0, 'change'] = "🔴"
df_new_t.loc[df_new_t.myr == 0, 'change'] = "🟡"
#test = telegram_bot_sendtext(message)
#print(tabulate(df_new_t.values.tolist(),headers=["Coin","Change","Status"], tablefmt='psql'))
message = tabulate(df_new_t.values.tolist(), tablefmt='simple')
test = pif.telegram_bot_sendtext(message)