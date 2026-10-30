import pytest


@pytest.mark.parametrize("nome, email, telefone", [
    ("carlos", "email@valido.com", "+5511999999999")
])
def test_criar_cliente(client, db_session, nome, email, telefone):

    resposta = client.post("/clientes", json={
        "nome": nome,
        "email": email,
        "telefone": telefone
        }
    )

    assert resposta.status_code == 201
    assert resposta.json()["email"] == email


def test_email_duplicado(client, db_session):
    dados = {"nome": "user1", "email": "user1@email.com", "telefone": "+5511999999999"}

    client.post("/clientes", json=dados)

    resposta = client.post("/clientes", json={**dados, "nome": "user2"})

    assert resposta.status_code == 400


@pytest.mark.parametrize("nome,email,telefone", [
    ("",           "ana@email.com", "+5511999999999"),
    ("Ana",        "email-invalido", "+5511999999999"),
    ("Ana",        "ana@email.com", "123"),
    ("Ana",        "ana@email.com", ""),
    ("Ab",         "ana@email.com", "+5511999999999"),
])
def test_criar_cliente_invalido(client, nome, email, telefone):
    resposta = client.post("/clientes", json={
        "nome": nome,
        "email": email,
        "telefone": telefone
    })
    assert resposta.status_code == 422


def test_listar_clientes(client):
    resposta = client.get("/clientes")
    assert resposta.status_code == 200
    assert isinstance(resposta.json(), list)


def test_listar_cliente(client):
    resposta = client.get(f"/clientes/{99999999}")
    assert resposta.status_code == 404
    assert resposta.json() == {"detail": "cliente nao encontrado"}


def test_buscar_cliente_existente(client, db_session):
    from database.model import Cliente

    resp_criar = client.post("/clientes", json={
        "nome": "Maria",
        "email": "maria@email.com",
        "telefone": "+5511999999999"
    })
    assert resp_criar.status_code == 201
    cliente_id = resp_criar.json()["id"]

    resp_busca = client.get(f"/clientes/{cliente_id}")
    assert resp_busca.status_code == 200
    assert resp_busca.json()["nome"] == "Maria"
    assert resp_busca.json()["email"] == "maria@email.com"

    no_banco = db_session.query(Cliente).filter(Cliente.id == cliente_id).first()
    assert no_banco is not None
    assert no_banco.nome == "Maria"