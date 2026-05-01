from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    description: Optional[str] = None


class OrderCreate(OrderBase):
    customer_id: int
    description: Optional[str] = None
    promotional_code:  Optional[str] = None
    pass


class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    description: Optional[str] = None
    promotion_code: Optional[str] = None



class Order(OrderBase):
    id: int
    customer_id: int
    description: str
    promotional_id: Optional[int] = None
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
