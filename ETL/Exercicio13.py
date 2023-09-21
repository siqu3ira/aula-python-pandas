import pandas as pd 
import numpy as np
import datetime as dt
import requests as r

credenciais = {
    'username': 'usuario',
    'password': "sdfs92",
    'hostname': 'ip-69-144-197-170.servermysql.io',
    'port': 3306,
    'database': 'criptomoedas'
}

STRING_DE_CONEXAO = "mysql+pymysql://{}:{}@{}:{}/{}".format(
    credenciais['username'], credenciais['password'], credenciais['hostname'], credenciais['port'], credenciais['database'])


print("\nExemplo p/ um banco MySQL -> {}\n".format(STRING_DE_CONEXAO))