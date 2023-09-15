import pandas as pd 
import numpy as np

df = pd.read_csv('http://www.harve.com.br/praticas/dados_etl.csv', sep="\t")

def tratar_nomes(x):
  x = x.replace(" ", "_").upper() # Adicionando o "x." antes do replace para concertar o erro
  return x

cols = list(df.columns)
cols_tratadas = map(tratar_nomes, cols)
df.columns = list(cols_tratadas)