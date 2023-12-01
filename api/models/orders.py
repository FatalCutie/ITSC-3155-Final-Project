from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))

    # Coupon foreign key referencing the id column in the coupons table
    coupon_id = Column(Integer, ForeignKey("coupon.id"))

    # establish relationships
    order_details = relationship("OrderDetail", back_populates="orders")
    coupon = relationship("Coupon", back_populates="orders")
