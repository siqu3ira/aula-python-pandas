import pandas as pd 
import numpy as np
import datetime as dt

df = pd.read_csv('https://www.harve.com.br/praticas/dados_etl.csv', sep="\t") # separando quando o delimitador é uma \

df = df.rename(columns={'Client ID': 'Client_Id'}) # Alterando o nome da coluna 
print(df.Client_Id) # Chamando a coluna de uma forma diferente
print()

def tratar_nomes(x) :
    x = x.replace(" ", "_").upper() # Substituindo o nome da coluna passada e colocando tudo em maiúsculo
    return x

print(tratar_nomes('Dt Customer')) # Utilizando a função para alterar o nome da coluna
print()

colunas = list(df.columns) # criando uma lista com os nomes das colunas
print(colunas)
print()

colunas_tratadas = map(tratar_nomes, colunas) # Altera todos os nomes que estiverem na lista colunas
#print(list(colunas_tratadas)) # mostra todos os itens do map
print()

df.columns = list(colunas_tratadas) # Alterando o nome de todas as colunas
print(df)