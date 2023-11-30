from typing import Optional
from pydantic import BaseModel


class CouponBase(BaseModel):
    discount: int
    code: int
    expiration_date: str


class CouponCreate(CouponBase):
    pass


class CouponUpdate(BaseModel):
    discount: Optional[int] = None
    code: Optional[int] = None
    expiration_date: Optional[str] = None


class Coupon(CouponBase):
    discount: int
    code: int
    expiration_date = str

    class ConfigDict:
        from_attributes = True