from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))
    review_text = Column(String(100), nullable=False)
    score = Column(DECIMAL(10,2), nullable=False)

    order = relationship("Order", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

