from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Coupon(Base):
    __tablename__ = "coupon"

    discount = Column(Integer, index=True, nullable=False, server_default='0.0')

    # TODO: These models/schemas haven't been implemented yet, so this doesn't work yet
    # recipes = relationship("Recipe", back_populates="resource") #recipe where price is stored
