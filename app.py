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

cursor.execute("INSERT INTO usuarios (nome,preco,estoque) VALUES (?,?,?)", ("feijao", 20, 10))
cursor.execute("INSERT INTO usuarios (nome,preco,estoque) VALUES (?,?,?)", ("macarrao", 15, 15))
cursor.execute("INSERT INTO usuarios (nome,preco,estoque) VALUES (?,?,?)", ("carne", 30, 20))

conexao.commit()
conexao.close()

if __name__ == "__main__":
    app.run(debug=True)
