import pandas as pd 

serie1 = pd.Series(data=[10, 22, 23, 48, 54], index=[0, 1, 2, 3, 4]) # cria uma tabela aonde o index é a posição e data o valor

print(serie1)
print(serie1[0]) # pega o valor (data) do index indicado
print(serie1[3])
