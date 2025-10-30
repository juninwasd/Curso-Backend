import json
import os
import uuid
import csv
import io
from decimal import Decimal
from pathlib import Path
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
from flask import (
    request, redirect, url_for, render_template, flash, jsonify,
    make_response, send_file, abort, send_from_directory
)
from flask_login import login_required
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
from sqlalchemy import func

# módulos locais
from app import app, db
import auth
import admin
from models import Cliente, Produto, Categoria, Fornecedor, Pedido, ItemPedido, Arquivo
from auth import role_required

# ===========================
# CONFIGURAÇÕES
# ===========================
app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "uploads")
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# ===========================
# MENU PRINCIPAL
# ===========================
@app.route("/", methods=["GET"])
@login_required
def home():
    return render_template("index.html")

# ----------------------------
# CLIENTES
# ----------------------------
@app.route("/clientes", methods=["GET"])
@login_required
def listar_clientes():
    clientes = Cliente.query.order_by(Cliente.id.desc()).all()
    return render_template("clientes.html", clientes=clientes)

@app.route("/clientes", methods=["POST"])
@role_required("admin", "operador")
def cadastrar_cliente():
    nome = request.form.get("nome")
    email = request.form.get("email") or None
    if not nome:
        return "Nome é obrigatório", 400
    c = Cliente(nome=nome, email=email)
    db.session.add(c)
    db.session.commit()
    return redirect(url_for("listar_clientes"))

@app.route("/clientes/editar/<int:id>", methods=["GET"])
@role_required("admin", "operador")
def form_editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return render_template("clientes_editar.html", cliente=cliente)

@app.route("/clientes/editar/<int:id>", methods=["POST"])
@role_required("admin", "operador")
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    nome = request.form.get("nome")
    email = request.form.get("email") or None
    if not nome:
        flash("Nome é obrigatório.", "error")
        return redirect(url_for("form_editar_cliente", id=id))
    try:
        cliente.nome = nome
        cliente.email = email
        db.session.commit()
        flash("Cliente atualizado com sucesso!", "success")
        return redirect(url_for("listar_clientes"))
    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao atualizar cliente: {e}", "error")
        return redirect(url_for("form_editar_cliente", id=id))

# ----------------------------
# PRODUTOS
# ----------------------------
@app.route("/produtos", methods=["GET"])
@login_required
def listar_produtos():
    produtos = Produto.query.order_by(Produto.id.desc()).all()
    categorias = Categoria.query.order_by(Categoria.nome.asc()).all()
    return render_template("produtos.html", produtos=produtos, categorias=categorias)

@app.route("/produtos", methods=["POST"])
@role_required("admin", "operador")
def cadastrar_produto():
    nome = request.form.get("nome")
    preco = request.form.get("preco", type=float)
    estoque = request.form.get("estoque", type=int, default=0)
    categoria_id = request.form.get("categoria_id", type=int)

    if not nome or preco is None:
        flash("Nome e preço são obrigatórios.", "error")
        return redirect(url_for("listar_produtos"))

    try:
        p = Produto(nome=nome, preco=preco, estoque=estoque, categoria_id=categoria_id)
        db.session.add(p)
        db.session.commit()
        flash("Produto cadastrado com sucesso!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao cadastrar: {e}", "error")

    return redirect(url_for("listar_produtos"))

@app.route("/produtos/editar/<int:id>", methods=["GET"])
@role_required("admin", "operador")
def form_editar_produto(id):
    produto = Produto.query.get_or_404(id)
    categorias = Categoria.query.order_by(Categoria.nome.asc()).all()
    return render_template("produtos_editar.html", produto=produto, categorias=categorias)

@app.route("/produtos/editar/<int:id>", methods=["POST"])
@role_required("admin", "operador")
def editar_produto(id):
    produto = Produto.query.get_or_404(id)
    nome = request.form.get("nome")
    preco = request.form.get("preco", type=float)
    estoque = request.form.get("estoque", type=int)
    categoria_id = request.form.get("categoria_id", type=int)

    if not nome or preco is None:
        flash("Nome e preço são obrigatórios.", "error")
        return redirect(url_for("form_editar_produto", id=id))

    try:
        produto.nome = nome
        produto.preco = preco
        produto.estoque = estoque if estoque is not None else produto.estoque
        produto.categoria_id = categoria_id
        db.session.commit()
        flash("Produto atualizado com sucesso!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao atualizar produto: {e}", "error")

    return redirect(url_for("listar_produtos"))

# ----------------------------
# UPLOADS
# ----------------------------
ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".txt", ".csv", ".xlsx"}
ALLOWED_MIME = {
    "image/png", "image/jpeg", "image/gif",
    "application/pdf", "text/plain",
    "text/csv", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
}

def allowed_file(filename: str, mimetype: str | None) -> bool:
    ext = Path(filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        return False
    if mimetype and mimetype not in ALLOWED_MIME:
        return False
    return True

@app.route("/uploads", methods=["GET"])
@login_required
def listar_arquivos():
    arquivos = Arquivo.query.order_by(Arquivo.id.desc()).all()
    return render_template("arquivos.html", arquivos=arquivos)

@app.errorhandler(RequestEntityTooLarge)
@login_required
def handle_large_file(e):
    flash("Arquivo(s) muito grande(s). Limite de 10MB por envio.", "error")
    return redirect(url_for("listar_arquivos"))

# ----------------------------
# UTILITÁRIOS
# ----------------------------
def parse_date(dstr: str | None):
    if not dstr:
        return None
    for fmt in ("%d/%m/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(dstr, fmt)
        except ValueError:
            continue
    return None

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
