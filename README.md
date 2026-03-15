# Recommendation API

A backend service that recommends media to users based on their past interactions.

Built to gain hands-on familiarity with Python, FastAPI, PostgreSQL, and SQLAlchemy — developed with [Claude Code](https://claude.ai/claude-code).

---

## Features

- Create users, items, and interactions via REST API
- Items have a type (`movie`, `series`, `book`, `manga`, `comic`) and multiple tags (genre, creator, theme, etc.)
- Recommendations are based on tag overlap with items the user has already rated, sorted by relevance
- Seeded with 16 real media items across all 5 types

## Stack

- **Python** + **FastAPI**
- **PostgreSQL** + **SQLAlchemy**
- **Pydantic** for request/response validation
- **pytest** for testing

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Health check |
| `POST` | `/users` | Create a user |
| `POST` | `/items` | Create an item with type and tags |
| `POST` | `/interactions` | Record a user rating an item (0–5) |
| `GET` | `/recommendations/{user_id}` | Get recommended items for a user |

## Running locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Make sure you have a PostgreSQL server running locally with a database and user created. Then create a `.env` file (see `.env.example`):
```
DATABASE_URL=postgresql://user:password@localhost/dbname
```

Start the API:
```bash
uvicorn app.main:app --reload
```

Seed the database:
```bash
python -m scripts.seed
```

## Running tests

```bash
pytest tests/ -v
```

Tests use an in-memory SQLite database — no PostgreSQL required.
