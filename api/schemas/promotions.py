from typing import Optional
from datetime import date  # matches the Date column type in the model
from pydantic import BaseModel


class PromotionBase(BaseModel):
    code: str
    discount_percent: float  # allows decimals e.g. 10.5 for 10.5% off
    expiration_date: date


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    # everything optional since manager may only update one field at a time
    code: Optional[str] = None
    discount_percent: Optional[float] = None
    expiration_date: Optional[date] = None


class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True