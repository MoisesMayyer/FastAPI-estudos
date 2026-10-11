from sqlalchemy import Column, Integer, Float, String, Boolean
from database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    preco = Column("preco", Float)
    estoque = Column("estoque", Integer)
    ativo = Column("ativo", Boolean, default=True)