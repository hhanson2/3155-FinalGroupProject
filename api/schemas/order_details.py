from pydantic import BaseModel, ConfigDict
from typing import Optional
from .menu_items import MenuItems

class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    menu_item_id: int

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    amount: Optional[int] = None
    menu_item_id: Optional[int] = None

class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    menu_item_id: int
    menu_items: Optional[MenuItems] = None

    model_config = ConfigDict(from_attributes=True)