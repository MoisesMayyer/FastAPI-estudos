from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "sqlite:///./test.db"
db = create_engine(db_url)

Session = sessionmaker(bind=db)
