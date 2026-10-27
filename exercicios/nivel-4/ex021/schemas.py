from pydantic import BaseModel


class TarefaCreate(BaseModel):
    titulo: str
    descricao: str
    concluida: bool = False


class TarefaResponse(TarefaCreate):
    id: int