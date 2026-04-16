from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class FoodCategory(Base):
    __tablename__ = "food_categories"

    id   = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    menu_items = relationship("MenuItem", back_populates="category")