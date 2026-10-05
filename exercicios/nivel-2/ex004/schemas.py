from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


class AlunoBase(BaseModel):
    nome: str = Field(..., min_length=1, description="Nome completo do aluno (obrigatório)")
    email: EmailStr = Field(..., description="Email único do aluno (obrigatório, formato válido)")


class AlunoCreate(AlunoBase):
    senha: str = Field(..., min_length=6, description="Senha do aluno (mínimo 6 caracteres)")


class AlunoUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=1, description="Novo nome (opcional)")
    email: Optional[EmailStr] = Field(None, description="Novo email (opcional, único)")
    senha: Optional[str] = Field(None, min_length=6, description="Nova senha (opcional, mínimo 6)")
    ativo: Optional[bool] = Field(None, description="Status ativo/inativo (opcional)")


class AlunoList(BaseModel):
    id: int = Field(..., description="Identificador único")
    nome: str = Field(..., description="Nome do aluno")
    email: EmailStr = Field(..., description="Email do aluno")
    ativo: bool = Field(..., description="Status: True=ativo, False=inativo")

    class Config:
        from_attributes = True


class MatriculaSimples(BaseModel):
    id: int
    data_inicio: datetime
    data_fim: datetime
    ativa: bool

    class Config:
        from_attributes = True


class AlunoResponse(AlunoBase):
    id: int = Field(..., description="Identificador único")
    ativo: bool = Field(..., description="Status do aluno")
    matriculas: List[MatriculaSimples] = Field(default_factory=list, description="Lista de matrículas do aluno")

    class Config:
        from_attributes = True
