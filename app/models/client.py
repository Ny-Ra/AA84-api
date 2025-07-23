from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.current_timestamp())
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    marketable = Column(Boolean, nullable=True)
    
    # Foreign key to Franchise
    franchise_id = Column(UUID(as_uuid=True), ForeignKey('franchises.franchise_id'), nullable=False)

    # Relationships
    franchise = relationship("Franchise", back_populates="clients")
    orders = relationship("Order", back_populates="client")
    addresses = relationship("Address", back_populates="client")