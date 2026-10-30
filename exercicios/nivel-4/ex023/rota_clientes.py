from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from schemas import ClientCreate, ClienteResponse, ClienteUpdate

from database.depends import get_db
from database.model import Cliente

rota_clientes = APIRouter(prefix="/clientes", tags=["clientes"])


@rota_clientes.get("/", response_model=list[ClienteResponse])
async def pegar_clientes(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()

    return clientes


@rota_clientes.get("/{id}", response_model=ClienteResponse)
async def pegar_cliente(id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="cliente nao encontrado")

    return cliente


@rota_clientes.post("/", response_model=ClienteResponse)
async def criar_cliente(dados: ClientCreate, db: Session = Depends(get_db)):
    cliente_existe = db.query(Cliente).filter(Cliente.email == dados.email).first()

    if cliente_existe:
        raise HTTPException(status_code=400, detail="cliente ja cadastrado")

    novo_cliente = Cliente(
        nome=dados.nome,
        email=dados.email,
        telefone=dados.telefone
    )
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)

    return novo_cliente




@rota_clientes.put("/{id}")
async def editar_cliente(
    id: int,
    dados: ClienteUpdate,
    db: Session = Depends(get_db)
):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    if dados.nome is not None:
        cliente.nome = dados.nome

    if dados.email is not None:
        email_existe = db.query(Cliente).filter(
            Cliente.email == dados.email,
            Cliente.id != id
        ).first()

        if email_existe:
            raise HTTPException(status_code=409, detail="Email já cadastrado")

        cliente.email = dados.email

    if dados.telefone is not None:
        cliente.telefone = dados.telefone

    db.commit()
    db.refresh(cliente)

    return cliente


@rota_clientes.delete("/{id}")
async def deletar_cliente(id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="cliente nao encontrado")

    db.delete(cliente)
    db.commit()

    return None