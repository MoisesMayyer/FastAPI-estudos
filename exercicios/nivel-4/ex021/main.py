from fastapi import FastAPI

from database import salvar_json
from router_tarefas import tarefa_router
app = FastAPI()
app.include_router(tarefa_router)


@app.get("/")
def root():
    return {"message": "Hello World"}