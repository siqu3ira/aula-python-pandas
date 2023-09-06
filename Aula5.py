import pandas as pd 

serie1 = pd.Series(data=[10, 22, 23, 48, 54], index=[0, 1, 2, 3, 4]) # cria uma tabela aonde o index é a posição e data o valor

dados = {'prova1': [6, 7, 8, 8, 9, 3, 6], 
         'prova2': [7, 8, 5, 7, 10, 8, 7], 
         'nome': ['Ana', 'Pedro', 'João', 'Karla', 'Silvio', 'Teresa', 'Claudia'],
         'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B']}

df = pd.DataFrame(data=dados, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])

df.columns = ['Prova 1', 'Prova 2', 'Nomes', 'Turma']  # altera o nome das colunas (somente se for de todas as colunas)

df = df.set_index(keys = 'Nomes') # identifica qual coluna substituirá o index
df.head(n=3)

print("Verificando os tipos de dados do dataFrame e da serie")                                                                               
print("- DataFrame: ")
print(df.dtypes)  
print()
print(df.info()) # funciona apenas para dataFrame. Mostra os tipos de cada coluna e exibe a quantidade de memória necessária
# para armazenar todo conjunto de dados
print("- Serie: ")
print(serie1.dtypes) 
print()
