"""Shared test fixtures."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.db import Base, get_db
from app.main import app
from app.models import Interaction, Item, Tag, User

SQLALCHEMY_TEST_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_TEST_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db(setup_db):
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture
def user(db: Session) -> User:
    u = User(name="Arcane")
    db.add(u)
    db.commit()
    db.refresh(u)
    return u


@pytest.fixture
def items(db: Session) -> list[Item]:
    sci_fi = Tag(name="sci-fi")
    cyberpunk = Tag(name="cyberpunk")
    dystopia = Tag(name="dystopia")
    db.add_all([sci_fi, cyberpunk, dystopia])
    db.flush()

    matrix = Item(name="The Matrix", type="movie", tags=[sci_fi, cyberpunk])
    neuromancer = Item(name="Neuromancer", type="book", tags=[sci_fi, cyberpunk])
    akira = Item(name="Akira", type="manga", tags=[sci_fi, cyberpunk])
    nineteen_eighty_four = Item(name="1984", type="book", tags=[dystopia])

    db.add_all([matrix, neuromancer, akira, nineteen_eighty_four])
    db.commit()
    return [matrix, neuromancer, akira, nineteen_eighty_four]
