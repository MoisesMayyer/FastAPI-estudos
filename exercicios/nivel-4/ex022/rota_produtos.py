from fastapi import APIRouter, HTTPException
from schemas import ProdutoCreate, ProdutoResponse, ProdutoUpdate

from database import carregar_json, salvar_json

rota_produtos = APIRouter(prefix="/produtos", tags=["produtos"])


def criar_id(lista_produto: list[dict]) -> int:
    maior_id = max(
        (produto["id"] for produto in lista_produto),
        default=0
    )

    return maior_id + 1


def buscar_produto(lista_produto: list[dict], id: int) -> dict | None:
    return next(
        (produto for produto in lista_produto if produto["id"] == id),
        None
    )


@rota_produtos.post("/", response_model=ProdutoResponse, status_code=201)
async def criar_produto(dados: ProdutoCreate):
    lista_produto = carregar_json()

    produto = ProdutoResponse(
        id=criar_id(lista_produto),
        nome=dados.nome,
        descricao=dados.descricao,
        preco=dados.preco,
        disponivel=dados.disponivel,
    )

    lista_produto.append(produto.model_dump())
    salvar_json(lista_produto)

    return produto


@rota_produtos.delete("/{id}", status_code=204)
async def deletar_produto(id: int):
    lista_produto = carregar_json()

    produto_deletar = buscar_produto(lista_produto, id)

    if produto_deletar is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    lista_produto.remove(produto_deletar)
    salvar_json(lista_produto)


@rota_produtos.put("/{id}", response_model=ProdutoResponse)
async def atualizar_produto(id: int, dados: ProdutoUpdate):
    lista_produto = carregar_json()

    produto_atualizar = buscar_produto(lista_produto, id)

    if produto_atualizar is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    dados_atualizados = {
        campo: valor
        for campo, valor in dados.model_dump(exclude_unset=True).items()
        if valor is not None or campo == "descricao"
    }

    produto_atualizar.update(dados_atualizados)
    salvar_json(lista_produto)

    return produto_atualizar


@rota_produtos.get("/", response_model=list[ProdutoResponse])
async def listar_produtos():
    lista_produto = carregar_json()
    return lista_produto


@rota_produtos.get("/{id}", response_model=ProdutoResponse)
async def listar_produto(id: int):
    lista_produto = carregar_json()

    produto_return = buscar_produto(lista_produto, id)

    if produto_return is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return produto_return
