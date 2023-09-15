import pandas as pd 
import numpy as np

df = pd.read_csv('http://www.harve.com.br/praticas/dados_etl.csv', sep="\t")

def tratar_nomes(x):
  x = x.replace(" ", "_").upper() 
  return x

cols = list(df.columns)
cols_tratadas = map(tratar_nomes, cols)
df.columns = list(cols_tratadas)

ensino_dict = {
  "Graduation": "Médio",
  "PhD": "Alto",
  "Master": "Alto",
  "2n Cycle": "Baixo",
  "Basic": "Médio"

}

df["EDUCATION_CATEGORY"] = df["EDUCATION"].apply(lambda x: ensino_dict[x]) # Cria uma nova tabela atribuindo os valores dela para que se o nome for tal vai atribuir tal valor

df["EDUCATION_CATEGORY"].value_counts()

print(df["EDUCATION_CATEGORY"].value_counts())