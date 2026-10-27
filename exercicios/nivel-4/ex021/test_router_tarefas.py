from starlette.testclient import TestClient
import pytest
from main import app


client = TestClient(app)


def test_pegar_tarefas():
    resposta = client.get("/tarefas/")

    assert resposta.status_code == 200
    assert isinstance(resposta.json(), list)


def test_pegar_tarefa_inexistente():
    resposta = client.get("/tarefas/999999")

    assert resposta.status_code == 404
    assert resposta.json() == {
        "detail": "Tarefa não encontrada"
    }


def test_pegar_tarefa():
    resposta = client.get(f"/tarefas/{1}")

    if not resposta.json():
        assert resposta.json() == []

    assert resposta.status_code == 200


def test_json():
    resposta = client.get(f"/tarefas/{1}")

    assert resposta.json() == {
        "id": 1,
        "titulo": "teste",
        "descricao": "teste",
        "concluida": False,
    }


@pytest.mark.parametrize("dados", [
    {},  # sem nenhum campo
    {"titulo": "teste"},  # faltam campos
    {"titulo": 123, "descricao": "teste", "concluida": False},
    {"titulo": "teste", "descricao": "teste", "concluida": "errado"},
])
def test_criar_tarefa_dados_invalidos(dados):
    resposta = client.post("/tarefas/", json=dados)

    assert resposta.status_code == 422

