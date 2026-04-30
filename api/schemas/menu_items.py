from typing import Optional
from pydantic import BaseModel

class MenuItemsBase(BaseModel):
    name: str
    pass

class MenuItemsCreate(MenuItemsBase):
    description: str
    price: float
    calories: int
    food_category: str


class MenuItemsUpdate(BaseModel):
    description: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    food_category: Optional[str] = None


class MenuItems(MenuItemsBase):
    description: str
    price: float
    calories: int
    food_category: str