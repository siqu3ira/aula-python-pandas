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

QUERY = """
    SELECT
        TIME,
        OPEN
    FROM preco_criptomoedas
    WHERE OPEN > 54657
"""

output = pd.read_sql(QUERY, conn_obj)

conn_obj.close() # Boa prática encerrar a conexão 
print(output.head())