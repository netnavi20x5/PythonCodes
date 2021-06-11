import time 
import datetime
import pandas as pd
import requests
from pycoingecko import CoinGeckoAPI
import configparser
from tabulate import tabulate


config = configparser.ConfigParser()
config.read('config.conf')
config.sections()
config["telegram_RedNavi_bot"]['bot_token']

def convert_unix(time): #For fuck sake this is annoying To convert time 
        return datetime.datetime.fromtimestamp(int(str(time)[:10])).strftime('%d/%m/%y %a %H:%M')
    

def convert_data_frame(dict_data):
    df =pd.DataFrame(dict_data["prices"])
    df.columns = ['posix', 'price']
    df["date"]=df.apply(lambda row : convert_unix(row['posix']), axis = 1)
    price_now=df['price'].values[len(df.price)-1]
    df["diff_between_now"]=(price_now/df['price']-1)*100
    df["change"]= df.price.pct_change() * 100
    
    return df[["date","price","diff_between_now","change"]].round(2)



def telegram_bot_sendtext(bot_message):
    bot_token = config["telegram_RedNavi_bot"]['bot_token']
    #bot_chatID = '269721616'562593592
    bot_chatID = config["telegram_RedNavi_bot"]['bot_chatID']
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()