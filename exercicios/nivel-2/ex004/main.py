from fastapi import FastAPI
from database import Base, db
from alunos import rota_alunos

app = FastAPI()

app.include_router(rota_alunos)
#app.include_router()
#app.include_router()

Base.metadata.create_all(db)


@app.get("/")
def home():
    return {"message": "Hello World"}