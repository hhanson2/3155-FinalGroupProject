from typing import Optional
from pydantic import BaseModel

class PaymentMethodBase(BaseModel):
    customer_id: int
    type: str
    expiry_date: str
    card_number: str
    pass

class PaymentMethodCreate(PaymentMethodBase):
    pass


class PaymentMethodUpdate(BaseModel):
    customer_id: Optional[int] = None
    type: Optional[str] = None
    expiry_date: Optional[str] = None
    card_number: Optional[str] = None


class PaymentMethod(PaymentMethodBase):
    pass

    class Config:
        from_attributes = True