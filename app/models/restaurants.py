from sqlalchemy import Column, String, Boolean, ForeignKey, Table, Float, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import uuid

# Association table for Restaurant-OrderType many-to-many relationship
restaurant_order_type = Table(
    'restaurant_order_type',
    Base.metadata,
    Column('restaurant_id', UUID(as_uuid=True), ForeignKey('restaurants.id'), primary_key=True),
    Column('order_type_id', UUID(as_uuid=True), ForeignKey('order_types.id'), primary_key=True)
)

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    store_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, index=True)
    name = Column(String, nullable=False)
    pre_order = Column(Boolean, nullable=True)
    active = Column(Boolean, nullable=False)
    address = Column(String, nullable=False)
    postal = Column(String, nullable=False)
    state = Column(String, nullable=True)
    city = Column(String, nullable=False)
    
    # Foreign key to Franchise
    franchise_id = Column(UUID(as_uuid=True), ForeignKey('franchises.id'), nullable=False)

    # Relationships
    franchise = relationship("Franchise", back_populates="restaurants")
    delivery_zone = relationship("DeliveryZone", back_populates="restaurant", cascade="all, delete-orphan")
    status = relationship("ProductAvailability", back_populates="restaurant")
    hours = relationship("Hour", back_populates="restaurant")
    orders = relationship("Order", back_populates="restaurant")
    order_type = relationship("OrderType", secondary=restaurant_order_type, back_populates="restaurants")

class Hour(Base):
    __tablename__ = "hours"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    start = Column(String, nullable=False)
    end = Column(String, nullable=False)
    day = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    shift = Column(String, nullable=True)
    
    # Foreign key to Restaurant
    restaurant_id = Column(UUID(as_uuid=True), ForeignKey('restaurants.id'), nullable=False)

    # Relationships
    restaurant = relationship("Restaurant", back_populates="hours")

class DeliveryZone(Base):
    __tablename__ = "delivery_zones"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    zone_number = Column(String, nullable=False)
    color = Column(String, nullable=False)
    disabled = Column(Boolean, nullable=False)
    min_order = Column(Numeric(precision=10, scale=2), nullable=False)
    d_fee = Column(Numeric(precision=10, scale=2), nullable=False)
    
    # Foreign key to Restaurant
    restaurant_id = Column(UUID(as_uuid=True), ForeignKey('restaurants.id'), nullable=False)

    # Relationships
    points = relationship("DeliveryPoint", back_populates="zone", cascade="all, delete-orphan")
    restaurant = relationship("Restaurant", back_populates="delivery_zone")

class DeliveryPoint(Base):
    __tablename__ = "delivery_points"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    lat = Column(Float(precision=8), nullable=False)
    lng = Column(Float(precision=8), nullable=False)
    
    # Foreign key to DeliveryZone
    zone_id = Column(UUID(as_uuid=True), ForeignKey('delivery_zones.id', ondelete='CASCADE'), nullable=False)

    # Relationships
    zone = relationship("DeliveryZone", back_populates="points")