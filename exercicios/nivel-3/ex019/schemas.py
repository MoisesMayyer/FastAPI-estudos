from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional


class UsuarioBase(BaseModel):
    nome: str = Field(..., min_length=3, description="Nome do usuário (obrigatório, mínimo 3 caracteres)")
    email: EmailStr = Field(..., description="Email do usuário (obrigatório)")

    @field_validator("nome", "email", mode="before")
    @classmethod
    def limpar_texto(cls, valor):
        if isinstance(valor, str):
            valor = valor.strip()

        return valor


class UsuarioCreate(UsuarioBase):
    senha: str = Field(..., min_length=8, description="Senha do usuário (obrigatório)")

    @field_validator("senha")
    @classmethod
    def validar_senha(cls, valor: str) -> str:
        if not valor.strip():
            raise ValueError("A senha não pode conter apenas espaços")

        return valor


class UsuarioUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=3, description="Novo nome do usuário (opcional)")
    email: Optional[EmailStr] = Field(None, description="Novo email do usuário (opcional, formato válido)")
    senha: Optional[str] = Field(None, min_length=8, description="Nova senha do usuário (opcional, mínimo 8 caracteres)")
    ativo: Optional[bool] = Field(None, description="Status ativo/inativo (opcional)")


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    ativo: bool

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ProjetoBase(BaseModel):
    nome: str = Field(..., min_length=3, description="Nome do projeto")
    descricao: str = Field(..., min_length=3, description="descrição do projeto")


class ProjetoCreate(ProjetoBase):

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor: str) -> str:
        if not valor.strip():
            raise ValueError("A nome não pode conter apenas espaços")

        return valor


class ProjetoUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=3, description="Nome do projeto")
    descricao: Optional[str] = Field(None, min_length=3, description="descrição do projeto")

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor):
        if valor is not None and not valor.strip():
            raise ValueError("A nome não pode conter apenas espaços")

        return valor


class ProjetoResponse(ProjetoBase):
    id: int
    nome: str
    descricao: str
    usuario_id: int

    class Config:
        from_attributes = True


class TarefaBase(BaseModel):
    titulo: str = Field(..., min_length=3, description="Título da tarefa")
    descricao: str = Field(..., min_length=3, description="descrição da tarefa")


class TarefaCreate(TarefaBase):

    @field_validator("titulo")
    @classmethod
    def validar_titulo(cls, valor: str) -> str:
        if not valor.strip():
            raise ValueError("O título não pode conter apenas espaços")

        return valor


class TarefaUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=3, description="Título da tarefa")
    descricao: Optional[str] = Field(None, min_length=3, description="descrição da tarefa")
    concluida: Optional[bool] = Field(None, description="Status concluída/pendente da tarefa")

    @field_validator("titulo")
    @classmethod
    def validar_titulo(cls, valor):
        if valor is not None and not valor.strip():
            raise ValueError("O título não pode conter apenas espaços")

        return valor


class TarefaResponse(TarefaBase):
    id: int
    titulo: str
    descricao: str
    concluida: bool
    projeto_id: int

    class Config:
        from_attributes = True