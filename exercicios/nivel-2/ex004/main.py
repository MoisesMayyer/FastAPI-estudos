from fastapi import FastAPI
from database import Base, db
from alunos import rota_alunos
from planos import rota_planos
from matriculas import rota_matriculas

app = FastAPI()

app.include_router(rota_alunos)
app.include_router(rota_planos)
app.include_router(rota_matriculas)

Base.metadata.create_all(db)


@app.get("/")
def home():
    return {"message": "Hello World"}