import pytest
from database.model import Cliente


def test_criar_cliente(client):
    resposta = client.post("/clientes", json={
        "nome": "carlos",
        "email": "email@valido.com",
        "telefone": "+5511999999999"
    })

    assert resposta.status_code == 201
    assert resposta.json()["email"] == "email@valido.com"


def test_email_duplicado(client):
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


def test_buscar_cliente_inexistente(client):
    resposta = client.get(f"/clientes/{99999999}")

    assert resposta.status_code == 404
    assert resposta.json() == {"detail": "cliente nao encontrado"}


def test_buscar_cliente_existente(client, db_session):
    resp_criar = client.post("/clientes", json={
        "nome": "Maria",
        "email": "maria@email.com",
        "telefone": "+5511999999999"
    })
    assert resp_criar.status_code == 201
    cliente_id = resp_criar.json()["id"]

    resposta = client.get(f"/clientes/{cliente_id}")

    assert resposta.status_code == 200
    assert resposta.json()["nome"] == "Maria"
    assert resposta.json()["email"] == "maria@email.com"

    no_banco = db_session.query(Cliente).filter(Cliente.id == cliente_id).first()
    assert no_banco is not None
    assert no_banco.nome == "Maria"


def test_exluir_cliente_existente(client, db_session):
    resp_criar = client.post("/clientes", json={
        "nome": "ana",
        "email": "ana@email.com",
        "telefone": "+5511999999999"
    })
    assert resp_criar.status_code == 201
    cliente_id = resp_criar.json()["id"]

    resposta = client.delete(f"/clientes/{cliente_id}")

    assert resposta.status_code == 204
    assert resposta.content == b""

    no_banco = db_session.query(Cliente).filter(Cliente.id == cliente_id).first()
    assert no_banco is None


def test_exluir_cliente_inexistente(client):
    resposta = client.delete("/clientes/999999")

    assert resposta.status_code == 404
    assert resposta.json() == {"detail": "cliente nao encontrado"}


def test_atualizar_cliente(client, db_session):
    resp_criar = client.post("/clientes", json={
        "nome": "Maria",
        "email": "maria@email.com",
        "telefone": "+5511999999999"
    })
    assert resp_criar.status_code == 201
    cliente_id = resp_criar.json()["id"]

    resposta = client.put(f"/clientes/{cliente_id}", json={"nome": "Maria Silva"})

    assert resposta.status_code == 200
    assert resposta.json()["nome"] == "Maria Silva"
    assert resposta.json()["email"] == "maria@email.com"
    assert resposta.json()["telefone"] == "+5511999999999"

    no_banco = db_session.query(Cliente).filter(Cliente.id == cliente_id).first()
    assert no_banco.nome == "Maria Silva"


def test_atualizar_cliente_completo(client, db_session):
    resp_criar = client.post("/clientes", json={
        "nome": "Ana",
        "email": "ana@email.com",
        "telefone": "+5511999999999"
    })
    assert resp_criar.status_code == 201
    cliente_id = resp_criar.json()["id"]

    resposta = client.put(f"/clientes/{cliente_id}", json={
        "nome": "Ana Souza",
        "email": "ana.souza@email.com",
        "telefone": "+5511888888888"
    })

    assert resposta.status_code == 200
    assert resposta.json()["nome"] == "Ana Souza"
    assert resposta.json()["email"] == "ana.souza@email.com"
    assert resposta.json()["telefone"] == "+5511888888888"

    no_banco = db_session.query(Cliente).filter(Cliente.id == cliente_id).first()
    assert no_banco.email == "ana.souza@email.com"


def test_atualizar_cliente_inexistente(client):
    resposta = client.put("/clientes/999999", json={"nome": "Fantasma"})

    assert resposta.status_code == 404
    assert resposta.json() == {"detail": "cliente nao encontrado"}


def test_atualizar_email_duplicado(client):
    client.post("/clientes", json={
        "nome": "user1",
        "email": "user1@email.com",
        "telefone": "+5511999999999"
    })

    resp_criar = client.post("/clientes", json={
        "nome": "user2",
        "email": "user2@email.com",
        "telefone": "+5511999999999"
    })
    cliente_id = resp_criar.json()["id"]

    resposta = client.put(f"/clientes/{cliente_id}", json={"email": "user1@email.com"})

    assert resposta.status_code == 400
    assert resposta.json() == {"detail": "cliente ja cadastrado"}


def test_atualizar_telefone_invalido(client):
    resp_criar = client.post("/clientes", json={
        "nome": "Ana",
        "email": "ana@email.com",
        "telefone": "+5511999999999"
    })
    cliente_id = resp_criar.json()["id"]

    resposta = client.put(f"/clientes/{cliente_id}", json={"telefone": "123"})

    assert resposta.status_code == 422
