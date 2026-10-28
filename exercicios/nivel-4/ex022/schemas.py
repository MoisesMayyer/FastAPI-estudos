from pydantic import BaseModel, Field
from typing import Optional

class ProdutoCreate(BaseModel):
    nome: str = Field(..., min_length=1, max_length=50)
    descricao: Optional[str] = Field(None, min_length=1, max_length=200)
    preco: float= Field(..., gt=0)
    disponivel: bool = True


class ProdutoUpdate(BaseModel):
    nome : Optional[str] = Field(None, min_length=1, max_length=50)
    descricao: Optional[str] = Field(None, min_length=1, max_length=200)
    preco: Optional[float] = Field(None, gt=0)
    disponivel: Optional[bool] = True



class ProdutoResponse(ProdutoCreate):
    id: int
