from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schemas import PlanoCreate, PlanoUpdate, PlanoList, PlanoResponse
from models import Plano, Matricula
from depends import get_db

rota_planos = APIRouter(prefix="/planos", tags=["planos"])


@rota_planos.post("/", response_model=PlanoResponse)  # Cria plano validando nome único, preço/duração > 0, ativo=True default
def criar_plano(dados: PlanoCreate, db: Session = Depends(get_db)):
    # Verifica nome único
    plano_existe = db.query(Plano).filter(Plano.nome == dados.nome).first()
    if plano_existe:
        raise HTTPException(status_code=409, detail="Plano já cadastrado")

    plano = Plano(nome=dados.nome, preco=dados.preco, duracao_dias=dados.duracao_dias, ativo=True)
    db.add(plano)
    db.commit()
    db.refresh(plano)
    return plano


@rota_planos.get("/", response_model=List[PlanoList])  # Retorna todos os planos (lista leve)
def listar_planos(db: Session = Depends(get_db)):
    return db.query(Plano).all()


@rota_planos.get("/{id}", response_model=PlanoResponse)  # Retorna plano por ID ou 404
def buscar_plano(id: int, db: Session = Depends(get_db)):
    plano = db.query(Plano).filter(Plano.id == id).first()
    if not plano:
        raise HTTPException(status_code=404, detail="Plano inexistente")
    return plano


@rota_planos.put("/{id}", response_model=PlanoResponse)  # Atualiza plano; valida nome único se mudado; não desativa se tem matrículas ativas
def atualizar_plano(id: int, dados: PlanoUpdate, db: Session = Depends(get_db)):
    plano = db.query(Plano).filter(Plano.id == id).first()
    if not plano:
        raise HTTPException(status_code=404, detail="Plano inexistente")

    # Valida nome único se enviado e diferente
    if dados.nome is not None and dados.nome != plano.nome:
        nome_existe = db.query(Plano).filter(Plano.nome == dados.nome).first()
        if nome_existe:
            raise HTTPException(status_code=409, detail="Nome de plano já cadastrado")
        plano.nome = dados.nome

    # Atualiza campos enviados
    if dados.preco is not None:
        plano.preco = dados.preco
    if dados.duracao_dias is not None:
        plano.duracao_dias = dados.duracao_dias

    # Regra: não pode desativar plano que possui matrículas ativas
    if dados.ativo is not None:
        if not dados.ativo:
            matricula_ativa = db.query(Matricula).filter(
                Matricula.plano_id == id, Matricula.ativa == True
            ).first()
            if matricula_ativa:
                raise HTTPException(
                    status_code=409, detail="Não pode desativar plano com matrículas ativas"
                )
        plano.ativo = dados.ativo

    db.commit()
    db.refresh(plano)
    return plano


@rota_planos.delete("/{id}")  # Deleta plano se não tem matrículas ativas; retorna 204
def deletar_plano(id: int, db: Session = Depends(get_db)):
    plano = db.query(Plano).filter(Plano.id == id).first()
    if not plano:
        raise HTTPException(status_code=404, detail="Plano inexistente")

    # Regra: não pode excluir plano com matrículas ativas
    matricula_ativa = db.query(Matricula).filter(
        Matricula.plano_id == id, Matricula.ativa == True
    ).first()
    if matricula_ativa:
        raise HTTPException(status_code=409, detail="Plano possui matrículas ativas")

    db.delete(plano)
    db.commit()
    return None