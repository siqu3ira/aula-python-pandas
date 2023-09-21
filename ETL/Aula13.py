import pandas as pd 
import numpy as np
import datetime as dt
import requests as r

credenciais = {
    'username': 'alunoharve',
    'password': "wj7Hs2itAhv$",
    'hostname': 'ip-69-164-197-170.cloudezapp.io',
    'port': 3306,
    'database': 'harve_alunos.sql'
}

STRING_DE_CONEXAO = "mysql+pymysql://{}:{}@{}:{}/{}".format(
    credenciais['username'], credenciais['password'], credenciais['hostname'], credenciais['port'], credenciais['database'])

print("\nExemplo p/ um banco MySQL -> {}\n".format(STRING_DE_CONEXAO))