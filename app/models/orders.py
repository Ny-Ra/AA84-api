from sqlalchemy import Column, String, Float, ForeignKey, Numeric, Text
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import uuid
import enum

class OrderStatusEnum(enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PREPARING = "preparing"
    READY = "ready"
    OUT_FOR_DELIVERY = "out_for_delivery"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"

class Paiement(Base):
    __tablename__ = "paiements"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)

    # Relationships
    orders = relationship("Order", back_populates="paiement")

class OrderType(Base):
    __tablename__ = "order_types"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    type = Column(String, nullable=False)

    # Relationships
    orders = relationship("Order", back_populates="order_type")
    restaurants = relationship("Restaurant", secondary="restaurant_order_type", back_populates="order_type")

class Order(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.current_timestamp())
    order_number = Column(String, nullable=False, unique=True, index=True)
    status = Column(String, nullable=True)
    total_price = Column(Float, nullable=False)
    discount_type = Column(String, nullable=True)
    discount_order = Column(Float, nullable=True)
    comment = Column(String, nullable=True)
    
    # Foreign keys
    paiement_id = Column(UUID(as_uuid=True), ForeignKey('paiements.id'), nullable=True)
    order_type_id = Column(UUID(as_uuid=True), ForeignKey('order_types.id'), nullable=False)
    client_id = Column(UUID(as_uuid=True), ForeignKey('clients.id'), nullable=False)
    restaurant_id = Column(UUID(as_uuid=True), ForeignKey('restaurants.id'), nullable=False)

    # Relationships
    paiement = relationship("Paiement", back_populates="orders")
    order_type = relationship("OrderType", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    client = relationship("Client", back_populates="orders")
    restaurant = relationship("Restaurant", back_populates="orders")
    status_history = relationship("OrderStatusHistory", back_populates="order", cascade="all, delete-orphan")

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    quantity = Column(String, nullable=False)
    comment = Column(String, nullable=True)
    discount_type = Column(String, nullable=True)
    discount_price = Column(Numeric(precision=10, scale=2), nullable=True)
    
    # Foreign keys
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'), nullable=False)
    order_id = Column(UUID(as_uuid=True), ForeignKey('orders.id'), nullable=False)

    # Relationships
    product = relationship("Product", back_populates="order_item")
    order = relationship("Order", back_populates="items")
    extras = relationship("OrderItemExtra", back_populates="order_item", cascade="all, delete-orphan")

class OrderItemExtra(Base):
    __tablename__ = "order_item_extras"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    quantity = Column(String, nullable=False)
    
    # Foreign keys
    order_item_id = Column(UUID(as_uuid=True), ForeignKey('order_items.id'), nullable=False)
    supplement_id = Column(UUID(as_uuid=True), ForeignKey('supplements.id'), nullable=False)

    # Relationships
    order_item = relationship("OrderItem", back_populates="extras")
    supplement = relationship("Supplement", back_populates="extra")

class OrderStatusHistory(Base):
    __tablename__ = "order_status_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    status = Column(String, nullable=False)  # OrderStatusEnum values
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.current_timestamp())
    notes = Column(Text, nullable=True)
    
    # Foreign keys
    order_id = Column(UUID(as_uuid=True), ForeignKey('orders.id'), nullable=False)
    changed_by_user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=True)

    # Relationships
    order = relationship("Order", back_populates="status_history")
    changed_by = relationship("User")