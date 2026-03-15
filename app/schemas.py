"""Pydantic schemas for request and response validation."""

from pydantic import BaseModel, Field, field_validator


class UserCreate(BaseModel):
    name: str


class UserResponse(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}


class ItemCreate(BaseModel):
    name: str
    type: str
    tags: list[str] = []


class ItemResponse(BaseModel):
    id: int
    name: str
    type: str
    tags: list[str]

    model_config = {"from_attributes": True}

    @field_validator("tags", mode="before")
    @classmethod
    def extract_tag_names(cls, v: object) -> list[str]:
        if isinstance(v, list) and v and hasattr(v[0], "name"):
            return [tag.name for tag in v]
        return v  # type: ignore[return-value]


class InteractionCreate(BaseModel):
    user_id: int
    item_id: int
    rating: float = Field(..., ge=0.0, le=5.0)


class InteractionResponse(BaseModel):
    id: int
    user_id: int
    item_id: int
    rating: float

    model_config = {"from_attributes": True}
