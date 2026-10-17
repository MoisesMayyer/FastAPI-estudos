from fastapi import FastAPI
from routers.usuario import user_router
from database import Base, db

app = FastAPI()
app.include_router(user_router)


Base.metadata.create_all(db)

@app.get("/")
async def root():
    return {
        "message": "ola mundo!"
    }
