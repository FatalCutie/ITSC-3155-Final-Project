from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class CouponBase(BaseModel):
    discount: int
    code: str
    expiration_date: Optional[datetime] = None


class CouponCreate(CouponBase):
    pass


class CouponUpdate(BaseModel):
    discount: Optional[int] = None
    code: Optional[int] = None
    expiration_date: Optional[str] = None


class Coupon(CouponBase):
    id: int

    class ConfigDict:
        from_attributes = True
