from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import Aluno, Matricula
from schemas import AlunoCreate,AlunoList, AlunoResponse, AlunoUpdate
from depends import get_db
from security import pwd_context

rota_alunos = APIRouter(prefix="/alunos", tags=["alunos"])


@rota_alunos.post("/", response_model=AlunoResponse)
def cadastrar_aluno(dados: AlunoCreate, db: Session = Depends(get_db)):


    aluno_existe = db.query(Aluno).filter(Aluno.email == dados.email).first()

    if aluno_existe:
        raise HTTPException(status_code=409, detail="aluno ja cadastrado")

    if not dados.email.strip():
        raise HTTPException(status_code=400, detail="o campo email nao deve ser vazio")

    senha_hash = pwd_context.hash(dados.senha)
    aluno = Aluno(
        nome=dados.nome,
        email=dados.email,
        senha=senha_hash,
        ativo=True
    )

    db.add(aluno)
    db.commit()
    db.refresh(aluno)

    return aluno


@rota_alunos.delete("/{id}")
def deletar_aluno(id:int, db: Session = Depends(get_db)):

    aluno_existe = db.query(Aluno).filter(Aluno.id == id).first()
    if not aluno_existe:
        raise HTTPException(status_code=404, detail="Aluno Inexistente")

    matricula = db.query(Matricula).filter(Matricula.aluno_id == id, Matricula.ativa == True).first()
    if matricula:
        raise HTTPException(status_code=409, detail="Matricula ainda esta ativa")


    db.delete(aluno_existe)
    db.commit()
    return None


@rota_alunos.put("/{id}", response_model=AlunoResponse)
def atualizar_aluno(id: int, dados: AlunoUpdate, db: Session = Depends(get_db)):
    # Busca aluno no banco
    aluno = db.query(Aluno).filter(Aluno.id == id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno Inexistente")

    # Valida e atualiza email se enviado e diferente do atual
    if dados.email is not None and dados.email != aluno.email:
        email_existe = db.query(Aluno).filter(Aluno.email == dados.email).first()
        if email_existe:
            raise HTTPException(status_code=409, detail="Email já cadastrado")
        aluno.email = dados.email

    # Atualiza nome se enviado
    if dados.nome is not None:
        aluno.nome = dados.nome

    # Atualiza senha com hash se enviada
    if dados.senha is not None:
        aluno.senha = pwd_context.hash(dados.senha)

    # Valida regra de negócio antes de desativar: impede se houver matrícula ativa
    if dados.ativo is not None:
        if not dados.ativo:
            matricula_ativa = db.query(Matricula).filter(
                Matricula.aluno_id == id, Matricula.ativa == True
            ).first()
            if matricula_ativa:
                raise HTTPException(
                    status_code=409, detail="Não pode desativar aluno com matrícula ativa"
                )
        aluno.ativo = dados.ativo

    db.commit()
    db.refresh(aluno)
    return aluno


@rota_alunos.get("/", response_model=List[AlunoList])
def pegar_alunos(db: Session = Depends(get_db)):

    alunos = db.query(Aluno).all()
    return alunos

@rota_alunos.get("/{id}", response_model= AlunoResponse)
def pegar_aluno(id: int, db: Session = Depends(get_db)):

    aluno_existe = db.query(Aluno).filter(Aluno.id == id).first()
    if not aluno_existe:
        raise HTTPException(status_code=404, detail="Aluno Inexistente")

    return aluno_existe