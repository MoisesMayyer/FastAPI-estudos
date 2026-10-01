from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


db= create_engine('sqlite:///ex003.db')

Base = declarative_base()

SessionLocal = sessionmaker(bind=db, autoflush=False, autocommit=False)