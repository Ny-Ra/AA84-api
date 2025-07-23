from sqlalchemy import Column, String, ForeignKey, Text, Boolean, Numeric
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base
import uuid

class FranchiseSettings(Base):
    __tablename__ = "franchise_settings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    setting_key = Column(String, nullable=False)
    setting_value = Column(Text, nullable=True)
    setting_type = Column(String, nullable=False)  # 'string', 'number', 'boolean', 'json'
    description = Column(Text, nullable=True)
    is_system = Column(Boolean, default=False)  # System settings cannot be deleted
    
    # Foreign key to Franchise
    franchise_id = Column(UUID(as_uuid=True), ForeignKey('franchises.id'), nullable=False)

    # Relationships
    franchise = relationship("Franchise")

    # Constraints
    __table_args__ = (
        {'extend_existing': True},
    )

class RestaurantSettings(Base):
    __tablename__ = "restaurant_settings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    setting_key = Column(String, nullable=False)
    setting_value = Column(Text, nullable=True)
    setting_type = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    
    # Foreign key to Restaurant
    restaurant_id = Column(UUID(as_uuid=True), ForeignKey('restaurants.id'), nullable=False)

    # Relationships
    restaurant = relationship("Restaurant")

class TaxConfiguration(Base):
    __tablename__ = "tax_configurations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    tax_name = Column(String, nullable=False)
    tax_rate = Column(Numeric(precision=5, scale=4), nullable=False)  # 0.0825 for 8.25%
    is_active = Column(Boolean, default=True)
    applies_to_delivery = Column(Boolean, default=True)
    applies_to_takeout = Column(Boolean, default=True)
    applies_to_dine_in = Column(Boolean, default=True)
    
    # Foreign key to Franchise
    franchise_id = Column(UUID(as_uuid=True), ForeignKey('franchises.id'), nullable=False)

    # Relationships
    franchise = relationship("Franchise")