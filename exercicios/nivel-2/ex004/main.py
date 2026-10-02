from fastapi import FastAPI
from database import Base, db

app = FastAPI()

Base.metadata.create_all(db)


@app.get("/")
def home():
    return {"message": "Hello World"}