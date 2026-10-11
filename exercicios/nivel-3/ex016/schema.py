from pydantic import BaseModel, EmailStr, Field, field_validator
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


class AuthLogin(BaseModel):
    email: EmailStr = Field(..., description="Email do usuário (obrigatório)")
    senha: str = Field(..., min_length=8, description="Senha do usuário (obrigatório)")

    @field_validator("senha")
    @classmethod
    def validar_senha(cls, valor: str) -> str:
        if not valor.strip():
            raise ValueError("A senha não pode conter apenas espaços")

        return valor