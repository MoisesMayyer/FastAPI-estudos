from fastapi import FastAPI
from database import db, Base

app = FastAPI()


Base.metadata.create_all(bind=db)
@app.get("/")
async def root():
    return {"message": "Hello World"}
