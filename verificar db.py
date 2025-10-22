import psycopg2
from psycopg2 import OperationalError

def conectar():

    try:
        conexao = psycopg2.connect(
            dbname="loja_virtual",
            user="postgres",
            password="senaisp",
            host="localhost",
            port="5432"
        )

        print(" ✅conexão com o banco de dados bem-sucedida!")
        conexao.close()

    except OperationalError as e:
            print(" ❌ Erro ao conectar ao banco de dados")
            print(e)

conectar()