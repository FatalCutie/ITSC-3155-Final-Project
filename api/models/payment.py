from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payment"

    #card_number: Optional[int] = None
    #cvc: Optional[int] = None
    #payment_type: PaymentType

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    card_number = Column(Integer, nullable=False)
    payment_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    cvc = Column(Integer, nullable=False)

    # establish relationships
    # orders = relationship("Orders", back_populates="payment") #untagging will probably break everything. Oh well!

