from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(100))
    price = Column(DECIMAL)
    calories = Column(Integer)
    food_category = Column(String(100))

    order_details = relationship("OrderDetail", back_populates="menu_items")
    recipes = relationship("Recipe", back_populates="menu_item")