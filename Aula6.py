import pandas as pd 

dados = {'prova1': [6, 7, 8, 8, 9, 3, 6], 
         'prova2': [7, 8, 5, 7, 10, 8, 7], 
         'nome': ['Ana', 'Pedro', 'João', 'Karla', 'Silvio', 'Teresa', 'Claudia'],
         'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B']}

df = pd.DataFrame(data=dados, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
df = df._append({'prova1': 6, 'prova2': 7, 'nome': 'Cristiane', 'turma': 'A'}, ignore_index=True) # add um novo item para cada coluna
                                                                               # ignore_index=True indica que indicie não sera passado          

df = pd.DataFrame(data=dados, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])

df.columns = ['Prova 1', 'Prova 2', 'Nomes', 'Turma']  # altera o nome das colunas (somente se for de todas as colunas)

df = df.set_index(keys = 'Nomes') # identifica qual coluna substituirá o index

print("Modos de mostrar o dataFrame")                                                                               
print("- Completo: ")
print(df)
print()
print("- Apenas os 3 primeiros: ")
print(df.head(n=3))
print()
print("- Apenas os 3 últimos: ")
print(df.tail(n=3))
print()