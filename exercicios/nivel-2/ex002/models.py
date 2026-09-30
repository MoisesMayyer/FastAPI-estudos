from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Autor(Base):
    __tablename__ = 'autores'

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    nome = Column("nome",String, nullable=False)
    email = Column("email",String, nullable=False)


class Livro(Base):

    __tablename__ = 'livros'

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo",String, nullable=False)
    ano_publicacao = Column("ano_publicacao",String)
    disponivel = Column("disponivel",Boolean, default=True)
    autor_id = Column("autor_id",Integer, ForeignKey('autores.id'))