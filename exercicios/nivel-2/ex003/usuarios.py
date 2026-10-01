from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from models import Usuario, Tarefa
from depends import get_db
from security import pwd_context

rota_usuario = APIRouter(prefix="/usuarios" , tags=["usuarios"])


@rota_usuario.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def adicionar_usuario(usuario_dados: UsuarioCreate, db: Session = Depends(get_db)):

    usuario_existente = db.query(Usuario).filter(Usuario.email == usuario_dados.email).first()

    if usuario_existente:
        raise HTTPException(status_code=400, detail="Usuario ja existe")

    if not usuario_dados.nome.strip():
        raise HTTPException(status_code=400, detail="nome não pode ser vazio")

    if not usuario_dados.senha or not usuario_dados.senha.strip():
        raise HTTPException(400, "senha não pode ser vazia")

    senha_criptografada = pwd_context.hash(usuario_dados.senha)
    usuario = Usuario(nome=usuario_dados.nome, email=usuario_dados.email, senha=senha_criptografada)

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario


@rota_usuario.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_usuario(id: int, db: Session = Depends(get_db)):
    usuario_existe = db.query(Usuario).filter(Usuario.id == id).first()

    if not usuario_existe:
        raise HTTPException(status_code=404, detail="usuario inexistente")

    usuario_tarefa = db.query(Tarefa).filter(Tarefa.usuario_id == id).first()

    if usuario_tarefa:
        raise HTTPException(status_code=400, detail="Usuario possui tarefa vinculada")

    db.delete(usuario_existe)
    db.commit()
    return None


@rota_usuario.put("/{id}", response_model=UsuarioResponse)
def atualizar_usuario(id: int, dados: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario = db.get(Usuario, id)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    if dados.nome is not None:
        if not dados.nome.strip():
            raise HTTPException(400, "nome não pode ser vazio")
        usuario.nome = dados.nome.strip()
    
    if dados.email is not None:
        if not dados.email.strip():
            raise HTTPException(400, "email não pode ser vazio")

        email_existe = db.query(Usuario).filter(Usuario.email == dados.email, Usuario.id != id).first()

        if email_existe:
            raise HTTPException(400, "email já cadastrado")
        usuario.email = dados.email.strip()
    
    if dados.senha is not None:
        if not dados.senha.strip():
            raise HTTPException(400, "senha não pode ser vazia")

        usuario.senha = pwd_context.hash(dados.senha.strip())

    db.commit()
    db.refresh(usuario)

    return usuario


@rota_usuario.get("/", response_model=list[UsuarioResponse])
def retornar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios


@rota_usuario.get("/{id}", response_model=UsuarioResponse)
def retornar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.get(Usuario, id)

    if not usuario:
        raise HTTPException(status_code=404, detail="usuario inexistente")

    return usuario