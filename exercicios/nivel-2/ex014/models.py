from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from database import Base


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    nome =  Column("nome",String, nullable=False)
    email = Column("email",String, unique=True, nullable=False)
    senha = Column("senha",String, nullable=False)


class Tarefa(Base):
    __tablename__ = 'tarefas'

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo",String, nullable=False)
    descricao = Column("descricao",String, nullable=True)
    usuario_id = Column("usuario_id",Integer, ForeignKey('usuarios.id'), nullable=False)
    concluida = Column("concluida",Boolean, nullable=False, default=False)