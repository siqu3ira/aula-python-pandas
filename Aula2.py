import pandas as pd 

dados = {'prova_1': [6, 7, 8, 8, 9, 3, 6], # Cria uma tabela com os dados passados. 
         'prova_2': [7, 8, 5, 7, 10, 8, 7], # Todos os campos devem possuir o mesmo número de itens
         'nome': ['Ana', 'Pedro', 'João', 'Karla', 'Silvio', 'Teresa', 'Claudia'],
         'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B']}

df = pd.DataFrame(data=dados)

print(df)
