from fastapi import APIRouter,Depends, HTTPException

from models import Usuario
from schema import AuthLogin

from depends import get_db

from sqlalchemy.orm import Session

from security import pwd_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/login")
async def login(dados: AuthLogin, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == dados.email).first()

    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="E-mail ou senha incorretos"
        )

    if not usuario.ativo:
        raise HTTPException(
            status_code=401,
            detail="E-mail ou senha incorretos"
        )

    if not pwd_context.verify(dados.senha, usuario.senha):
        raise HTTPException(
            status_code=401,
            detail="E-mail ou senha incorretos"
        )

    return {
        "message": "Login bem-sucedido",
        "usuario": {"id": usuario.id, "nome": usuario.nome, "email": usuario.email, "ativo": usuario.ativo}
    }