from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("Id",Integer, primary_key=True, index=True)
    nome = Column("Nome",String, index=True)
    email = Column("Email",String, unique=True, index=True)
    senha = Column("Senha",String)
    ativo = Column("Ativo",Boolean, default=True, nullable=False)