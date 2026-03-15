"""Business logic and recommendation services."""

from sqlalchemy.orm import Session

from app import models


def get_recommendations(db: Session, user_id: int) -> list[models.Item]:
    """Return items that share tags with items the user has interacted with, excluding already-seen items."""
    interactions = (
        db.query(models.Interaction)
        .filter(models.Interaction.user_id == user_id)
        .all()
    )

    interacted_item_ids = {i.item_id for i in interactions}

    interacted_items = (
        db.query(models.Item)
        .filter(models.Item.id.in_(interacted_item_ids))
        .all()
    )
    tag_ids = {tag.id for item in interacted_items for tag in item.tags}

    if not tag_ids:
        return []

    candidates = (
        db.query(models.Item)
        .filter(
            models.Item.tags.any(models.Tag.id.in_(tag_ids)),
            models.Item.id.notin_(interacted_item_ids),
        )
        .all()
    )

    return sorted(candidates, key=lambda item: len({t.id for t in item.tags} & tag_ids), reverse=True)
