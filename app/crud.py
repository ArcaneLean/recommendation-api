"""CRUD operations for database models."""

from sqlalchemy.orm import Session

from app import models, schemas


def create_user(db: Session, data: schemas.UserCreate) -> models.User:
    user = models.User(name=data.name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, user_id: int) -> models.User | None:
    return db.get(models.User, user_id)


def create_item(db: Session, data: schemas.ItemCreate) -> models.Item:
    item = models.Item(name=data.name, type=data.type)
    item.tags = [_get_or_create_tag(db, name) for name in data.tags]
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_item(db: Session, item_id: int) -> models.Item | None:
    return db.get(models.Item, item_id)


def create_interaction(db: Session, data: schemas.InteractionCreate) -> models.Interaction:
    interaction = models.Interaction(
        user_id=data.user_id,
        item_id=data.item_id,
        rating=data.rating,
    )
    db.add(interaction)
    db.commit()
    db.refresh(interaction)
    return interaction


def _get_or_create_tag(db: Session, name: str) -> models.Tag:
    tag = db.query(models.Tag).filter(models.Tag.name == name).first()
    if not tag:
        tag = models.Tag(name=name)
        db.add(tag)
        db.flush()
    return tag
