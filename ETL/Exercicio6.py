import pandas as pd 
import numpy as np
import datetime as dt

df = pd.read_csv('https://www.harve.com.br/praticas/dados_etl.csv', sep="\t") # separando quando o delimitador é uma \

df = df.rename(columns={'Client ID': 'CLIENT_ID'})

def recebimento(valor):
  if valor<10000:
    return 'classe d'
  else:
    if valor < 30000:
      return 'classe c'
    else:
      if valor < 60000:
        return 'classe b'
      else:
        if valor >0:
          return 'classe a'
        else:
          return ''

classe = df['Income']
print(classe)
print()

df['Classe'] = classe.apply (lambda x: recebimento(x)) # Cria uma coluna aonde os valores são retornos do método passado

print(df['Classe'].value_counts()) # Calcula quantas vezes cada valor aparece na coluna

