from database import Session, db
from models import Base, Pessoa


Base.metadata.create_all(db)


def adicionar(nome: str, idade: int, nacionalidade: str) -> None:
    session = Session()

    pessoa = Pessoa(
        nome=nome,
        idade=idade,
        nacionalidade=nacionalidade
    )

    session.add(pessoa)
    session.commit()
    session.close()


def listar():
    session = Session()

    pessoas = session.query(Pessoa).all()

    for pessoa in pessoas:
        print(
            f"ID: {pessoa.id} | "
            f"Nome: {pessoa.nome} | "
            f"Idade: {pessoa.idade} | "
            f"Nacionalidade: {pessoa.nacionalidade}"
        )

    session.close()


def atualizar():
    session = Session()

    id = int(input("ID: "))
    pessoa = session.get(Pessoa, id)

    novo_nome = input("Nome: ")
    nova_idade = int(input("Idade: "))
    nova_nacionalidade = input("Nacionalidade: ")

    pessoa.nome = novo_nome
    pessoa.idade = nova_idade
    pessoa.nacionalidade = nova_nacionalidade

    session.commit()
    session.close()


def remover():
    session = Session()

    id = int(input("ID: "))
    pessoa = session.get(Pessoa, id)

    session.delete(pessoa)
    session.commit()
    session.close()


while True:
    escolha = int(
        input(
            "\n1 - Adicionar\n"
            "2 - Listar\n"
            "3 - Atualizar\n"
            "4 - Remover\n"
            "5 - Sair\n"
            "Escolha: "
        )
    )

    if escolha == 1:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        nacionalidade = input("Nacionalidade: ")

        adicionar(nome, idade, nacionalidade)

    elif escolha == 2:
        listar()

    elif escolha == 3:
        atualizar()

    elif escolha == 4:
        remover()

    elif escolha == 5:
        break

    else:
        print("Opção inválida.")