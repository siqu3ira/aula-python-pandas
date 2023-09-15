import pandas as pd 
import numpy as np
import datetime as dt

df = pd.read_csv('https://www.harve.com.br/praticas/dados_etl.csv', sep="\t") # separando quando o delimitador é uma \

df = df.rename(columns={'Client ID': 'CLIENT_ID'})

tmp = df.loc[df['Income'].isna()] # Pegando os dados do dataFrame que tem a coluna 'Income' com valor null
print('Soma de compras na loja(NumStorePurchases) de registros que estão com renda (income) como Nan:', tmp['NumStorePurchases'].sum()) # Calculando a soma de todos os valores da coluna'NumStorePurchases'