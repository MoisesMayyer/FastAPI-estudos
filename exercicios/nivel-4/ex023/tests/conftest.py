import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from config import TEST_URL_DATABASE
from database.database import Base
from database.depends import get_db
from main import app


engine_test = create_engine(TEST_URL_DATABASE, pool_pre_ping=True)
TestingSessionLocal = sessionmaker(bind=engine_test, autocommit=False, autoflush=False)


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine_test)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.rollback()
        session.close()


@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    test_client = TestClient(app)

    try:
        yield test_client
    finally:
        app.dependency_overrides.clear()


@pytest.fixture(scope="session", autouse=True)
def cleanup_database():
    yield
    Base.metadata.drop_all(bind=engine_test)