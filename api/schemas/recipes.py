from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .ingredients import Ingredient



class RecipeBase(BaseModel):
    menu_item_id: int
    instructions: str

class RecipeCreate(RecipeBase):
    ingredients: list[Ingredient]
    pass

class RecipeUpdate(BaseModel):
    menu_item_id: Optional[int] = None
    ingredients: Optional[list[Ingredient]] = None
    instructions: Optional[str] = None

class Recipe(RecipeBase):
    id: int
    ingredients: str
    pass
    class ConfigDict:
        from_attributes = True