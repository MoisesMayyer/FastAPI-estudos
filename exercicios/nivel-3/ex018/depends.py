from fastapi import Depends, HTTPException

from sqlalchemy.orm import Session

from config import SECRET_KEY, ALGORITHM
from database import SessionLocal
from security import oauth2_scheme
from models import Usuario
import jwt


def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def verificar_token(token: str = Depends(oauth2_scheme), session: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id = payload.get("sub")

        if usuario_id is None:
            raise HTTPException(status_code=401, detail="Acesso negado")

        try:
            usuario_id = int(usuario_id)
        except (ValueError, TypeError):
            raise HTTPException(status_code=401, detail="Acesso negado")

    except (jwt.InvalidTokenError, ValueError, TypeError):
        raise HTTPException(status_code=401, detail="Acesso negado")

    usuario = session.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not usuario:
        raise HTTPException(status_code=401, detail="Acesso negado")
    else:
        return usuario