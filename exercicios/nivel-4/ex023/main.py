from fastapi import FastAPI

from database.database import Base, db
from database.model import Cliente

from rota_clientes import rota_clientes

Base.metadata.create_all(bind=db)

app = FastAPI()
app.include_router(rota_clientes)


@app.get("/")
def root():
    return {
        "message": "helo world"
    }


print(Base.metadata.tables.keys())