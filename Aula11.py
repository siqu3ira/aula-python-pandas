import pandas as pd 
import numpy as np

dados = {'prova1': [6, 7, 8, 8, 9, 3, 6], 
         'prova2': [7, 8, 5, 7, 10, 8, 7], 
         'nome': ['Ana', 'Pedro', 'João', 'Karla', 'Silvio', 'Teresa', 'Claudia'],
         'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B']}

df = pd.DataFrame(data=dados, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
                                                                               # ignore_index=True indica que indicie não sera passado          
df.columns = ['Prova 1', 'Prova 2', 'Nomes', 'Turma']  # altera o nome das colunas (somente se for de todas as colunas)

df = df.set_index(keys = 'Nomes') # identifica qual coluna substituirá o index

df.loc['Ana', 'Prova 1'] = 8

df.loc['Marcelo'] = [10, 4, 'B'] # Adicionando um novo dado no dataFrame

df.loc['Marcelo'] = [9, 6, 'A'] # Como já existe um Marcelo ele irá apenas alterar os dados do aluno

df = df.reset_index() # Volta o index para o formato original

df.loc[8] = ['Marcelo', 10, 4, 'B'] # Adiciona um novo dado no dataFrame 

df.loc[:, 'Soma das Notas'] = df['Prova 1'] + df['Prova 2'] # Adiciona uma nova coluna aonde soma os valores de outras duas do mesmo index


print("Adicionando uma nova coluna com valores null")
df.loc[:, 'Media'] = np.nan
print(df.head())
print()

print('Verifica quais dados são ou não do tipo null no dataFrame')
print(df.isnull())
print()

print('Soma todos os dados do tipo null no dataFrame')
print(df.isnull().sum())
print()

print('Substitui os valores do tipo null, do dataFrame, por um valor default indicado')
df = df.fillna(value=7)
print(df.head())
print()

print('Mudando a nota do primeiro aluno')
df.loc[0, 'Media'] = np.nan
print(df.head())

print('Substitui os valores do tipo null, do dataFrame de uma coluna específica, por um valor default indicado')
df = df.fillna(value={'Media': 1}) # Altera somente os dados que forem do tipo null para o valor indicado
print(df.head())
print()

print('Removendo a linha que pertence ao aluno que possui um dado do tipo null')
df = df.dropna(axis=0) # Remove a linha aonde tem um dado do tipo null, caso coloque axis igual a 1 remove a coluna.
print(df)
print()

print("Mostrando todos os nomes existentes na coluna informado:")
print(df['Nomes'].unique())
print()

print("Mostrando quantas vezes cada valor aparece na coluna informada:")
print(df['Nomes'].value_counts())
print()

print("Removendo valores duplicados da coluna informada:")
df = df.drop_duplicates(subset=['Nomes'], keep='first')
print(df['Nomes'].value_counts())
print(df)
print()