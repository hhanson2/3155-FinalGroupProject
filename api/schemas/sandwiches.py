from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SandwichBase(BaseModel):
    sandwich_name: str
    pass


class SandwichCreate(SandwichBase):
    price: float


class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None


class Sandwich(SandwichBase):
    price: float
