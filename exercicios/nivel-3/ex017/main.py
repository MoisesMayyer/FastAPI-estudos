from fastapi import FastAPI
from database import db, Base
from routers.usuarios import user_router
from routers.auth import auth_router
from routers.tarefas import tarefas_router

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(tarefas_router)

Base.metadata.create_all(bind=db)
@app.get("/")
async def root():
    return {"message": "Hello World"}
