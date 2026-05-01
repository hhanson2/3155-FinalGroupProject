from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    id              = Column(Integer,     primary_key=True, index=True, autoincrement=True)
    customer_id     = Column(Integer,     ForeignKey("customers.id"), nullable=False)
    type            = Column(String(50),  nullable=False)
    expiry_date     = Column(String(7),   nullable=True)

    customer = relationship("Customer", back_populates="payment_methods")