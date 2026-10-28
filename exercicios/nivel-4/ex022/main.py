from fastapi import FastAPI
from rota_produtos import rota_produtos

app = FastAPI()
app.include_router(rota_produtos)


@app.get("/")
def root():
    return {"message": "hello world"}
