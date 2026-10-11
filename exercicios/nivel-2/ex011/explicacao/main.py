"""
SQLAlchemy - Guia de Estudo Básico
Exemplos mínimos para entender o fluxo: Engine → Session → Model → CRUD
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


# ENGINE & SESSION
engine = create_engine('sqlite:///../test.db', echo=True)  # echo=True loga SQL
Session = sessionmaker(bind=engine)                        # Factory de sessões
session = Session()                                         # Sessão ativa (transação)
Base = declarative_base()                                   # Base para modelos ORM


# MODELO (tabela)
class Numero(Base):
    __tablename__ = "numeros"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)

Base.metadata.create_all(engine)  # Cria tabelas que não existem


# CREATE
n = Numero(nome="um")     # Instância (transient)
session.add(n)            # Adiciona à sessão (pending)
session.commit()          # Persiste no banco (persistent)
print(f"Criado: {n.id}, {n.nome}")


# READ
todos = session.query(Numero).all()              # Todos (lista)
for n in todos:                                   # Iterar resultados
    print(f"  id={n.id}, nome={n.nome}")

session.query(Numero).get(1)                      # Por PK (rápido)
session.query(Numero).filter_by(nome="um").first()  # Filtro simples
session.query(Numero).filter(Numero.nome == "um").first()  # Filtro avançado
session.query(Numero).order_by(Numero.id.desc()).limit(10).all()  # Ordena + pagina


# UPDATE
# Forma 1: Via objeto (recomendada para 1 registro)
obj = session.query(Numero).get(1)
if obj:
    obj.nome = "atualizado"
    session.commit()

# Forma 2: Via query (bulk - múltiplos registros)
session.query(Numero).filter(Numero.id == 1).update({"nome": "bulk"})
session.commit()


# DELETE
# Forma 1: Via objeto (recomendada para 1 registro)
obj = session.query(Numero).get(1)
if obj:
    session.delete(obj)
    session.commit()

# Forma 2: Via query (bulk - múltiplos registros)
session.query(Numero).filter(Numero.nome.like("teste%")).delete()
session.commit()


# ESTADOS DO OBJETO
# ──────────────────────────────────────────────────────────────
# Transient  → session.add() → Pending → commit() → Persistent
# Persistent → session.delete() → Deleted → commit() → (removido)
# Persistent → session.expunge() → Detached (fora da sessão)


# BOAS PRÁTICAS
# ──────────────────────────────────────────────────────────────
# session.commit()    # Salva
# session.rollback()  # Desfaz em erro
# session.close()     # Fecha conexão
# with Session() as s:  # Context manager (auto close/commit/rollback)

session.close()