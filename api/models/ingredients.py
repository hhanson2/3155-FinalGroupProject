from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    id   = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    unit = Column(String(50),  nullable=False)

    recipes   = relationship("Recipe",   back_populates="ingredient")
    resources = relationship("Resource", back_populates="ingredient")