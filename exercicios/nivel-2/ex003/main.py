from fastapi import FastAPI
from database import db, Base
from usuarios import rota_usuario

app= FastAPI()
app.include_router(rota_usuario)
#app.include_router()


Base.metadata.create_all(db)

@app.get("/")
def home():
    return {"message": "bem vindo"}