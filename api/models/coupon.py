from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Coupon(Base):
    __tablename__ = "coupon"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    discount = Column(DECIMAL(precision=5, scale=2), index=True, nullable=False, server_default='0.0')
    code = Column(String(20), unique=True, nullable=False)
    expiration_date = Column(DATETIME, nullable=True)


    # TODO: These models/schemas haven't been implemented yet, so this doesn't work yet
    recipes = relationship("Recipe", back_populates="coupon") #recipe where price is stored
    person = relationship("Person", back_populates="coupon")
    # establish relationships
    orders = relationship("orders", back_populates="coupon")
