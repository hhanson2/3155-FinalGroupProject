from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    description: Optional[str] = None


class OrderCreate(OrderBase):
    customer_id: int
    description: Optional[str] = None
    promotional_code:  Optional[str] = "None"
    order_type: Optional[str] = "dine-in"  # takeout, delivery, dine-in


class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    description: Optional[str] = None
    promotional_code: Optional[str] = None
    order_type: Optional[str] = None
    status: Optional[str] = None



class Order(OrderBase):
    id: int
    customer_id: int
    description: str
    promotion_id: Optional[int] = None
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None
    tracking_number: Optional[str] = None
    order_type: Optional[str] = None
    total_price: Optional[float] = None
    status: Optional[str] = None
    
    class ConfigDict:
        from_attributes = True
