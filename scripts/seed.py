"""Populate the database with dummy users, items, and interactions."""

from app.db import SessionLocal
from app.models import Interaction, Item, Tag, User, item_tags

USERS = [
    "Arcane",
    "Blake",
    "Casey",
    "Dana",
]

# (name, type, tags)
ITEMS = [
    ("1984",                "book",   ["dystopia", "classic", "george-orwell", "political"]),
    ("Brave New World",     "book",   ["dystopia", "classic", "aldous-huxley", "philosophical"]),
    ("Dune",                "book",   ["sci-fi", "epic", "frank-herbert", "political"]),
    ("Foundation",          "book",   ["sci-fi", "classic", "isaac-asimov", "epic"]),
    ("Neuromancer",         "book",   ["sci-fi", "cyberpunk", "william-gibson"]),
    ("Watchmen",            "comic",  ["superhero", "alan-moore", "dystopia", "political"]),
    ("Akira",               "manga",  ["sci-fi", "cyberpunk", "action", "katsuhiro-otomo"]),
    ("Ghost in the Shell",  "manga",  ["sci-fi", "cyberpunk", "philosophical", "masamune-shirow"]),
    ("The Matrix",          "movie",  ["sci-fi", "cyberpunk", "action", "philosophical"]),
    ("Blade Runner",        "movie",  ["sci-fi", "cyberpunk", "noir", "ridley-scott"]),
    ("Inception",           "movie",  ["sci-fi", "thriller", "christopher-nolan", "philosophical"]),
    ("Interstellar",        "movie",  ["sci-fi", "epic", "christopher-nolan", "philosophical"]),
    ("Severance",           "series", ["dystopia", "thriller", "philosophical", "sci-fi"]),
    ("Dark",                "series", ["sci-fi", "thriller", "mystery", "philosophical"]),
    ("Attack on Titan",     "series", ["action", "dystopia", "epic", "political"]),
    ("Fullmetal Alchemist", "series", ["action", "epic", "philosophical", "fantasy"]),
]

# (user index, item index, rating)
INTERACTIONS = [
    # Arcane: into cyberpunk and sci-fi
    (0, 0, 5.0),   # 1984
    (0, 8, 4.5),   # The Matrix
    (0, 9, 4.0),   # Blade Runner

    # Blake: into philosophical sci-fi and thrillers
    (1, 10, 4.5),  # Inception
    (1, 11, 5.0),  # Interstellar
    (1, 13, 4.0),  # Dark

    # Casey: into dystopia and political themes
    (2, 0, 4.0),   # 1984
    (2, 1, 5.0),   # Brave New World
    (2, 5, 4.5),   # Watchmen

    # Dana: into action and epic stories
    (3, 14, 5.0),  # Attack on Titan
    (3, 15, 4.5),  # Fullmetal Alchemist
    (3, 2, 4.0),   # Dune
]


def seed() -> None:
    db = SessionLocal()
    try:
        db.query(Interaction).delete()
        db.execute(item_tags.delete())
        db.query(Item).delete()
        db.query(Tag).delete()
        db.query(User).delete()
        db.flush()

        users = [User(name=name) for name in USERS]
        db.add_all(users)
        db.flush()

        items = []
        for name, type_, tag_names in ITEMS:
            tags = []
            for tag_name in tag_names:
                tag = db.query(Tag).filter(Tag.name == tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name)
                    db.add(tag)
                    db.flush()
                tags.append(tag)
            item = Item(name=name, type=type_, tags=tags)
            db.add(item)
            items.append(item)
        db.flush()

        interactions = [
            Interaction(user_id=users[u].id, item_id=items[i].id, rating=rating)
            for u, i, rating in INTERACTIONS
        ]
        db.add_all(interactions)
        db.commit()

        print(f"Seeded {len(users)} users, {len(items)} items, {len(interactions)} interactions.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
