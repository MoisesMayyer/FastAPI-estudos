from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime, timedelta, timezone
from typing import Optional
from config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM
from jose import jwt
from schemas import Login, Token, UsuarioResponse
from dependencies import get_db, verificar_token
from sqlalchemy.orm import Session
from models import Usuario
from security import pwd_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])


def criar_token(usuario_id: int, duracao_token: Optional[timedelta] = None):
    if duracao_token is None:
        duracao_token = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))

    data_expiracao = datetime.now(timezone.utc) + duracao_token

    dict_info = {"sub": str(usuario_id), "exp": data_expiracao}

    if not SECRET_KEY:
        raise RuntimeError("SECRET_KEY não configurada")
    if not ALGORITHM:
        raise RuntimeError("ALGORITHM não configurado")

    token = jwt.encode(dict_info, SECRET_KEY, algorithm=ALGORITHM)

    return token


@auth_router.post("/login", response_model=Token)
async def login(dados: Login, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == dados.email).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="credenciais invalidas")

    if not usuario.ativo:
        raise HTTPException(status_code=401, detail="credenciais invalidas")

    if not pwd_context.verify(dados.senha, usuario.senha):
        raise HTTPException(status_code=401, detail="credenciais invalidas")

    token = criar_token(usuario.id)
    return {"access_token": token, "token_type": "bearer"}


@auth_router.get("/me", response_model=UsuarioResponse)
async def get_me(usuario: Usuario = Depends(verificar_token)):
    return usuario

