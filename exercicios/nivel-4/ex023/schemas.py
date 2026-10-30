from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class ClientBase(BaseModel):
    nome: str = Field(...,min_length=3, max_length=50)
    email: EmailStr = Field(...)


class ClientCreate(ClientBase):
    telefone: str = Field(
        pattern=r"^\+?[0-9]{10,15}$"
    )


class ClienteUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr]
    telefone: Optional[str]


class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    telefone: str

    class Config:
        from_attributes = True


