from enum import Enum
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
# from .order_details import OrderDetail

class PaymentType(str, Enum):
    takeout = "cash"
    delivery = "card"

class PaymentBase(BaseModel):
    card_number: Optional[int] = None
    cvc: Optional[int] = None
    payment_type: PaymentType


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    card_number: Optional[int] = None
    cvc: Optional[int] = None
    payment_type: Optional[PaymentType] = None



class Payment(PaymentBase):
    card_number: Optional[int] = None
    cvc: Optional[int] = None
    payment_type: Optional[PaymentType] = None

    class ConfigDict:
        from_attributes = True
