import pandas as pd 
import numpy as np
import datetime as dt

df = pd.read_csv('https://www.harve.com.br/praticas/dados_etl.csv', sep="\t") # separando quando o delimitador é uma \

print("Verificando quantos dados do tipo nulo existem em cada coluna")
print(df.isna().sum())
print()

tmp = df[df.Income.isna() == True]
print("Verificando quantos dados do tipo nulo existem na coluna Income")
print('Quantidade de itens:', len(tmp))
print()

tmp = df['Income'].dropna()
print("Tamanho do dataFrame completo:", len(df))
print("Tamnho do dataFrame sem os valores nulo:", len(tmp))
print()

df["Income"] = df["Income"].fillna(df["Income"].mean())
print(df[df.Income.isna() == True])