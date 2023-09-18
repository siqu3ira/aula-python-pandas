import pandas as pd 
import numpy as np
import requests
import json
import datetime as dt

headers = {
    'x-api-key': "1f1EPRY19SDFDF2nM5F4hNB1GDvWcs3PQ33krU"
} # usuario e senha da api

data = dt.datetime(2020, 3, 17, 00, 00, 00) # Instanciando a data do tipo dataTime

timeStamp = int(data.timestamp()) # Transformando em timeStamp
print(timeStamp)
print()

url = 'https://yfapi.net/v7/finance/options/AAPL?date=' + str(int(timeStamp)) # Instanciando a url

response = requests.request("GET", url, headers=headers) # Consulta a API. Autenticação feita pelo request

x = response.json() # Transformando a resposta da consula a API em json
print(x)