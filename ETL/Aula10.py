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
print("\nURL da requisição: {}".format(URL_PRECOS_BITCOIN))
print()

response = r.get(url = URL_PRECOS_BITCOIN) # Pegando o retorno da chamada da API
print("Retorno da API no formato json:", response.json()[0]) # Pegando o primeiro item do retorno e transformando em json
print()

print("Código de retorno da chamada da API:", response.status_code) # Retorna 200 quando a chamada a API é bem sucedida 
print()

response_erro = r.get(url = 'https://api.binance.com/api/v3/klines?sssssymbol=BTCUSDT&interval=1h&startTime=1584414000000')
print("Código de retorno da chamada da API com erro:", response_erro.status_code) # Retorna 400 quando tem algum erro na chamada da API que não envolva a conexão com ela