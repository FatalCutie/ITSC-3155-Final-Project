from typing import Optional
from pydantic import BaseModel

class CouponBase(BaseModel):
    discount:int

class CouponCreate(CouponBase):
    pass

class CouponUpdate(BaseModel):
    discount: Optional[int] = None


class Coupon(CouponBase):
    discount: int

    class ConfigDict:
        from_attributes = True