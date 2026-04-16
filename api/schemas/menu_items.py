from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich

class MenuItemsBase(BaseModel):
    name: str