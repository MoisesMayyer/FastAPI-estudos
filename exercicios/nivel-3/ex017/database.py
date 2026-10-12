from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine('sqlite:///database.db')

SessionLocal = sessionmaker(bind=db)

Base = declarative_base()