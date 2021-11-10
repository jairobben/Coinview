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

    
