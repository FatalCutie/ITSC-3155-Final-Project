from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rating = Column(Integer, nullable=False)
    reviewText = Column(String(300), unique=True, nullable=False)
    order_detail_id = Column(Integer, ForeignKey("order_details.id"), nullable=True)

    # establish relationships
    order_details = relationship("OrderDetail", back_populates="review")
