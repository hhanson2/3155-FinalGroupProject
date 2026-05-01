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
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    food_category: Optional[str] = None


class MenuItems(MenuItemsBase):
    id: int
    description: str
    price: float
    calories: int
    food_category: str

    class Config:
        from_attributes = True