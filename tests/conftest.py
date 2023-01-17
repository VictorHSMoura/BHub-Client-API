"""
Pytest Fixture adapted from:
https://gist.github.com/kissgyorgy/e2365f25a213de44b9a2
"""

import pytest

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from db.sqlalchemy_db import Base, get_db_instance

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app import app

DATABASE_PATH = "sqlite:///test_database.db"


@pytest.fixture(scope="function")
def engine():
    """ Creates a mock engine for tests. """
    return create_engine("sqlite:///test_database.db",
                         connect_args={"check_same_thread": False})


@pytest.fixture(scope="function")
def fast_app(engine: Engine):
    """ Starts new engine for each test. """
    Base.metadata.create_all(engine)
    yield app
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")  # For DB tests.
def dbsession(engine: Engine, fast_app: FastAPI):
    """ Returns a new sqlAlchemy database session for each test. """
    connection = engine.connect()
    transaction = connection.begin()  # begin the nested transaction
    # use the connection with the already started transaction
    session = Session(bind=connection, autoflush=False, autocommit=False)

    yield session

    session.close()
    transaction.rollback()  # roll back the broader transaction
    connection.close()  # put back the connection to the connection pool


@pytest.fixture(scope="function")  # For API tests.
def client(engine: Engine, fast_app: FastAPI, dbsession: Session):
    """
    Returns a fastAPI TestClient that uses `dbsession` as database for tests.
    """

    def get_test_db():
        yield dbsession

    app.dependency_overrides[get_db_instance] = get_test_db
    with TestClient(fast_app) as client:
        yield client
