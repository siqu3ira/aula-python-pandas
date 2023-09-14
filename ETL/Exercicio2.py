import pandas as pd 
import numpy as np

df = pd.read_csv('http://www.harve.com.br/praticas/dados_etl.csv', sep="\t")

filtro = (df['Client ID'] == 2278)
print(df[filtro])