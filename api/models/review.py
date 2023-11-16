from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    reviewText = Column(String(300), unique=True, nullable=False)

    person = relationship("Person", back_populates="review")