from typing import Optional
from pydantic import BaseModel

class IngredientBase(BaseModel):
    name: str
    amount: int

class Ingredient(IngredientBase):
    pass