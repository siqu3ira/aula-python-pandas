import pandas as pd 

dados = {'prova1': [6, 7, 8, 8, 9, 3, 6], 
         'prova2': [7, 8, 5, 7, 10, 8, 7], 
         'nome': ['Ana', 'Pedro', 'João', 'Karla', 'Silvio', 'Teresa', 'Claudia'],
         'turma': ['A', 'A', 'B', 'B', 'A', 'B', 'B']}

df = pd.DataFrame(data=dados, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
                                                                               # ignore_index=True indica que indicie não sera passado          
df.columns = ['Prova 1', 'Prova 2', 'Nomes', 'Turma']  # altera o nome das colunas (somente se for de todas as colunas)

df = df.set_index(keys = 'Nomes') # identifica qual coluna substituirá o index

print("Verificação de quem pertence a turma A e possui uma nota maior que 7")
filtro = (df['Turma'] == 'A') & (df['Prova 1'] > 7) # Verifica quem pertence a condição estabelecida
print(df[filtro]) # Retorna o dataFrame com as condições estabelecidas
print()

print("Verificação de quem tirou em pelo menos uma das provas uma nota maior ou igual a 8")
filtro = (df['Prova 1'] >= 8) | (df['Prova 2'] >= 8) # Verifica quem pertence a condição estabelecida
print(df[filtro]) # Retorna o dataFrame com as condições estabelecidas
print()

print("Realizando o filtro sem criar uma variável")
print(df[(df['Prova 1'] >= 8) | (df['Prova 2'] >= 8)]) # Retorna o dataFrame com as condições estabelecidas