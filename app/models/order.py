from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.current_timestamp())
    order_number = Column(String, nullable=False, unique=True, index=True)
    status = Column(String, nullable=True)
    total_price = Column(Float, nullable=False)
    discount_type = Column(String, nullable=True)
    discount_order = Column(Float, nullable=True)
    comment = Column(String, nullable=True)
    
    # Foreign keys
    paiement_id = Column(Integer, ForeignKey('paiements.id'), nullable=True)
    order_type_id = Column(Integer, ForeignKey('order_types.id'), nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)

    # Relationships
    paiement = relationship("Paiement", back_populates="orders")
    order_type = relationship("OrderType", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    client = relationship("Client", back_populates="orders")
    restaurant = relationship("Restaurant", back_populates="orders")