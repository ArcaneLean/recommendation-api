"""Main entry point for the Recommendation API."""

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, services
from app.db import Base, engine, get_db
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


@app.post("/users", response_model=schemas.UserResponse, status_code=201)
def create_user(data: schemas.UserCreate, db: Session = Depends(get_db)) -> User:
    return crud.create_user(db, data)


@app.post("/items", response_model=schemas.ItemResponse, status_code=201)
def create_item(data: schemas.ItemCreate, db: Session = Depends(get_db)) -> Item:
    return crud.create_item(db, data)


@app.post("/interactions", response_model=schemas.InteractionResponse, status_code=201)
def create_interaction(data: schemas.InteractionCreate, db: Session = Depends(get_db)) -> Interaction:
    if not crud.get_user(db, data.user_id):
        raise HTTPException(status_code=404, detail="User not found")
    if not crud.get_item(db, data.item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return crud.create_interaction(db, data)


@app.get("/recommendations/{user_id}", response_model=list[schemas.ItemResponse])
def get_recommendations(user_id: int, db: Session = Depends(get_db)) -> list[Item]:
    if not crud.get_user(db, user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return services.get_recommendations(db, user_id)
