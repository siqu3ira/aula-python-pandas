import pandas as pd 

serie1 = pd.Series(data=[10, 22, 23, 48, 54], index=[0, 1, 2, 3, 4]) # cria uma tabela aonde o index é a posição e data o valor

dados = {'prova1': [6, 7, 8, 8, 9, 3, 6], 
         'prova2': [7, 8, 5, 7, 10, 8, 7], 
         'nome': ['Ana', 'Pedro', 'João', 'Karla', 'Silvio', 'Teresa', 'Claudia'],
         'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B']}

df = pd.DataFrame(data=dados, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
df = df._append({'prova1': 6, 'prova2': 7, 'nome': 'Cristiane', 'turma': 'A'}, ignore_index=True) # add um novo item para cada coluna

print("Verificando o tamanho do dataFrame e da serie")                                                                               # ignore_index=True indica que indicie não sera passado          
print("- DataFrame: ")
print(df.shape)  #retorna o número de linhas e colunas
print("- Serie: ")
print(serie1.shape) # retorna a qtd de linhas já que é uma estrutura unidimensional
print()

print("Mostrando os nomes das colunas do dataFrame")
print("- Nomes: " + df.columns) # retorna o nome das colunas existentes
print()

print("Alterando os nomes das colunas do dataFrame")
df.columns = ['Prova 1', 'Prova 2', 'Nomes', 'Turma']  # altera o nome das colunas (somente se for de todas as colunas)
print(df)
print()

print("Dando um nome a serie")
print(serie1)
serie1.name = 'Idades' # dá um nome a serie (já que é apenas uma coluna)
print(serie1)
print()

print("Mostrando os index do dataFrame e da serie")
print("- DataFrame: ")
print(df.index.tolist())
print("- Serie: ")
print(serie1.index)
print()

print("Mudando o index do dataFrame por uma coluna e seus valores")
df = df.set_index(keys = 'Nomes') # identifica qual coluna substituirá o index
print(df.head(n=3)) # pega n valores do dataFrame
print()

