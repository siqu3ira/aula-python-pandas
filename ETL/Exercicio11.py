import pandas as pd 
import numpy as np
import datetime as dt
import requests as r

headers = {
    'x-api-key': "1f1EPRY19SDFDF2nM5F4hNB1GDvWcs3PQ33krU"
}


dia = 22
mes = 10 
ano = 2019

URL = "https://apitempo.inmet.gov.br/condicao/capitais/"+str(ano) + '-' + str(mes) + '-' + str(dia)
response = r.request("GET", URL, headers=headers)
x = response.json()
df = pd.DataFrame(x)
print(df.dtypes)
df['TMAX18'] = df['TMAX18'].str.replace("*", "") # Substitui os valores que forem = a "*" por ""

df['TMAX18'] = pd.to_numeric(df['TMAX18']) # Muda o tipo do valor da coluna para numérico

print(round(df['TMAX18'].mean(), 2))