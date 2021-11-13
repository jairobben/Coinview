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
    return frame


df = getminutedata('ADAUSDT','1m','100')
#Guarda en fichero, con esta funcion no hace falta abrir ni cerrar el fichero
csvfile2 = df.to_csv("prueba5.csv")


#def add_vars(dataframe, )






#df.insert(1, 'datetime',[datetime.fromtimestamp(d/1000)for d in df.timestamp])

def applytechnicals(df):
    df['%K'] = ta.momentum.stock(df.High,df.Low,df.Close, window=14, smooth_window=3)
    df['%D'] = df['%K'].rolling(3).mean()
    df['rsi'] = ta.momentum.rsi(df.Close, window=14)
    df['macd'] = ta.trend.macd_diff(df.Close)
    df.dropna(inplace = True)

technicals=applytechnicals(df)

print(technicals)

