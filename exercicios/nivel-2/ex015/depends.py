from database import LocalSession


def get_db():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()