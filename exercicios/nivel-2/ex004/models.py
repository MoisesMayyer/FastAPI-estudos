from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float, DateTime
from sqlalchemy.orm import relationship
from database import Base


class Aluno(Base):
    __tablename__ = 'alunos'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False, unique=True)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, nullable=False, default=True)

    matriculas = relationship("Matricula", back_populates="aluno")


class Plano(Base):
    __tablename__ = 'planos'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False, unique=True)
    preco = Column("preco", Float, nullable=False)
    duracao_dias = Column("duracao_dias", Integer, nullable=False)
    ativo = Column("ativo", Boolean, nullable=False, default=True)

    matriculas = relationship("Matricula", back_populates="plano")


class Matricula(Base):
    __tablename__ = 'matriculas'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    aluno_id = Column("aluno_id", Integer, ForeignKey('alunos.id'), nullable=False)
    plano_id = Column("plano_id", Integer, ForeignKey('planos.id'), nullable=False)
    data_inicio = Column("data_inicio", DateTime, nullable=False)
    data_fim = Column("data_fim", DateTime, nullable=False)
    ativa = Column("ativa", Boolean, nullable=False, default=True)

    aluno = relationship("Aluno", back_populates="matriculas")
    plano = relationship("Plano", back_populates="matriculas")