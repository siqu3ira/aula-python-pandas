import pandas as pd 
import numpy as np
import datetime as dt

df = pd.read_csv('https://www.harve.com.br/praticas/dados_etl.csv', sep="\t") # separando quando o delimitador é uma \

def tratar_nomes(x) :
    x = x.replace(" ", "_").upper() # Substituindo o nome da coluna passada e colocando tudo em maiúsculo
    return x

colunas = list(df.columns) # criando uma lista com os nomes das colunas
colunas_tratadas = map(tratar_nomes, colunas) # Altera todos os nomes que estiverem na lista colunas
df.columns = list(colunas_tratadas)

tmp = df[['CLIENT_ID', 'KIDHOME', 'TEENHOME']]
print(tmp.head())
print()

x = tmp.iloc[0]
print(x)

valor = 1 if x.KIDHOME + x.TEENHOME > 0 else 0
print(valor)
print()

tmp['CHILD_FLAG'] = tmp.apply (

    lambda x:
    1 if x.KIDHOME + x.TEENHOME > 0
    else 0, axis=1
)

print(tmp['CHILD_FLAG'])