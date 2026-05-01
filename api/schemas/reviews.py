from typing import Optional
from pydantic import BaseModel, ConfigDict


class ReviewBase(BaseModel):
    review_text: str
    score: float


class ReviewCreate(ReviewBase):
    customer_id: int
    order_id: int


class ReviewUpdate(BaseModel):
    review_text: Optional[str] = None
    score: Optional[float] = None
    customer_id: Optional[int] = None
    order_id: Optional[int] = None


class Review(ReviewBase):
    id: int
    customer_id: int
    order_id: int

    model_config = ConfigDict(from_attributes=True)