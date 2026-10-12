from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from dependencies import get_db, verificar_token
from models import Tarefa, Usuario
from schemas import TarefaCreate, TarefaResponse, TarefaUpdate

tarefas_router = APIRouter(prefix="/tarefas", tags=["tarefas"])


@tarefas_router.post("/", response_model=TarefaResponse, status_code=status.HTTP_201_CREATED)
async def criar_tarefa(
    dados: TarefaCreate,
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(verificar_token)  # usuário logado via JWT
):

    nova_tarefa = Tarefa(
        titulo=dados.titulo,
        descricao=dados.descricao,
        usuario_id=usuario_atual.id,  # dono da tarefa = usuário do token
        concluida=False
    )

    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)

    return nova_tarefa


@tarefas_router.get("/", response_model=list[TarefaResponse])
async def listar_tarefas(
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(verificar_token)
):
    # Busca apenas tarefas onde usuario_id == id do usuário logado
    tarefas = db.query(Tarefa).filter(Tarefa.usuario_id == usuario_atual.id).all()
    return tarefas


@tarefas_router.get("/{id}", response_model=TarefaResponse)
async def obter_tarefa(
    id: int,
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(verificar_token)
):
    # Busca tarefa pelo ID
    tarefa = db.query(Tarefa).filter(Tarefa.id == id).first()

    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    # Verifica se a tarefa pertence ao usuário autenticado
    if tarefa.usuario_id != usuario_atual.id:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return tarefa


@tarefas_router.put("/{id}", response_model=TarefaResponse)
async def atualizar_tarefa(
    id: int,
    dados: TarefaUpdate,
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(verificar_token)
):
    tarefa = db.query(Tarefa).filter(Tarefa.id == id).first()

    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    if tarefa.usuario_id != usuario_atual.id:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    if dados.titulo is not None:
        tarefa.titulo = dados.titulo
    if dados.descricao is not None:
        tarefa.descricao = dados.descricao
    if dados.concluida is not None:
        tarefa.concluida = dados.concluida

    db.commit()
    db.refresh(tarefa)

    return tarefa


@tarefas_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_tarefa(
    id: int,
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(verificar_token)
):
    tarefa = db.query(Tarefa).filter(Tarefa.id == id).first()

    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    if tarefa.usuario_id != usuario_atual.id:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    db.delete(tarefa)
    db.commit()

    return None