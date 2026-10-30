from fastapi import FastAPI
from database.database import Base, db
from database.model import Cliente


Base.metadata.create_all(bind=db)

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "helo world"
    }


print(Base.metadata.tables.keys())