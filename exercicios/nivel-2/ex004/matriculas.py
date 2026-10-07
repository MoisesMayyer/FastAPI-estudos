from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from schemas import MatriculaCreate, MatriculaUpdate, MatriculaList, MatriculaResponse
from models import Matricula, Aluno, Plano
from depends import get_db

rota_matriculas = APIRouter(prefix="/matriculas", tags=["matriculas"])


@rota_matriculas.post("/", response_model=MatriculaResponse)  # Cria matrícula validando aluno/plano ativos, datas, e aluno sem matrícula ativa
def criar_matricula(dados: MatriculaCreate, db: Session = Depends(get_db)):
    # Valida aluno existe e está ativo
    aluno = db.query(Aluno).filter(Aluno.id == dados.aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno inexistente")
    if not aluno.ativo:
        raise HTTPException(status_code=409, detail="Aluno inativo não pode receber matrícula")

    # Valida plano existe e está ativo
    plano = db.query(Plano).filter(Plano.id == dados.plano_id).first()
    if not plano:
        raise HTTPException(status_code=404, detail="Plano inexistente")
    if not plano.ativo:
        raise HTTPException(status_code=409, detail="Plano inativo não pode receber matrícula")

    # Valida datas
    if dados.data_fim <= dados.data_inicio:
        raise HTTPException(status_code=400, detail="data_fim deve ser posterior à data_inicio")

    # Regra: aluno não pode ter duas matrículas ativas simultâneas
    matricula_ativa = db.query(Matricula).filter(
        Matricula.aluno_id == dados.aluno_id, Matricula.ativa == True
    ).first()
    if matricula_ativa:
        raise HTTPException(status_code=409, detail="Aluno já possui matrícula ativa")

    matricula = Matricula(
        aluno_id=dados.aluno_id,
        plano_id=dados.plano_id,
        data_inicio=dados.data_inicio,
        data_fim=dados.data_fim,
        ativa=True
    )
    db.add(matricula)
    db.commit()
    db.refresh(matricula)
    return matricula


@rota_matriculas.get("/", response_model=List[MatriculaList])  # Retorna todas as matrículas (lista leve)
def listar_matriculas(db: Session = Depends(get_db)):
    return db.query(Matricula).all()


@rota_matriculas.get("/{id}", response_model=MatriculaResponse)  # Retorna matrícula por ID ou 404
def buscar_matricula(id: int, db: Session = Depends(get_db)):
    matricula = db.query(Matricula).filter(Matricula.id == id).first()
    if not matricula:
        raise HTTPException(status_code=404, detail="Matrícula inexistente")
    return matricula


@rota_matriculas.put("/{id}", response_model=MatriculaResponse)  # Atualiza matrícula; valida FKs se mudados, data_fim>data_inicio, permite cancelar (ativa=False)
def atualizar_matricula(id: int, dados: MatriculaUpdate, db: Session = Depends(get_db)):
    matricula = db.query(Matricula).filter(Matricula.id == id).first()
    if not matricula:
        raise HTTPException(status_code=404, detail="Matrícula inexistente")

    # Valida aluno se enviado
    if dados.aluno_id is not None and dados.aluno_id != matricula.aluno_id:
        aluno = db.query(Aluno).filter(Aluno.id == dados.aluno_id).first()
        if not aluno:
            raise HTTPException(status_code=404, detail="Aluno inexistente")
        if not aluno.ativo:
            raise HTTPException(status_code=409, detail="Aluno inativo não pode receber matrícula")
        # Verifica se novo aluno já tem matrícula ativa (exceto a atual)
        outra_ativa = db.query(Matricula).filter(
            Matricula.aluno_id == dados.aluno_id,
            Matricula.ativa == True,
            Matricula.id != id
        ).first()
        if outra_ativa:
            raise HTTPException(status_code=409, detail="Aluno já possui outra matrícula ativa")
        matricula.aluno_id = dados.aluno_id

    # Valida plano se enviado
    if dados.plano_id is not None and dados.plano_id != matricula.plano_id:
        plano = db.query(Plano).filter(Plano.id == dados.plano_id).first()
        if not plano:
            raise HTTPException(status_code=404, detail="Plano inexistente")
        if not plano.ativo:
            raise HTTPException(status_code=409, detail="Plano inativo não pode receber matrícula")
        matricula.plano_id = dados.plano_id

    # Atualiza datas se enviadas
    nova_inicio = dados.data_inicio if dados.data_inicio is not None else matricula.data_inicio
    nova_fim = dados.data_fim if dados.data_fim is not None else matricula.data_fim

    if nova_fim <= nova_inicio:
        raise HTTPException(status_code=400, detail="data_fim deve ser posterior à data_inicio")

    matricula.data_inicio = nova_inicio
    matricula.data_fim = nova_fim

    # Atualiza status ativa se enviado (permite cancelar)
    if dados.ativa is not None:
        matricula.ativa = dados.ativa

    db.commit()
    db.refresh(matricula)
    return matricula


@rota_matriculas.delete("/{id}")  # Cancela matrícula (ativa=False); retorna matrícula cancelada
def cancelar_matricula(id: int, db: Session = Depends(get_db)):
    matricula = db.query(Matricula).filter(Matricula.id == id).first()
    if not matricula:
        raise HTTPException(status_code=404, detail="Matrícula inexistente")

    matricula.ativa = False
    db.commit()
    db.refresh(matricula)
    return matricula