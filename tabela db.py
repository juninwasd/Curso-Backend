import psycopg2

conexao = psycopg2.connect(
    dbname="loja_virtual",
    user="postgres",
    password="senaisp",
    host="localhost",
    port="5432"
)
cursor = conexao.cursor()
cursor.execute("""
                INSERT INTO clientes ( nome, email, telefone ) VALUES 
                ('Marcelo Breitenbach', 'Marcelo.breitenbach@sp.senai.br', '(19)9.8111-8959'),
                ('Junio da Silva', 'junio@oul.com.br', '(19)9.8888-1234'),
                ('Ana Julia', 'anaju@terra.com.br', '(19)9.1488-9595')
                ON CONFLICT (email) DO NOTHING;
      
""")
conexao.commit()
cursor.close()
conexao.close()

print("Tabela 'clientes' criada com sucesso!")