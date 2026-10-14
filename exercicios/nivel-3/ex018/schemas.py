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


class ProdutoBase(BaseModel):
    nome: str = Field(..., min_length=2, description="Nome do produto (obrigatório, mínimo 2 caracteres)")
    descricao: Optional[str] = Field(None, description="Descrição do produto (opcional)")


class ProdutoCreate(ProdutoBase):
    preco: float = Field(..., gt=0, description="Preço do produto (deve ser maior que zero)")
    estoque: int = Field(..., ge=0, description="Estoque do produto (não pode ser negativo)")
    ativo: Optional[bool] = Field(True, description="Status ativo/inativo (padrão: true)")

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor: str) -> str:
        if not valor.strip():
            raise ValueError("O nome não pode conter apenas espaços")
        return valor


class ProdutoUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, description="Nome do produto (opcional)")
    descricao: Optional[str] = Field(None, description="Descrição do produto (opcional)")
    preco: Optional[float] = Field(None, gt=0, description="Preço do produto (deve ser maior que zero)")
    estoque: Optional[int] = Field(None, ge=0, description="Estoque do produto (não pode ser negativo)")
    ativo: Optional[bool] = Field(None, description="Status ativo/inativo (opcional)")

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor: Optional[str]) -> Optional[str]:
        if valor is not None and not valor.strip():
            raise ValueError("O nome não pode conter apenas espaços")
        return valor


class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: float
    estoque: int
    ativo: bool

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"