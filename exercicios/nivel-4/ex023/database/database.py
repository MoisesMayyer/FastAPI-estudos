from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import URL_DATABASE

db = create_engine(URL_DATABASE)

Base = declarative_base()

SessionLocal = sessionmaker(bind=db)
