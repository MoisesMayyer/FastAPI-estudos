from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///database.db")

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db)