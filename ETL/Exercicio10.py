import pandas as pd 
import numpy as np
import datetime as dt
import requests as r

headers = {
    'x-api-key': "1f1EPRY19SDFDF2nM5F4hNB1GDvWcs3PQ33krU"
}

data = dt.datetime(2020, 6, 18)
data = data.timestamp()

API_URL = "https://www.yahoofinanceapi.com/"
API_ROUTE = "v7/finance/options"
QUERY_PARAMS = "/AAPL?date={}".format(int(data))

URL = API_URL + API_ROUTE + QUERY_PARAMS
response = r.request("GET", URL, headers=headers)

retorno_api = response.json()
resultado = retorno_api['optionChain']['result']
print(resultado[0]['quote']['quoteSourceName'])