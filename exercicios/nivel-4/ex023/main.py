from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.database import Base, db
from database.model import Cliente  # noqa: F401 — registra a tabela no metadata

from rota_clientes import rota_clientes


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=db)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(rota_clientes)


@app.get("/")
def root():
    return {
        "message": "helo world"
    }
