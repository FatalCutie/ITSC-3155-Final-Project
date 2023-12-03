from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource
from .sandwiches import Sandwich


class RecipeBase(BaseModel):
    amount: int


class RecipeCreate(RecipeBase):
    sandwich_id: int
    resource_id: int
<<<<<<< HEAD
=======
    price: int
    #cheese: int
    #bread: int
    #tomato: int
>>>>>>> f43cbf5d924e16c9c6b542e75fa750e29124302c


class RecipeUpdate(BaseModel):
    sandwich_id: Optional[int] = None
    resource_id: Optional[int] = None
    amount: Optional[int] = None
    price: Optional[int] = None


class Recipe(RecipeBase):
    id: int
    sandwich: Sandwich = None
    resource: Resource = None

    class ConfigDict:
        from_attributes = True
