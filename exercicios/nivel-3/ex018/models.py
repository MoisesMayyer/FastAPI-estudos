from sqlalchemy import Column, Integer, String, Boolean, Float

from database import Base


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column("Id",Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column("Nome",String, index=True)
    email = Column("Email",String, unique=True, index=True)
    senha = Column("Senha",String)
    ativo = Column("Ativo",Boolean, default=True, nullable=False)


class Produto(Base):
    __tablename__ = 'produtos'

    id = Column("Id",Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column("Nome", String, index=True, nullable=False)
    descricao = Column("Descricao",String)
    preco = Column("preco", Float, nullable=False)
    estoque =Column("estoque", Integer, nullable=False)
    ativo = Column("ativo", Boolean, default=True, nullable=False)