from datetime import timedelta, timezone, datetime
import jwt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models import Usuario
from schemas import UsuarioResponse, Token
from sqlalchemy.orm import Session
from depends import get_db, verificar_token
from security import pwd_context
from typing import Optional
from config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM

auth_router = APIRouter(prefix="/auth",tags=["auth"])

def criar_token(usuario_id:int, duracao_token: Optional[timedelta] = None):
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


@auth_router.post("/token", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    usuario = db.query(Usuario).filter(Usuario.email == form_data.username).first()

    if not usuario:
        raise HTTPException(status_code=401, detail="credenciais invalidas")

    if not usuario.ativo:
        raise HTTPException(status_code=401, detail="credenciais invalidas")

    if not pwd_context.verify(form_data.password, usuario.senha):
        raise HTTPException(status_code=401, detail="credenciais invalidas")

    token = criar_token(usuario.id)

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@auth_router.get("/", response_model=UsuarioResponse)
def get_user(usuario: Usuario = Depends(verificar_token)):
    return usuario