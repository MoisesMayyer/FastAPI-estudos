from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import TarefaCreate, TarefaResponse
from models import Usuario, Tarefa
from depends import get_db


rota_tarefas = APIRouter(prefix="/tarefas", tags=["tarefas"])


@rota_tarefas.post("/", response_model=TarefaResponse, status_code=status.HTTP_201_CREATED)
def adicionar_tarefa(dados: TarefaCreate, db: Session = Depends(get_db)):
    usuario_existe = db.query(Usuario).filter(Usuario.id == dados.usuario_id).first()

    if not usuario_existe:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuário não encontrado")

    if not dados.titulo.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Título é obrigatório")

    descricao = dados.descricao
    if descricao is not None:
        descricao = descricao.strip()
        if not descricao:
            descricao = None

    tarefa = Tarefa(
        titulo=dados.titulo.strip(),
        descricao=descricao,
        usuario_id=dados.usuario_id
    )

    db.add(tarefa)
    db.commit()
    db.refresh(tarefa)

    return tarefa


@rota_tarefas.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_tarefa(id: int, db: Session = Depends(get_db)):
    tarefa_existe = db.query(Tarefa).filter(Tarefa.id == id).first()

    if not tarefa_existe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")

    db.delete(tarefa_existe)
    db.commit()

    return None


@rota_tarefas.put("/{id}")
def atualizar_tarefa():
    pass


@rota_tarefas.get("/", response_model=list[TarefaResponse])
def listar_tarefas(db: Session = Depends(get_db)):
    tarefas = db.query(Tarefa).all()

    return tarefas


@rota_tarefas.get("/{id}", response_model=TarefaResponse)
def listar_tarefa(id: int, db: Session = Depends(get_db)):
    tarefa_existe = db.query(Tarefa).filter(Tarefa.id == id).first()

    if not tarefa_existe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")

    return tarefa_existe