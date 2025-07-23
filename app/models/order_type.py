from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class OrderType(Base):
    __tablename__ = "order_types"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)

    # Relationships
    orders = relationship("Order", back_populates="order_type")
    restaurants = relationship("Restaurant", secondary="restaurant_order_type", back_populates="order_type")