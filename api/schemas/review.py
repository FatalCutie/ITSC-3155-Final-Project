from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail


class ReviewBase(BaseModel):
    rating: Optional[int] = None
    reviewText: Optional[str] = None
    order_detail_id: Optional[int] = None


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    reviewText: Optional[str] = None
    order_detail_id: Optional[int] = None


class Review(ReviewBase):
    id: int
    order_detail: OrderDetail = None

    class ConfigDict:
        from_attributes = True
