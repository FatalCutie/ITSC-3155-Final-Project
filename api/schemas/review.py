from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ReviewBase(BaseModel):
    reviewText: str


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    reviewText: Optional[str] = None


class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True
