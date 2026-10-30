from sqlalchemy import Column, Integer, String
from database.database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False,)
    email = Column("email", String, nullable=False)
    telefone = Column("telefone", String(20), nullable=False)