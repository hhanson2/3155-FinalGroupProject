from typing import Optional
from pydantic import BaseModel
from .ingredients import IngredientCreate

class MenuItemsBase(BaseModel):
    name: str
    pass

class MenuItemsCreate(MenuItemsBase):
    description: str
    price: float
    calories: int
    food_category: str
    ingredients: list[IngredientCreate]



class MenuItemsUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    food_category: Optional[str] = None
    ingredients: Optional[list[IngredientCreate]] = None


class MenuItems(MenuItemsBase):
    id: int
    description: str
    price: float
    calories: int
    food_category: str
    ingredients: str

    class Config:
        from_attributes = True