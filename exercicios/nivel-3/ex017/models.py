
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column("Id",Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column("Nome",String, index=True)
    email = Column("Email",String, unique=True, index=True)
    senha = Column("Senha",String)
    ativo = Column("Ativo",Boolean, default=True, nullable=False)

    tarefas = relationship("Tarefa", back_populates="usuario")


class Tarefa(Base):
    __tablename__ = 'tarefas'

    id = Column("Id",Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column("Titulo",String, index=True, nullable=False)
    descricao = Column("Descricao",String)
    usuario_id = Column("UsuarioId",Integer, ForeignKey("usuarios.Id"))
    concluida = Column("Concluida", Boolean, default=False, nullable=False)

    usuario = relationship("Usuario", back_populates="tarefas")
