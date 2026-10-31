from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional


TELEFONE_REGEX = r"^\+?[0-9]{10,15}$"


class ClienteBase(BaseModel):
    nome: str = Field(..., min_length=3, max_length=50)
    email: EmailStr


class ClienteCreate(ClienteBase):
    telefone: str = Field(..., pattern=TELEFONE_REGEX)


class ClienteUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    telefone: Optional[str] = Field(None, pattern=TELEFONE_REGEX)


class ClienteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome: str
    email: EmailStr
    telefone: str
