from typing import Optional
from pydantic import BaseModel

class PersonBase(BaseModel):
    name: str
    phone_number: int
    email_address: str

class PersonCreate(PersonBase):
    pass

class PersonUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[int] = None
    email_address: Optional[str] = None

class Person(PersonBase):
    id: int

    class ConfigDict:
        from_attributes = True