import time 
import datetime
import pandas as pd
import requests
from pycoingecko import CoinGeckoAPI
import configparser
cg = CoinGeckoAPI()
coins =['bitcoin', 'bitcoin-cash', 'ethereum', 'litecoin', 'ripple']
currency="MYR"
config = configparser.ConfigParser()
config.read('config.conf')
config.sections()
config["telegram_RedNavi_bot"]['bot_token']

def convert_unix(time): #For fuck sake this is annoying To convert time 
    return datetime.datetime.fromtimestamp(int(str(time)[:10])).strftime('%Y-%m-%d %H:%M:%S')
    #return datetime.datetime.fromtimestamp(int(str(time)[:10])).strftime('%Y-%m-%d')
	
def telegram_bot_sendtext(bot_message):
    bot_token = config["telegram_RedNavi_bot"]['bot_token']
    bot_chatID = config["telegram_RedNavi_bot"]['bot_chatID']
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


current_price=cg.get_price(ids=coins, vs_currencies=currency)
message="Current coin price in MYR is :\n"
for i in current_price:
    message = message+(i+": MYR "+str(current_price[i]['myr'])+"\n")
print(message)
test = telegram_bot_sendtext(message)