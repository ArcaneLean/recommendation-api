"""SQLAlchemy ORM models."""

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


item_tags = Table(
    "item_tags",
    Base.metadata,
    Column("item_id", Integer, ForeignKey("items.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


class User(Base):
    """Represents a user in the system."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    interactions: Mapped[list["Interaction"]] = relationship(back_populates="user")


class Tag(Base):
    """Represents a tag that can be applied to items (genre, creator, theme, etc.)."""

    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    items: Mapped[list["Item"]] = relationship(secondary=item_tags, back_populates="tags")


class Item(Base):
    """Represents a media item that can be recommended."""

    __tablename__ = "items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)  # movie, series, book, manga, comic

    tags: Mapped[list["Tag"]] = relationship(secondary=item_tags, back_populates="items")
    interactions: Mapped[list["Interaction"]] = relationship(back_populates="item")


class Interaction(Base):
    """Represents a user's interaction with an item."""

    __tablename__ = "interactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    item_id: Mapped[int] = mapped_column(Integer, ForeignKey("items.id"), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    user: Mapped["User"] = relationship(back_populates="interactions")
    item: Mapped["Item"] = relationship(back_populates="interactions")
