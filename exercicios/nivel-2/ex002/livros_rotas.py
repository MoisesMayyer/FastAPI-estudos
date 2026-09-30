from fastapi import APIRouter, HTTPException, status

from database import Session
from models import Livro, Autor
from datetime import datetime

rota_livros = APIRouter(prefix="/livros", tags=["livros"])


@rota_livros.post("/", status_code=status.HTTP_201_CREATED)
def adicionar_livro(titulo: str, ano_publicado: str, autor_id: int):
    session = Session()

    if not titulo.strip():
        session.close()
        raise HTTPException(status_code=400, detail="titulo é obrigatorio")

    try:
        data = datetime.strptime(ano_publicado, "%d/%m/%Y")
        if data > datetime.now():
            session.close()
            raise HTTPException(status_code=400, detail="ano de publicacao nao pode ser no futuro")
    except ValueError:
        session.close()
        raise HTTPException(
            status_code=400,
            detail="Data inválida. Use o formato DD/MM/YYYY."
        )

    autor = session.query(Autor).filter(Autor.id == autor_id).first()

    if not autor:
        session.close()
        raise HTTPException(
            status_code=400,
            detail="Autor não encontrado"
        )

    try:
        livro = Livro(titulo=titulo, ano_publicacao=ano_publicado, autor_id=autor.id)

        session.add(livro)
        session.commit()
        session.refresh(livro)
        return {
            "id": livro.id,
            "titulo": livro.titulo,
            "ano_publicacao": livro.ano_publicacao,
            "disponivel": livro.disponivel,
            "autor_id": livro.autor_id
        }
    finally:
        session.close()


@rota_livros.delete("/{id}")
def deletar_livro(id):
    pass


@rota_livros.put("/{id}")
def atualizar_livro(id):
    pass


@rota_livros.get("/")
def listar_livros():
    pass


@rota_livros.get("/{id}")
def listar_livro(id):
    pass
