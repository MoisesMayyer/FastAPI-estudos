from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from depends import get_db, verificar_token
from models import Usuario, Tarefa, Projeto
from schemas import TarefaCreate, TarefaResponse, TarefaUpdate


tarefas_router = APIRouter(tags=["tarefas"])


@tarefas_router.get("/projetos/{projeto_id}/tarefas", response_model=list[TarefaResponse])
def listar_tarefas(projeto_id: int, db: Session = Depends(get_db), usuario: Usuario = Depends(verificar_token)):
    projeto = db.query(Projeto).filter(Projeto.id == projeto_id, Projeto.usuario_id == usuario.id).first()

    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    tarefas = db.query(Tarefa).filter(Tarefa.projeto_id == projeto.id).all()

    return tarefas


@tarefas_router.post("/projetos/{projeto_id}/tarefas", response_model=TarefaResponse)
def criar_tarefa(projeto_id: int, dados: TarefaCreate, db: Session = Depends(get_db), usuario: Usuario = Depends(verificar_token)):
    projeto = db.query(Projeto).filter(Projeto.id == projeto_id, Projeto.usuario_id == usuario.id).first()

    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    nova_tarefa = Tarefa(
        titulo=dados.titulo,
        descricao=dados.descricao,
        projeto_id=projeto.id,
    )

    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)

    return nova_tarefa


@tarefas_router.put("/tarefas/{id}", response_model=TarefaResponse)
def atualizar_tarefa(id: int, dados: TarefaUpdate, db: Session = Depends(get_db), usuario: Usuario = Depends(verificar_token)):
    tarefa = (
        db.query(Tarefa)
        .join(Projeto, Tarefa.projeto_id == Projeto.id)
        .filter(Tarefa.id == id, Projeto.usuario_id == usuario.id)
        .first()
    )

    if not tarefa:
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


@tarefas_router.delete("/tarefas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(id: int, db: Session = Depends(get_db), usuario: Usuario = Depends(verificar_token)):
    tarefa = (
        db.query(Tarefa)
        .join(Projeto, Tarefa.projeto_id == Projeto.id)
        .filter(Tarefa.id == id, Projeto.usuario_id == usuario.id)
        .first()
    )

    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    db.delete(tarefa)
    db.commit()

    return None
