from fastapi import FastAPI
from database import Base, db
from livros_rotas import rota_livros
from autores_rotas import rota_autores


app = FastAPI()
app.include_router(rota_livros)
app.include_router(rota_autores)

Base.metadata.create_all(db)


@app.get("/")
def root():
    return {"message": "bem vindo a biblioteca"}