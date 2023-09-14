import pandas as pd 

dados = {'prova1': [6, 7, 8, 8, 9, 3, 6], 
         'prova2': [7, 8, 5, 7, 10, 8, 7], 
         'nome': ['Ana', 'Pedro', 'João', 'Karla', 'Silvio', 'Teresa', 'Claudia'],
         'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B']}

df = pd.DataFrame(data=dados, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
                                                                               # ignore_index=True indica que indicie não sera passado          
df.columns = ['Prova 1', 'Prova 2', 'Nomes', 'Turma']  # altera o nome das colunas (somente se for de todas as colunas)

df = df.set_index(keys = 'Nomes') # identifica qual coluna substituirá o index

df.loc['Ana', 'Prova 1'] = 8

print("Adicionando um novo aluno no dataFrame")
df.loc['Marcelo'] = [10, 4, 'B'] # Adicionando um novo dado no dataFrame
print(df.shape) # Verificação de linhas e colunas do dataFrame
print(df)
print()

print("Adicionando um novo aluno no dataFrame com o nome de um já existente")
df.loc['Marcelo'] = [9, 6, 'A'] # Como já existe um Marcelo ele irá apenas alterar os dados do aluno
print(df.shape) # Verificação de linhas e colunas do dataFrame
print(df) 
print()

print("Resetando o index para o formato original")
df = df.reset_index() # Volta o index para o formato original
print(df.head())
print()

print("Adicionando um novo aluno no dataFrame")
df.loc[8] = ['Marcelo', 10, 4, 'B'] # Adiciona um novo dado no dataFrame 
print(df.shape)
print(df)
print()

print("Adicionando uma nova coluna aonde o valor é a soma de duas colunas")
df.loc[:, 'Soma das Notas'] = df['Prova 1'] + df['Prova 2'] # Adiciona uma nova coluna aonde soma os valores de outras duas do mesmo index
print(df.head())