import pandas as pd 
import numpy as np
import datetime as dt
import requests as r

symbol = 'BTCUSDT'
interval = '1h'
data = dt.datetime(2020, 3, 17, 00, 00, 00) 
timeStamp = int(data.timestamp())

API_URL = "https://api.binance.com"
API_ROUTE = "/api/v3/klines"
QUERY_PARAMS = "?symbol={}&interval={}&startTime={}000".format(symbol, interval, timeStamp)
URL_PRECOS_BITCOIN = API_URL + API_ROUTE + QUERY_PARAMS


response = r.get(url = URL_PRECOS_BITCOIN) # Pegando o retorno da chamada da API
obj_lista = response.json()

df = pd.DataFrame(obj_lista) # Cria um dataFrame com base nos dados retornados na chamada a API
print(df.head(5))
print()

df = df.iloc[:, :6] # Pegando as 6 primeiras colunas do dataFrame
df.columns = ['TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']
print(df.head())
print()

df['TIME'] = df['TIME'].apply(lambda x: dt.datetime.fromtimestamp(x/1000)) # Transformando a data de timeStamp para dateTime. A divisão por mil serve pois na API é em milisegundos e no python é em segundos
print(df.head())
print()

print(df.dtypes)
print()

df['OPEN'] = round(df['OPEN'].astype(float), 2) # arredonda o valor da coluna pra quantidade de casas decimais indicada. Muda o tipo dos valores da coluna. 
print(df.head())
print()

for c in list(df.iloc[:, 1:].columns) : df[c] = round(df[c].astype(float), 2) # Pega todas as colunas a partir da segunda coluna transformando o tipo de seus valores em float e os arredondando para ter duas casas decimais
print(df.head())