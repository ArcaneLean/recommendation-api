"""Pydantic schemas for request and response validation."""

from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str


class UserResponse(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}


class ItemCreate(BaseModel):
    name: str
    category: str


class ItemResponse(BaseModel):
    id: int
    name: str
    category: str

    model_config = {"from_attributes": True}


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
