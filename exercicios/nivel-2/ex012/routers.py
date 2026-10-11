from decimal import Decimal

from fastapi import APIRouter, HTTPException
from database import Session
from models import Produto

rota_produtos = APIRouter(prefix="/produtos", tags=["produtos"])


@rota_produtos.post("/")
def produtos_adicionar(nome: str, valor: Decimal, estoque: int):
    session = Session()

    if valor <= 0 or estoque < 0:
        raise HTTPException(
            status_code=400,
            detail="valor e estoque não podem ser negativo"
        )

    nome_formatado = nome.strip().lower()
    if nome_formatado == '':
        raise HTTPException(
            status_code=400,
            detail="o nome nao pode ser vazio"
        )

    produto= Produto(nome=nome, preco=valor, estoque=estoque)

    session.add(produto)
    session.commit()
    session.close()

    return {"message": f"vc adicionou o produto: {nome}"}


@rota_produtos.get("/")
def produtos():
    session = Session()
    try:
        produtos = session.query(Produto).all()

        resultado = []
        for p in produtos:
            resultado.append({
                "id": p.id,
                "nome": p.nome,
                "preco": p.preco,
                "estoque": p.estoque,
                "ativo": p.ativo
            })

        return resultado
    finally:
        session.close()


@rota_produtos.get("/{id}")
def produto_id(id: int):
    session = Session()
    produto = session.get(Produto, id)

    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return {
        "id": produto.id,
        "nome": produto.nome,
        "preco": produto.preco,
        "estoque": produto.estoque,
        "ativo": produto.ativo
    }


@rota_produtos.put("/{id}")
def produtos_atualizar(id: int, nome: str, valor: Decimal, estoque: int, ativo: bool):
    session = Session()

    produto = session.get(Produto, id)
    if produto is None:
        session.close()
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    novo_nome = nome.strip().lower()
    if valor <= 0 or estoque < 0:
        session.close()
        raise HTTPException(status_code=400, detail="valores negativos nao sao permitidos")
    if novo_nome == "":
        session.close()
        raise HTTPException(status_code=400, detail="nome vazio nao é permitido")

    produto.nome = novo_nome
    produto.preco = valor
    produto.estoque = estoque
    produto.ativo = ativo

    session.commit()
    session.close()

    return {
        "id": produto.id,
        "nome": produto.nome,
        "preco": produto.preco,
        "estoque": produto.estoque,
        "ativo": produto.ativo
    }


@rota_produtos.delete("/{id}")
def produtos_deletar(id: int):
    session = Session()

    produto = session.get(Produto, id)
    if produto is None:
        session.close()
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    session.delete(produto)
    session.commit()
    session.close()

    return {"message": f"ID {id} deletado com sucesso"}