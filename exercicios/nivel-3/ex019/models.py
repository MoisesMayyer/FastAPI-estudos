from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column("id",Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column("Nome",String, index=True)
    email = Column("Email",String, unique=True, index=True)
    senha = Column("Senha",String)
    ativo = Column("Ativo",Boolean, default=True, nullable=False)

    projetos = relationship("Projeto", back_populates="usuario")


class Projeto(Base):
    __tablename__ = 'projetos'

    id = Column("id",Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column("Nome",String, index=True)
    descricao = Column("Descricao", String)
    usuario_id = Column("Usuario_id",Integer, ForeignKey('usuarios.id'))

    usuario = relationship("Usuario", back_populates="projetos")
    tarefas = relationship("Tarefa", back_populates="projeto")


class Tarefa(Base):
    __tablename__ = 'tarefas'

    id = Column("id",Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column("Titulo",String, index=True)
    descricao = Column("Descricao", String)
    concluida = Column("Concluida",Boolean, default=False, nullable=False)
    projeto_id = Column("Projeto",Integer, ForeignKey('projetos.id'))

    projeto = relationship("Projeto", back_populates="tarefas")