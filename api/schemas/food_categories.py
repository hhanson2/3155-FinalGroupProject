from typing import Optional
from pydantic import BaseModel


class FoodCategoryBase(BaseModel):
    name: str


class FoodCategoryCreate(FoodCategoryBase):
    pass


class FoodCategoryUpdate(BaseModel):
    name: Optional[str] = None


class FoodCategory(FoodCategoryBase):
    id: int

    class ConfigDict:
        from_attributes = True