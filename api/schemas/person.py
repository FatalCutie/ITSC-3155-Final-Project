from typing import Optional
from pydantic import BaseModel

class PersonBase(BaseModel):
    name: str
    phone_number: int
    email_address: str
    id: int

class PersonCreate(PersonBase):
    pass

class PersonUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[int] = None
    email_address: Optional[str] = None
    id: Optional[int] = None #change id is in the class diagram. I think this will cause problems if used. Oh well!

class Person(PersonBase):
    id: int

    class ConfigDict:
        from_attributes = True