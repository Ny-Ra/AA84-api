from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import uuid

# Association table for Restaurant-OrderType many-to-many relationship
restaurant_order_type = Table(
    'restaurant_order_type',
    Base.metadata,
    Column('restaurant_id', Integer, ForeignKey('restaurants.id'), primary_key=True),
    Column('order_type_id', Integer, ForeignKey('order_types.id'), primary_key=True)
)

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, index=True)
    name = Column(String, nullable=False)
    pre_order = Column(Boolean, nullable=True)
    active = Column(Boolean, nullable=False)
    address = Column(String, nullable=False)
    postal = Column(String, nullable=False)
    state = Column(String, nullable=True)
    city = Column(String, nullable=False)
    
    # Foreign key to Franchise
    franchise_id = Column(UUID(as_uuid=True), ForeignKey('franchises.franchise_id'), nullable=False)

    # Relationships
    franchise = relationship("Franchise", back_populates="restaurants")
    delivery_zone = relationship("DeliveryZone", back_populates="restaurant", cascade="all, delete-orphan")
    status = relationship("ProductAvailability", back_populates="restaurant")
    hours = relationship("Hour", back_populates="restaurant")
    orders = relationship("Order", back_populates="restaurant")
    order_type = relationship("OrderType", secondary=restaurant_order_type, back_populates="restaurants")