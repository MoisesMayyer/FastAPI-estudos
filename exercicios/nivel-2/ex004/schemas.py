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



class PlanoBase(BaseModel):
    nome: str = Field(..., min_length=1, description="Nome do plano (obrigatório, único)")
    preco: float = Field(..., gt=0, description="Preço do plano (obrigatório, > 0)")
    duracao_dias: int = Field(..., gt=0, description="Duração em dias (obrigatório, > 0)")



class PlanoCreate(PlanoBase):
    pass


class PlanoUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=1, description="Novo nome (opcional, único)")
    preco: Optional[float] = Field(None, gt=0, description="Novo preço (opcional, > 0)")
    duracao_dias: Optional[int] = Field(None, gt=0, description="Nova duração em dias (opcional, > 0)")
    ativo: Optional[bool] = Field(None, description="Ativar/desativar plano (opcional)")


class PlanoList(BaseModel):
    id: int
    nome: str
    preco: float
    duracao_dias: int
    ativo: bool

    class Config:
        from_attributes = True



class PlanoResponse(PlanoBase):
    id: int
    ativo: bool

    class Config:
        from_attributes = True



class MatriculaBase(BaseModel):
    aluno_id: int = Field(..., description="ID do aluno (obrigatório)")
    plano_id: int = Field(..., description="ID do plano (obrigatório)")
    data_inicio: datetime = Field(..., description="Data de início (obrigatório, ISO 8601)")
    data_fim: datetime = Field(..., description="Data de fim (obrigatório, deve ser > data_inicio)")



class MatriculaCreate(MatriculaBase):
    pass


class MatriculaUpdate(BaseModel):
    aluno_id: Optional[int] = Field(None, description="Novo ID do aluno (opcional)")
    plano_id: Optional[int] = Field(None, description="Novo ID do plano (opcional)")
    data_inicio: Optional[datetime] = Field(None, description="Nova data de início (opcional)")
    data_fim: Optional[datetime] = Field(None, description="Nova data de fim (opcional)")
    ativa: Optional[bool] = Field(None, description="Ativar/desativar matrícula (opcional)")


class MatriculaList(BaseModel):
    id: int
    aluno_id: int
    plano_id: int
    data_inicio: datetime
    data_fim: datetime
    ativa: bool

    class Config:
        from_attributes = True



class AlunoResumo(BaseModel):
    id: int
    nome: str
    email: EmailStr
    class Config:
        from_attributes = True

class PlanoResumo(BaseModel):
    id: int
    nome: str
    preco: float
    duracao_dias: int
    class Config:
        from_attributes = True


class MatriculaResponse(MatriculaBase):
    id: int
    ativa: bool
    aluno: AlunoResumo
    plano: PlanoResumo

    class Config:
        from_attributes = True