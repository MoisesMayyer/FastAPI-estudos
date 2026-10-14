from fastapi import APIRouter, Depends, HTTPException, status
from schemas import ProdutoResponse, ProdutoCreate, ProdutoUpdate
from models import Produto, Usuario
from depends import get_db, verificar_token
from sqlalchemy.orm import Session

produto_router = APIRouter(prefix="/produtos", tags=["produtos"])


@produto_router.get("/", response_model=list[ProdutoResponse])
async def listar_produtos(db: Session = Depends(get_db)):
    produtos = db.query(Produto).all()
    return produtos


@produto_router.get("/{id}", response_model=ProdutoResponse)
async def obter_produto(id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@produto_router.post("/", response_model=ProdutoResponse, status_code=status.HTTP_201_CREATED)
async def criar_produto(
    dados: ProdutoCreate,
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(verificar_token)
):
    novo_produto = Produto(
        nome=dados.nome,
        descricao=dados.descricao,
        preco=dados.preco,
        estoque=dados.estoque,
        ativo=dados.ativo if dados.ativo is not None else True,
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto


@produto_router.put("/{id}", response_model=ProdutoResponse)
async def atualizar_produto(
    id: int,
    dados: ProdutoUpdate,
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(verificar_token)
):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    if dados.nome is not None:
        produto.nome = dados.nome
    if dados.descricao is not None:
        produto.descricao = dados.descricao
    if dados.preco is not None:
        produto.preco = dados.preco
    if dados.estoque is not None:
        produto.estoque = dados.estoque
    if dados.ativo is not None:
        produto.ativo = dados.ativo

    db.commit()
    db.refresh(produto)
    return produto


@produto_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_produto(
    id: int,
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(verificar_token)
):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    db.delete(produto)
    db.commit()