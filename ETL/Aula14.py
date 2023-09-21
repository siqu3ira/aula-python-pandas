import pandas as pd 
import numpy as np
import datetime as dt
import requests as r
import pymysql 
from sqlalchemy import create_engine

credenciais = {
    'username': 'alunoharve',
    'password': "wj7Hs2itAhv$",
    'hostname': 'ip-69-164-197-170.cloudezapp.io',
    'port': 3306,
    'database': 'harve_alunos.sql'
}

STRING_DE_CONEXAO = "mysql+pymysql://{}:{}@{}:{}/{}".format(
    credenciais['username'], credenciais['password'], credenciais['hostname'], credenciais['port'], credenciais['database'])


conn_obj = create_engine(STRING_DE_CONEXAO).connect() # Cria uma engine conectada ao banco de dados


'''df.to_sql(
    name = "preco_criptomoedas", # Nome da tabela que queremos criar
    con = conn_obj, # Engine de conexão
    if_exists = "append", # Se a tabela já existir os registros serão adicionados a ela. Por padrão se esse campo não for incluído tem como valor o "fail" que retorna um erro. Tem também o valor "replace" que substitui a tabela existente pela nova criada.
    index = False # Não considerar o index como uma coluna
)'''