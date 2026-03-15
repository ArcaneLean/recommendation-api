"""Main entry point for the Recommendation API."""

from fastapi import FastAPI

from app.db import Base, engine
from app.models import Interaction, Item, User  # noqa: F401

app = FastAPI(title="Recommendation API")


@app.on_event("startup")
def create_tables() -> None:
    """Create all database tables on application startup."""
    Base.metadata.create_all(bind=engine)


@app.get("/")
def health_check() -> dict[str, str]:
    """Return a health status message."""
    return {"status": "ok"}
