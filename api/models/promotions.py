from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id               = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code             = Column(String(50), nullable=False)
    discount_percent = Column(Float, nullable=False)
    expiration_date  = Column(Date, nullable=False)

    orders = relationship("Order", back_populates="promotion")