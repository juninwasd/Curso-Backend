from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2

conexao = psycopg2.connect(
    dbname="loja_virtual",
    user="postgres",
    password="senaisp",
    host="localhost",
    port="5432"
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    concluida = db.Column(db.Boolean, default=False)

# Página principal
@app.route('/')
def index():
    tarefas = Task.query.all()
    return render_template('index.html', tarefas=tarefas)

# Adicionar nova tarefa
@app.route('/add', methods=['POST'])
def add():
    titulo = request.form['titulo']
    descricao = request.form['descricao']
    nova_tarefa = Task(titulo=titulo, descricao=descricao)
    db.session.add(nova_tarefa)
    db.session.commit()
    cursor = conexao.cursor()
    cursor.execute("""
                INSERT INTO clientes ( nome, email, telefone ) VALUES 
                ('Marcelo Breitenbach', 'Marcelo.breitenbach@sp.senai.br', '(19)9.8111-8959'),
                ('Junio da Silva', 'junio@oul.com.br', '(19)9.8888-1234'),
                ('Ana Julia', 'anaju@terra.com.br', '(19)9.1488-9595')
                ON CONFLICT (email) DO NOTHING;
    """)


    return redirect(url_for('index'))




# Marcar como concluída
@app.route('/concluir/<int:id>')
def concluir(id):
    tarefa = Task.query.get_or_404(id)
    tarefa.concluida = True
    db.session.commit()
    return redirect(url_for('index'))

# Remover tarefa
@app.route('/remover/<int:id>')
def remover(id):
    tarefa = Task.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for('index'))

# Criação do banco e execução
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)