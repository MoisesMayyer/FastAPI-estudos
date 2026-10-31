import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from config import TEST_URL_DATABASE
from database.database import Base
from database.depends import get_db
from main import app


engine_test = create_engine(TEST_URL_DATABASE, pool_pre_ping=True)


@pytest.fixture(scope="session", autouse=True)
def schema_teste():
    Base.metadata.drop_all(bind=engine_test)
    Base.metadata.create_all(bind=engine_test)
    yield
    Base.metadata.drop_all(bind=engine_test)


@pytest.fixture(scope="function")
def db_session():
    conexao = engine_test.connect()
    transacao = conexao.begin()
    session = Session(bind=conexao, join_transaction_mode="create_savepoint")
    try:
        yield session
    finally:
        session.close()
        transacao.rollback()
        conexao.close()


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
