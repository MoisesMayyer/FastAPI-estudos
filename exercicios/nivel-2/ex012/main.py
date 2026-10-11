from fastapi import FastAPI
from routers import rota_produtos
from database import Base, db

app = FastAPI()
app.include_router(rota_produtos)

Base.metadata.create_all(db)

@app.get("/")
def root():
    return {"message": "bem vindo"}
