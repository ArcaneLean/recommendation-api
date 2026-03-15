"""Unit tests for recommendation service."""

from sqlalchemy.orm import Session

from app.models import Interaction, Item, User
from app.services import get_recommendations


def test_recommends_items_with_shared_tags(db: Session, user: User, items: list[Item]) -> None:
    matrix, neuromancer, akira, _ = items
    db.add(Interaction(user_id=user.id, item_id=matrix.id, rating=5.0))
    db.commit()

    results = get_recommendations(db, user.id)

    result_ids = [r.id for r in results]
    assert neuromancer.id in result_ids
    assert akira.id in result_ids


def test_excludes_already_interacted_items(db: Session, user: User, items: list[Item]) -> None:
    matrix, *_ = items
    db.add(Interaction(user_id=user.id, item_id=matrix.id, rating=5.0))
    db.commit()

    results = get_recommendations(db, user.id)

    assert matrix.id not in [r.id for r in results]


def test_excludes_items_with_no_shared_tags(db: Session, user: User, items: list[Item]) -> None:
    matrix, _, _, nineteen_eighty_four = items
    db.add(Interaction(user_id=user.id, item_id=matrix.id, rating=5.0))
    db.commit()

    results = get_recommendations(db, user.id)

    assert nineteen_eighty_four.id not in [r.id for r in results]


def test_returns_empty_when_no_interactions(db: Session, user: User, items: list[Item]) -> None:
    results = get_recommendations(db, user.id)
    assert results == []


def test_sorted_by_shared_tag_count(db: Session, user: User, items: list[Item]) -> None:
    matrix, neuromancer, akira, nineteen_eighty_four = items
    # User rated both sci-fi+cyberpunk items — Neuromancer and Akira both share 2 tags
    # Add a new item with only 1 shared tag to verify ordering
    from app.models import Tag
    sci_fi_tag = db.query(Tag).filter(Tag.name == "sci-fi").first()
    low_overlap = Item(name="Low Overlap", type="series", tags=[sci_fi_tag])
    db.add(low_overlap)
    db.flush()

    db.add(Interaction(user_id=user.id, item_id=matrix.id, rating=5.0))
    db.commit()

    results = get_recommendations(db, user.id)

    # neuromancer and akira share 2 tags; low_overlap shares 1
    high_overlap_ids = {neuromancer.id, akira.id}
    assert results[0].id in high_overlap_ids
    assert results[1].id in high_overlap_ids
    assert results[-1].id == low_overlap.id
