import pandas as pd 
import numpy as np

df = pd.read_csv('http://www.harve.com.br/praticas/dados_etl.csv', sep="\t")

df['Mais de Uma Compra'] = df['NumWebPurchases'] > 1 # Criando uma tabela aonde retorna True para o cliente que fez mais de uma compra e False para quem não fez

print(len(df.loc[df['Mais de Uma Compra'] == True])) # Pegando a quantidade de cliente que realizaram mais de uma compra