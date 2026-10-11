from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import Aluno, Matricula
from schemas import AlunoCreate, AlunoList, AlunoResponse, AlunoUpdate
from depends import get_db
from security import pwd_context

rota_alunos = APIRouter(prefix="/alunos", tags=["alunos"])


@rota_alunos.post("/", response_model=AlunoResponse)  # Cria aluno validando nome/email obrigatórios, email único, senha hash, ativo=True
def cadastrar_aluno(dados: AlunoCreate, db: Session = Depends(get_db)):
    # Validações ANTES de ir ao banco
    if not dados.nome.strip():
        raise HTTPException(status_code=400, detail="O campo nome não deve ser vazio")
    if not dados.email.strip():
        raise HTTPException(status_code=400, detail="O campo email não deve ser vazio")

    # Verifica email único (normaliza para lower)
    email_normalizado = dados.email.strip().lower()
    aluno_existe = db.query(Aluno).filter(Aluno.email == email_normalizado).first()
    if aluno_existe:
        raise HTTPException(status_code=409, detail="Email já cadastrado")

    senha_hash = pwd_context.hash(dados.senha)
    aluno = Aluno(nome=dados.nome.strip(), email=email_normalizado, senha=senha_hash, ativo=True)
    db.add(aluno)
    db.commit()
    db.refresh(aluno)
    return aluno


@rota_alunos.delete("/{id}")  # Deleta aluno se não tem matrícula ativa; retorna 204
def deletar_aluno(id: int, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.id == id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno inexistente")

    matricula_ativa = db.query(Matricula).filter(Matricula.aluno_id == id, Matricula.ativa == True).first()
    if matricula_ativa:
        raise HTTPException(status_code=409, detail="Aluno possui matrícula ativa")

    db.delete(aluno)
    db.commit()
    return None


@rota_alunos.put("/{id}", response_model=AlunoResponse)  # Atualiza aluno; valida email único, hash senha, não desativa se tem matrícula ativa
def atualizar_aluno(id: int, dados: AlunoUpdate, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.id == id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno inexistente")

    if dados.nome is not None:
        if not dados.nome.strip():
            raise HTTPException(status_code=400, detail="Nome não pode ser vazio")
        aluno.nome = dados.nome.strip()

    if dados.email is not None and dados.email != aluno.email:
        email_normalizado = dados.email.strip().lower()
        if not email_normalizado:
            raise HTTPException(status_code=400, detail="Email não pode ser vazio")
        email_existe = db.query(Aluno).filter(Aluno.email == email_normalizado).first()
        if email_existe:
            raise HTTPException(status_code=409, detail="Email já cadastrado")
        aluno.email = email_normalizado

    if dados.senha is not None:
        aluno.senha = pwd_context.hash(dados.senha)

    if dados.ativo is not None:
        if not dados.ativo:
            matricula_ativa = db.query(Matricula).filter(Matricula.aluno_id == id, Matricula.ativa == True).first()
            if matricula_ativa:
                raise HTTPException(status_code=409, detail="Não pode desativar aluno com matrícula ativa")
        aluno.ativo = dados.ativo

    db.commit()
    db.refresh(aluno)
    return aluno


@rota_alunos.get("/", response_model=List[AlunoList])  # Retorna todos os alunos (lista leve)
def listar_alunos(db: Session = Depends(get_db)):
    return db.query(Aluno).all()


@rota_alunos.get("/{id}", response_model=AlunoResponse)  # Retorna aluno por ID com matrículas aninhadas ou 404
def buscar_aluno(id: int, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.id == id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno inexistente")
    return aluno