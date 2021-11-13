from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import numpy as np
import csv
import matplotlib.pyplot as plt
import config

client = Client(config.api_key, config.api_secret)

#prices = client.get_all_tickers()

#for price in prices:
    #print(price)

candles = client.get_klines(symbol='BNBUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('2012-2021BTC.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile)
candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2012", "7 Nov, 2021")

for candlestick in candlesticks:
    candlestick_writer.writerow(candlestick)

csvfile.close()



----------------------------------------------------------------------------------------------------------------------------


import config, csv
from binance.client import Client
from datetime import datetime
import pandas as pd

client = Client(config.API_KEY, config.API_SECRET)


def getminutedata(symbol, interval, lookback):
    
    frame = pd.DataFrame(client.get_historical_klines(symbol, 
                                                      interval, 
                                                      lookback + ' min ago UTC'))
    frame = frame.iloc[:,:12]
    frame.columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume','close_time', 'asset_volume', 'n_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume','ignore']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    #candlesticks = client.get_historical_klines(symbol,interval,lookback)

    return frame


candlesticks2 = getminutedata('ADAUSDT','1m','100')

for candlestick in candlesticks2:
    candlestick[0]= candlestick[0]/1000
    candlestick_writer.writerow(candlestick)


print(candlesticks2)


csvfile = open('1 minuto.csv', 'w', newline='') 
candlestick_writer = csv.writer(csvfile, delimiter=',')
for candlestick in  candlesticks:
    candlestick_writer.writerow(candlestick)
csvfile.close()
