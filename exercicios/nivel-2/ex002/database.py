from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine('sqlite:///livraria.db')

Base = declarative_base()

Session = sessionmaker(bind=db)
