from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base


db = create_engine('sqlite:///banco.db')
Base = declarative_base()
Session = sessionmaker(bind=db)
session = Session()

class Numero(Base):
    __tablename__ = "numeros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    valor = Column("valor", Integer)


Base.metadata.create_all(db)


def adicionar_numero(valor):

    session.add(Numero(valor=valor))
    session.commit()


def listar_numeros():
    lista = session.query(Numero).all()

    for numero in lista:
        print(f"ID: {numero.id} | Valor: {numero.valor}")

while True:
    print("menu")

    opc =int(input("opções: adicionar[1] listar[2] sair[3]: "))

    if opc == 1:
        valor_adicionar = int(input("valor: "))
        adicionar_numero(valor_adicionar)

    elif opc == 2:
        listar_numeros()

    elif opc == 3:
        break

    else:
        print("opc invalida")
