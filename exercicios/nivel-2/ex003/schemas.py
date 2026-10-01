from pydantic import BaseModel,EmailStr
from typing import Optional


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr


class UsuarioCreate(UsuarioBase):
    senha: str


class UsuarioUpdate(BaseModel):

    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None


class UsuarioResponse(UsuarioBase):
    id: int
    ativo: bool = True

    class Config:
        from_attributes = True


class TarefaBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None


class TarefaCreate(TarefaBase):
    usuario_id: int


class TarefaUpdate(TarefaBase):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    concluida: Optional[bool] = None


class TarefaResponse(TarefaBase):
    id: int
    usuario_id: int
    concluida: bool

    class Config:
        from_attributes = True