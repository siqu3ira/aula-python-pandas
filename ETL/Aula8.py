import pandas as pd 
import numpy as np
from datetime import datetime, timedelta

df = pd.read_csv('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&startTime=1634243893', sep="\t") # separando quando o delimitador é uma \

symbol = 'BTCUSDT'
interval = '1h'
startTime = datetime.now() # Pegando a data e hora atual

print("Data e hora atuais")
print(startTime)
print()

startTime = startTime - timedelta(5)
print('Data e hora de 5 dias atrás')
print(startTime)
print()

startTime = int(startTime.timestamp()) # Transformando a data do tipo dateTime por tipo TimeStamp
QUERY_PARAMS = "?symbol={}&interval={}&startTime={}000".format(symbol, interval, startTime)

print(QUERY_PARAMS)
print()

'''startTime = int(startTime.timestamp())
print(startTime)'''