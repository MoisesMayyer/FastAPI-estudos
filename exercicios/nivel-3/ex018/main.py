from fastapi import FastAPI
from database import Base, db
from routers.usuarios import user_router
from routers.auth import auth_router
from routers.produtos import produto_router
app = FastAPI()
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(produto_router)

Base.metadata.create_all(db)


@app.get("/")
async def root():
    return {"message": "Hello World"}