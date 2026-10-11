from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UsuarioBase(BaseModel):
    nome: str = Field(..., min_length=3, description="Nome do usuário (obrigatório, mínimo 3 caracteres)")
    email: EmailStr = Field(..., description="Email do usuário (obrigatório)")

class UsuarioCreate(UsuarioBase):
    password: str = Field(...,min_length=8, description="Senha do usuário (obrigatório)")


class UsuarioUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, description="Novo nome do usuário (opcional)")
    email: Optional[EmailStr] = Field(None, description="Novo email do usuário (opcional, formato válido)")
    password: Optional[str] = Field(None, min_length=8, description="Nova senha do usuário (opcional, mínimo 8 caracteres)")
    active: Optional[bool] = Field(None, description="Status ativo/inativo (opcional)")


class UsuarioResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    active: bool

    class Config:
        from_attributes = True