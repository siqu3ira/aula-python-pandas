import pandas as pd 

dados = {'prova1': [6, 7, 8, 8, 9, 3, 6], 
         'prova2': [7, 8, 5, 7, 10, 8, 7], 
         'nome': ['Ana', 'Pedro', 'João', 'Karla', 'Silvio', 'Teresa', 'Claudia'],
         'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B']}

df = pd.DataFrame(data=dados, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
                                                                               # ignore_index=True indica que indicie não sera passado          
df.columns = ['Prova 1', 'Prova 2', 'Nomes', 'Turma']  # altera o nome das colunas (somente se for de todas as colunas)

df = df.set_index(keys = 'Nomes') # identifica qual coluna substituirá o index

df.loc['Ana', 'Prova 1'] = 8 # Alterando a nota da Ana

print("Verificação de quem pertence a turma A")
filtro = (df['Turma'] == 'A') # Retorna true para quem pertence a turma A e false para quem pertence a turma B
print(filtro)
print()

print("Retornando somente quem pertence a turma A")
print(df[filtro])