from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class ResourceBase(BaseModel):
    item: str
    pass

class ResourceCreate(ResourceBase):
   amount: int


class ResourceUpdate(BaseModel):
    item: Optional[str] = None
    amount: Optional[int] = None


class Resource(ResourceBase):
    id: int
    item: str
    amount: int

    model_config = ConfigDict(from_attributes=True)