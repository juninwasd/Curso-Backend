import psycopg2

conexao = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="senaisp",
    host="localhost",
    port="5432"
)
conexao.autocommit = True

cursor = conexao.cursor()
cursor.execute("CREATE DATABASE loja_virtual")
cursor.close()
conexao.close()

print("Banco de dados  'meubanco' criado com sucesso!")