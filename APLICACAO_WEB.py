## Integração com Flask (rotas e templates) - Aqui entram as rotas @app.route integradas com o ORM
from decimal import Decimal
from flask import request, redirect, url_for, render_template, flash, send_from_directory, abort
from app import app, db
from sqlalchemy import func
import os
import uuid
from pathlib import Path
from werkzeug.utils import secure_filename
from models import Cliente, Produto, Categoria, Pedido, ItemPedido, Arquivo





# >>> MENU PRINCIPAL <<<
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# ----------------------------
# Clientes - GET - POST - UPDATE
# ----------------------------
@app.route("/clientes", methods=["GET"])
def listar_clientes():
    clientes = Cliente.query.order_by(Cliente.id.desc()).all()
    return render_template("clientes.html", clientes=clientes)

@app.route("/clientes", methods=["POST"])
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
def form_editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return render_template("clientes_editar.html", cliente=cliente)

@app.route("/clientes/editar/<int:id>", methods=["POST"])
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
# Produtos- listagem  GET e POST e UPDATE
# ----------------------------
@app.route("/produtos", methods=["GET"])
def listar_produtos():
    produtos = Produto.query.order_by(Produto.id.desc()).all()
    categorias = Categoria.query.order_by(Categoria.nome.asc()).all()
    return render_template("produtos.html", produtos=produtos, categorias=categorias)

@app.route("/produtos", methods=["POST"])
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
def form_editar_produto(id):
    produto = Produto.query.get_or_404(id)
    categorias = Categoria.query.order_by(Categoria.nome.asc()).all()
    return render_template("produtos_editar.html", produto=produto, categorias=categorias)

@app.route("/produtos/editar/<int:id>", methods=["POST"])
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
        return redirect(url_for("listar_produtos"))
    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao atualizar produto: {e}", "error")
        return redirect(url_for("form_editar_produto", id=id))

# ----------------------------
# Pedidos - listagem simples
# ----------------------------
@app.route("/pedidos", methods=["GET"])
def listar_pedidos():
    pedidos = Pedido.query.order_by(Pedido.id.desc()).all()
    return render_template("pedidos.html", pedidos=pedidos)

# ----------------------------
# Vendas - formulário e gravação
# ----------------------------
@app.route("/vendas/nova", methods=["GET"])
def form_venda():
    clientes = Cliente.query.order_by(Cliente.nome.asc()).all()
    produtos = Produto.query.order_by(Produto.nome.asc()).all()
    return render_template("vendas_nova.html", clientes=clientes, produtos=produtos)

@app.route("/vendas/nova", methods=["POST"])
def criar_venda():
    """
    Espera:
      - cliente_id (int)
      - itens (múltiplos inputs hidden) no formato "produto_id,qtd"
        exemplo: itens=1,2  (produto 1, quantidade 2)
    """
    cliente_id = request.form.get("cliente_id", type=int)
    itens_raw = request.form.getlist("itens")  # lista de strings "produto_id,qtd"

    if not cliente_id or not itens_raw:
        flash("Informe o cliente e pelo menos um item.", "error")
        return redirect(url_for("form_venda"))

    try:
        pedido = Pedido(cliente_id=cliente_id, status="pago")
        db.session.add(pedido)
        db.session.flush()  # garante pedido.id

        total = Decimal("0.00")

        for raw in itens_raw:
            try:
                produto_id_str, qtd_str = raw.split(",")
                produto_id = int(produto_id_str)
                qtd = int(qtd_str)
            except Exception:
                raise ValueError(f"Item inválido: {raw}")

            if qtd <= 0:
                raise ValueError("Quantidade deve ser >= 1.")

            produto = Produto.query.get(produto_id)
            if not produto:
                raise ValueError(f"Produto {produto_id} inexistente.")

            # Verifica estoque
            if produto.estoque < qtd:
                raise ValueError(f"Estoque insuficiente para {produto.nome} (disp: {produto.estoque}).")

            preco = Decimal(str(produto.preco))
            total += (preco * Decimal(qtd))

            # Baixa de estoque
            produto.estoque -= qtd

            db.session.add(ItemPedido(
                pedido_id=pedido.id,
                produto_id=produto.id,
                quantidade=qtd,
                preco_unitario=preco
            ))

        pedido.valor_total = total
        db.session.commit()
        flash("Venda registrada com sucesso!", "success")
        return redirect(url_for("listar_pedidos"))

    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao registrar venda: {e}", "error")
        return redirect(url_for("form_venda"))
    
# ===========================
# EXCLUSÕES (DELETE) COM REGRAS
# ===========================
@app.route("/clientes/excluir/<int:id>", methods=["POST"])
def excluir_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    # bloqueia se cliente tiver pedidos
    qtd_pedidos = Pedido.query.filter_by(cliente_id=id).count()
    if qtd_pedidos > 0:
        flash(f"Não é possível excluir: o cliente possui {qtd_pedidos} pedido(s).", "error")
        return redirect(url_for("listar_clientes"))
    try:
        db.session.delete(cliente)
        db.session.commit()
        flash("Cliente excluído com sucesso!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao excluir cliente: {e}", "error")
    return redirect(url_for("listar_clientes"))

@app.route("/produtos/excluir/<int:id>", methods=["POST"])
def excluir_produto(id):
    produto = Produto.query.get_or_404(id)
    # bloqueia se produto estiver em itens de pedido
    em_itens = db.session.query(func.count(ItemPedido.id)).filter_by(produto_id=id).scalar()
    if em_itens and em_itens > 0:
        flash(f"Não é possível excluir: o produto está em {em_itens} item(ns) de pedido.", "error")
        return redirect(url_for("listar_produtos"))
    try:
        db.session.delete(produto)
        db.session.commit()
        flash("Produto excluído com sucesso!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao excluir produto: {e}", "error")
    return redirect(url_for("listar_produtos"))

@app.route("/pedidos/excluir/<int:id>", methods=["POST"])
def excluir_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    try:
        db.session.delete(pedido)  # itens relacionados serão apagados pelo cascade
        db.session.commit()
        flash("Pedido excluído com sucesso!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao excluir pedido: {e}", "error")
    return redirect(url_for("listar_pedidos"))



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
        # se quiser ser menos rígido, remova esta verificação de mimetype
        return False
    return True

@app.route("/uploads", methods=["GET"])
def listar_arquivos():
    arquivos = Arquivo.query.order_by(Arquivo.id.desc()).all()
    return render_template("arquivos.html", arquivos=arquivos)

@app.route("/uploads", methods=["POST"])
def enviar_arquivos():
    """
    Form espera input name="files" multiple
    """
    if "files" not in request.files:
        flash("Nenhum arquivo enviado.", "error")
        return redirect(url_for("listar_arquivos"))

    files = request.files.getlist("files")
    if not files:
        flash("Nenhum arquivo selecionado.", "error")
        return redirect(url_for("listar_arquivos"))

    enviados = 0
    for f in files:
        if not f.filename:
            continue
        if not allowed_file(f.filename, f.mimetype):
            flash(f"Arquivo não permitido: {f.filename}", "error")
            continue

        safe_name = secure_filename(f.filename)
        # Garante nome único na pasta: <uuid>__<nome>
        unique_prefix = uuid.uuid4().hex[:12]
        stored_name = f"{unique_prefix}__{safe_name}"
        dest_dir = Path(app.config["UPLOAD_FOLDER"])
        dest_path = dest_dir / stored_name

        try:
            f.save(dest_path)
            size = dest_path.stat().st_size
            arq = Arquivo(
                nome_original=f.filename,
                nome_armazenado=stored_name,
                caminho=str(dest_path),
                mimetype=f.mimetype,
                tamanho_bytes=size,
            )
            db.session.add(arq)
            enviados += 1
        except Exception as e:
            flash(f"Falha ao salvar {f.filename}: {e}", "error")

    if enviados:
        try:
            db.session.commit()
            flash(f"{enviados} arquivo(s) enviado(s) com sucesso!", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Erro ao registrar no banco: {e}", "error")

    return redirect(url_for("listar_arquivos"))

@app.route("/uploads/download/<int:id>", methods=["GET"])
def download_arquivo(id):
    arq = Arquivo.query.get_or_404(id)
    dest_dir = Path(app.config["UPLOAD_FOLDER"])
    file_path = dest_dir / arq.nome_armazenado
    if not file_path.exists():
        abort(404)
    return send_from_directory(
        directory=str(dest_dir),
        path=arq.nome_armazenado,
        as_attachment=True,
        download_name=arq.nome_original,
        mimetype=arq.mimetype or "application/octet-stream"
    )

@app.route("/uploads/excluir/<int:id>", methods=["POST"])
def excluir_arquivo(id):
    arq = Arquivo.query.get_or_404(id)
    try:
        # tenta remover o arquivo do disco
        file_path = Path(arq.caminho)
        if file_path.exists():
            file_path.unlink()
        db.session.delete(arq)
        db.session.commit()
        flash("Arquivo excluído com sucesso!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao excluir: {e}", "error")
    return redirect(url_for("listar_arquivos"))

# Trata requisições maiores que MAX_CONTENT_LENGTH
from werkzeug.exceptions import RequestEntityTooLarge

@app.errorhandler(RequestEntityTooLarge)
def handle_large_file(e):
    flash("Arquivo(s) muito grande(s). Limite de 10MB por envio.", "error")
    return redirect(url_for("listar_arquivos"))
	

if __name__ == "__main__":
    # Executa servidor para testar as rotas
    app.run(debug=True)

