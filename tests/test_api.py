"""API endpoint tests."""

from fastapi.testclient import TestClient

from app.models import Interaction, Item, Tag, User


def test_health_check(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# --- Users ---

def test_create_user(client: TestClient) -> None:
    response = client.post("/users", json={"name": "Arcane"})
    assert response.status_code == 201
    assert response.json()["name"] == "Arcane"


def test_create_user_returns_id(client: TestClient) -> None:
    response = client.post("/users", json={"name": "Arcane"})
    assert "id" in response.json()


# --- Items ---

def test_create_item(client: TestClient) -> None:
    response = client.post("/items", json={"name": "1984", "type": "book", "tags": ["dystopia", "classic"]})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "1984"
    assert data["type"] == "book"
    assert set(data["tags"]) == {"dystopia", "classic"}


def test_create_item_without_tags(client: TestClient) -> None:
    response = client.post("/items", json={"name": "1984", "type": "book"})
    assert response.status_code == 201
    assert response.json()["tags"] == []


# --- Interactions ---

def test_create_interaction(client: TestClient, user: User, items: list[Item]) -> None:
    matrix = items[0]
    response = client.post("/interactions", json={"user_id": user.id, "item_id": matrix.id, "rating": 4.5})
    assert response.status_code == 201
    data = response.json()
    assert data["user_id"] == user.id
    assert data["item_id"] == matrix.id
    assert data["rating"] == 4.5


def test_create_interaction_invalid_rating(client: TestClient, user: User, items: list[Item]) -> None:
    response = client.post("/interactions", json={"user_id": user.id, "item_id": items[0].id, "rating": 6.0})
    assert response.status_code == 422


def test_create_interaction_unknown_user(client: TestClient, items: list[Item]) -> None:
    response = client.post("/interactions", json={"user_id": 9999, "item_id": items[0].id, "rating": 3.0})
    assert response.status_code == 404


def test_create_interaction_unknown_item(client: TestClient, user: User) -> None:
    response = client.post("/interactions", json={"user_id": user.id, "item_id": 9999, "rating": 3.0})
    assert response.status_code == 404


# --- Recommendations ---

def test_recommendations_returns_items(client: TestClient, db, user: User, items: list[Item]) -> None:
    matrix = items[0]
    db.add(Interaction(user_id=user.id, item_id=matrix.id, rating=5.0))
    db.commit()

    response = client.get(f"/recommendations/{user.id}")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_recommendations_unknown_user(client: TestClient) -> None:
    response = client.get("/recommendations/9999")
    assert response.status_code == 404


def test_recommendations_excludes_interacted(client: TestClient, db, user: User, items: list[Item]) -> None:
    matrix = items[0]
    db.add(Interaction(user_id=user.id, item_id=matrix.id, rating=5.0))
    db.commit()

    response = client.get(f"/recommendations/{user.id}")
    result_ids = [item["id"] for item in response.json()]
    assert matrix.id not in result_ids
