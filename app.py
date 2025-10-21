import sqlite3
from pathlib import Path



def criar_banco():
    conexao = sqlite3.connect("loja.db")
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL
    )
    """)
    conexao.commit()
    conexao.close()

def inserir_produtos():

    conexao = sqlite3.connect('loja.db')
    cursor =  conexao.cursor()
    produtos = [
        ("Camiseta", 49.90, 28),
        ("Bone", 29.90, 15),
        ("Tênis", 199.00, 10)
    ]
    cursor.executemany ('INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)', produtos)
    conexao.commit()
    conexao.close()

def listar_produtos():
    conexao = sqlite3.connect('loja.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    print("\n Lista de produtos cadastrados:")
    print("-" * 48)
    for produto in produtos:
        print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: RS {produto[2]:.24} | Estoque: {produto[3]}")
    print(40)
    conexao.close()
    
criar_banco()
inserir_produtos()
listar_produtos()