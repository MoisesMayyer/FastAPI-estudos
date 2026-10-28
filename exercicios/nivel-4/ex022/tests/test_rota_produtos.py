import sys
from pathlib import Path

import pytest
from starlette.testclient import TestClient

# Deixa os arquivos da ex022 importáveis (main, rota_produtos, schemas, database)
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def arquivo_isolado(tmp_path, monkeypatch):
    """Cada teste roda em uma pasta vazia, com seu próprio produtos.json."""
    monkeypatch.chdir(tmp_path)


@pytest.fixture
def dados_produto():
    return {
        "nome": "string",
        "descricao": "string",
        "preco": 1.0,
        "disponivel": True,
    }


@pytest.fixture
def produto_criado(dados_produto):
    resposta = client.post("/produtos/", json=dados_produto)
    assert resposta.status_code == 201
    return resposta.json()


@pytest.fixture
def produtos_criados():
    dados = [
        {"nome": "Caneta", "descricao": "azul", "preco": 2.5, "disponivel": True},
        {"nome": "Caderno", "descricao": None, "preco": 19.9, "disponivel": False},
    ]

    produtos = []
    for produto in dados:
        resposta = client.post("/produtos/", json=produto)
        assert resposta.status_code == 201
        produtos.append(resposta.json())

    return produtos


def test_json(produto_criado):
    resposta = client.get(f"/produtos/{produto_criado['id']}")

    assert resposta.status_code == 200
    assert resposta.json() == {
        "nome": "string",
        "descricao": "string",
        "preco": 1.0,
        "disponivel": True,
        "id": produto_criado["id"],
    }


def test_listar_produtos(produtos_criados):
    resposta = client.get("/produtos/")

    assert resposta.status_code == 200
    assert resposta.json() == produtos_criados


def test_listar_produtos_vazio():
    resposta = client.get("/produtos/")

    assert resposta.status_code == 200
    assert resposta.json() == []


def test_listar_produto(produto_criado):
    resposta = client.get(f"/produtos/{produto_criado['id']}")

    assert resposta.status_code == 200
    assert resposta.json() == produto_criado


@pytest.mark.parametrize("produto_id", [0, 99999])
def test_listar_produto_inexistente(produto_criado, produto_id):
    resposta = client.get(f"/produtos/{produto_id}")

    assert resposta.status_code == 404
    assert resposta.json() == {
        "detail": "Produto não encontrado"
    }



def test_criar_produto():
    resposta = client.post(
        "/produtos/",
        json={"nome": "Lápis", "preco": 1.5},
    )

    assert resposta.status_code == 201
    assert resposta.json() == {
        "nome": "Lápis",
        "descricao": None,
        "preco": 1.5,
        "disponivel": True,
        "id": 1,
    }


@pytest.mark.parametrize(
    "dados",
    [
        {"preco": 10.0},
        {"nome": "", "preco": 10.0},
        {"nome": "Caneta", "preco": 0},
        {"nome": "Caneta", "preco": -5.0},
        {"nome": "Caneta", "preco": "abc"},
    ],
)
def test_criar_produto_dados_invalidos(dados):
    resposta = client.post("/produtos/", json=dados)

    assert resposta.status_code == 422


def test_criar_produto_gera_ids_diferentes(produto_criado):
    resposta = client.post(
        "/produtos/",
        json={"nome": "Borracha", "preco": 0.5},
    )

    assert resposta.status_code == 201
    assert resposta.json()["id"] != produto_criado["id"]


def test_atualizar_produto(produto_criado):
    resposta = client.put(
        f"/produtos/{produto_criado['id']}",
        json={"preco": 9.99},
    )

    assert resposta.status_code == 200
    assert resposta.json() == {
        "nome": "string",
        "descricao": "string",
        "preco": 9.99,
        "disponivel": True,
        "id": produto_criado["id"],
    }

    resposta_get = client.get(f"/produtos/{produto_criado['id']}")
    assert resposta_get.json() == resposta.json()


def test_atualizar_produto_inexistente():
    resposta = client.put("/produtos/99999", json={"preco": 9.99})

    assert resposta.status_code == 404
    assert resposta.json() == {
        "detail": "Produto não encontrado"
    }


@pytest.mark.parametrize(
    "dados",
    [
        {"preco": 0},
        {"preco": -1.0},
        {"nome": ""},
    ],
)
def test_atualizar_produto_dados_invalidos(produto_criado, dados):
    resposta = client.put(f"/produtos/{produto_criado['id']}", json=dados)

    assert resposta.status_code == 422


def test_deletar_produto(produto_criado):
    resposta = client.delete(f"/produtos/{produto_criado['id']}")

    assert resposta.status_code == 204

    assert client.get(f"/produtos/{produto_criado['id']}").status_code == 404
    assert client.get("/produtos/").json() == []


def test_deletar_produto_inexistente():
    resposta = client.delete("/produtos/99999")

    assert resposta.status_code == 404
    assert resposta.json() == {
        "detail": "Produto não encontrado"
    }
