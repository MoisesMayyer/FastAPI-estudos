from fastapi import FastAPI
from database import Base, db
from routers.usuarios import user_router

app = FastAPI()
app.include_router(user_router)

Base.metadata.create_all(db)


@app.get("/")
async def root():
    return {"message": "Hello World"}