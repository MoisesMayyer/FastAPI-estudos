from fastapi import APIRouter, HTTPException

from database import carregar_json, salvar_json
from schemas import TarefaResponse, TarefaCreate

tarefa_router = APIRouter(prefix="/tarefas", tags=["tarefas"])


def criar_id() -> int:
    lista_tarefas = carregar_json()

    maior_id = max(
        (tarefa["id"] for tarefa in lista_tarefas),
        default=0
    )

    return maior_id + 1

@tarefa_router.get("/", response_model=list[TarefaResponse])
async def pegar_tarefas():
    lista_tarefas = carregar_json()
    return lista_tarefas


@tarefa_router.get("/{id}", response_model=TarefaResponse)
async def pegar_tarefa(id: int):
    lista_tarefas = carregar_json()

    for tarefa in lista_tarefas:
        if tarefa["id"] == id:
            return tarefa

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )


@tarefa_router.post("/", response_model=TarefaResponse)
async def criar_tarefa(dados: TarefaCreate):
    lista_tarefas = carregar_json()

    nova_tarefa = TarefaResponse(
        id=criar_id(),
        titulo=dados.titulo,
        descricao=dados.descricao,
        concluida=dados.concluida,
    )

    lista_tarefas.append(nova_tarefa.model_dump())
    salvar_json(lista_tarefas)

    return nova_tarefa