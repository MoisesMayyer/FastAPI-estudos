from sqlalchemy import Column, Integer, String
from database.database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False, unique=True, index=True)
    telefone = Column(String(20), nullable=False)
