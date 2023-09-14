import pandas as pd 

dados = {'prova1': [6, 7, 8, 8, 9, 3, 6], 
         'prova2': [7, 8, 5, 7, 10, 8, 7], 
         'nome': ['Ana', 'Pedro', 'João', 'Karla', 'Silvio', 'Teresa', 'Claudia'],
         'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B']}

df = pd.DataFrame(data=dados, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
                                                                               # ignore_index=True indica que indicie não sera passado          
df.columns = ['Prova 1', 'Prova 2', 'Nomes', 'Turma']  # altera o nome das colunas (somente se for de todas as colunas)

df = df.set_index(keys = 'Nomes') # identifica qual coluna substituirá o index

print("Mostrando apenas uma coluna e seus respectivos valores")
print(df['Prova 1'])  # Mostra os valores da coluna indicada
print()

print("Mostrando um item específico de uma coluna")
print('- ')
print(df['Prova 1']['Ana'])  # Mostra o valor de uma coluna indicada no index indicado
print("- ")
print(df.loc['Ana', 'Prova 1'])  # Mostra o valor de uma coluna indicada no index indicado
print()
print("- ")
print(df.loc[['Ana', 'Karla', 'Teresa'], 'Prova 1'])  # Mostra os valores de uma coluna indicada nos indexes indicados
print("- ")
print(df.loc['Ana':'Karla', 'Prova 1'])  # Mostra os valores de uma coluna indicada no intervalo dos indexes indicados
print()

print("Alterando o valor específico de uma coluna")
df['Prova 1']['Ana'] = 8 # Altera o valor de uma coluna indicada no index indicado
print(df)
print()
