from fastapi import APIRouter, HTTPException, Depends, status

from schema import UsuarioCreate, UsuarioResponse, UsuarioUpdate

from depends import get_db

from model import Usuario

from sqlalchemy.orm import Session

from security import pwd_context

user_router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@user_router.post("/", response_model=UsuarioResponse)
async def adicionar_usuarios(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existe = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if usuario_existe:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    senha_hash = pwd_context.hash(usuario.senha)
    novo_usuario = Usuario(nome=usuario.nome, email=usuario.email, senha=senha_hash, ativo=True)

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


@user_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db.delete(usuario)
    db.commit()


@user_router.put("/{id}", response_model=UsuarioResponse)
async def atualizar_usuario(id: int, dados: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")


    if dados.nome is not None:
        usuario.nome = dados.nome
    if dados.email is not None:
        # Verifica se novo email já pertence a outro usuário
        email_existe = db.query(Usuario).filter(Usuario.email == dados.email, Usuario.id != id).first()
        if email_existe:
            raise HTTPException(status_code=400, detail="Email já cadastrado")
        usuario.email = dados.email
    if dados.senha is not None:
        usuario.senha = pwd_context.hash(dados.senha)
    if dados.ativo is not None:
        usuario.ativo = dados.ativo

    db.commit()
    db.refresh(usuario)
    return usuario


@user_router.get("/{id}", response_model=UsuarioResponse)
async def obter_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario


@user_router.get("/", response_model=list[UsuarioResponse])
async def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios