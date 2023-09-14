import pandas as pd 
import numpy as np
import datetime as dt

df = pd.read_csv('https://www.harve.com.br/praticas/dados_etl.csv', sep="\t") # separando quando o delimitador é uma \

print("Pegando os tipos de valores das colunas")
print(df.dtypes)
print()

print("Pegando os valores da coluna Year_Birth")
print(df['Year_Birth'])
print()

'''df['Age'] = 2021 - df['Year_Birth'] # Criando uma coluna de idade, subtraindo o ano de nascimento do ano atual (utilizando 2021 como). Não é uma boa prática colocando o ano de tal forma (2021)
print(df['Age'])
print()'''

print("Pegando a data atual")
print(dt.datetime.now().year)

df['Age'] = abs(df["Year_Birth"] - dt.datetime.now().year) # Jeito correto de fazer o calculo. abs serve para pegar o valor absoluto 
print(df['Age'].head())
print()

promocao = df[df['Age'] > 50] # pegando os cliente que possuem mais de 50 anos
print(promocao)
print()

promocao.drop('Year_Birth', axis=1, inplace=True)
print(promocao.head())