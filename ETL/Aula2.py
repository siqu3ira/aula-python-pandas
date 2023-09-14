import pandas as pd 
import numpy as np

df = pd.read_csv('https://www.harve.com.br/praticas/dados_etl.csv', sep="\t") # separando quando o delimitador é uma \

print(df.head())