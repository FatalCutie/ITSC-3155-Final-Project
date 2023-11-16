from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class PersonBase(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    phone_number = Column(Integer)
    email_address = Column(String(200))

    # TODO: These models/schemas haven't been implemented yet, so this doesn't work yet
    # customers = relationship("Customer", back_populates="person")
    # managers = relationship("Manager", back_populates="manager")
    # staff = relationship("Staff", back_popoulates="staff")