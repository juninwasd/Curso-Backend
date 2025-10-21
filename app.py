import sqlite3
from pathlib import Path
from flask import Flask, render_template, jsonify


app = Flask(__name__)
conexao = sqlite3.connect("loja1.db")
cursor = conexao.cursor()
app.config['SQLITE3_DATABASE_URI'] = 'sqlite:///loja1.db'
app.config['SQLITE3_TRACK_MODIFICATIONS'] = False
db = sqlite3(app)
BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

def get_tarefas():
    return [
        {"id": 1, "titulo": "Estudar Flask", "descricao": "Rotas e templates", "concluida": True},
        {"id": 2, "titulo": "Criar API", "descricao": "Endpoints REST", "concluida": False},
        {"id": 3, "titulo": "Conectar DB", "descricao": "SQLAlchemy e migrações", "concluida": False},
    ]

# SSR (páginas)
@app.route("/")
def home():
    return render_template("index.html", tarefas=get_tarefas())

# API (JSON)
@app.route("/api/loja1")
def api_tarefas():
    return jsonify(get_tarefas())

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco TEXT UNIQUE NOT NULL,
    estoque TEXT UNIQUE NOT NULL
    )
        ''')
import sqlite3

def criar banco():

conexao sqlite3.connect("loja.db")

cursor conexao.cursor()

cursor.execute(

CREATE TABLE IF NOT EXISTS produtos (

id INTEGER PRIMARY KEY AUTOINCREMENT,

nome TEXT NOT NULL,

preco REAL NOT NULL,

estoque INTEGER NOT NULL

conexao.commit()

conexao.close()

def inserir_produtos():

conexao sqlite3.connect("loja.db')

cursor conexao.cursor()

produtos = [

("Camiseta", 49.90, 28),

("Bone", 29.90, 15),

("Tênis", 199.00, 10)

cursor.executemany (INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)', produtos)

conexao.commit()

conexao.close()

def listar produtos():

conexao sqlite3.connect('loja.db")

cursor conexao.cursor()

cursor.execute("SELECT FROM produtos")

produtos cursor.fetchall()

print("\n Lista de produtos cadastrados:")

print(48)

for produto in produtos:

print("ID: (produto[0]) | Nome: (produto[1]) | Preço: RS (produto[2]:.24] | Estoque: (produto[3]}")

print(40)

conexao.close() #Execução do fluxo completo.

criar_banco()

inserir produtos()

listar produtos()
