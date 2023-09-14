import pandas as pd 
import numpy as np

df = pd.read_csv('https://www.harve.com.br/praticas/baseficticia.csv', delimiter=';')
print(df['quantidade'].sum())