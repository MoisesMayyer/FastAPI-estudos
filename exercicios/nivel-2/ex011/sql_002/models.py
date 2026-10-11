from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'pessoas'

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    nome = Column("nome",String)
    idade = Column("idade",Integer)
    nacionalidade = Column("nacionalidade",String)