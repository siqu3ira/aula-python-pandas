import pandas as pd 
import numpy as np

df = pd.read_csv('http://www.harve.com.br/praticas/dados_etl.csv', sep="\t")

filtro = df[df['NumWebPurchases'] > 1] # Retornando apenas clientes que fizeram mais de uma compra na NumWebPurchases
print(filtro['NumWebPurchases'].count()) # Contanado quantos aparecem