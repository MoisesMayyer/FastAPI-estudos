from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


db = create_engine('sqlite:///academia.db')

Base = declarative_base()

LocalSession = sessionmaker(bind=db, autoflush=False, autocommit=False)

