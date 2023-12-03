from enum import Enum
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .order_details import OrderDetail

class DeliveryType(str, Enum):
    takeout = "takeout"
    delivery = "delivery"

class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None
    delivery_type: Optional[DeliveryType] = None


# <<<<<<< HEAD
#
#
# =======
# >>>>>>> 9a4525fd0edb055a9279c872ec8bdf2ce2c29747
class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    delivery_type: Optional[DeliveryType] = None



class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: List[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
