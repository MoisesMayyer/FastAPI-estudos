from fastapi import APIRouter, HTTPException
from models import Autor, Livro
from database import Session


rota_autores = APIRouter(prefix="/autores", tags=["autores"])


@rota_autores.post("/")
def adicionar_autor(nome: str, email: str):
    if not nome.strip() or not email.strip():
        raise HTTPException(status_code=400, detail="nome e email sao obrigatorios")

    session = Session()
    autor = Autor(nome=nome, email=email)
    session.add(autor)
    session.commit()
    session.refresh(autor)
    session.close()
    return {"id": autor.id, "nome": autor.nome, "email": autor.email}


@rota_autores.delete("/{id}")
def remover_autor(id: int):
    session = Session()
    autor = session.get(Autor, id)

    if autor is None:
        session.close()
        raise HTTPException(status_code=404, detail="autor nao encontrado")

    tem_livro = session.query(Livro).filter(Livro.autor_id == id).first()

    if tem_livro:
        session.close()
        raise HTTPException(status_code=400, detail="autor possui livros")

    session.delete(autor)
    session.commit()
    session.close()
    return {"id": autor.id, "nome": autor.nome, "email": autor.email}


@rota_autores.get("/")
def listar_autores():
    session = Session()

    try:
        autors = session.query(Autor).all()
        resultado = []
        for a in autors:
            resultado.append({
                "id": a.id,
                "nome": a.nome,
                "email": a.email
            })

        return resultado
    finally:
        session.close()


@rota_autores.get("/{id}")
def listar_autor(id: int):

    session = Session()

    try:
        autor = session.get(Autor, id)

        if autor is None:
            raise HTTPException(status_code=404, detail="autor não encontrado")

        return {
            "id": autor.id,
            "nome": autor.nome,
            "email": autor.email
        }
    finally:
        session.close()


@rota_autores.put("/{id}")
def alterar_autor(id: int, nome: str, email: str):
    session = Session()
    try:
        autor = session.get(Autor, id)
        if autor is None:
            raise HTTPException(404, detail="autor nao encontrado")

        if not nome.strip() or not email.strip():
            raise HTTPException(400, detail="nome e email sao obrigatorios")

        autor.nome = nome
        autor.email = email

        session.commit()
        return {"id": autor.id, "nome": autor.nome, "email": autor.email}
    finally:
        session.close()