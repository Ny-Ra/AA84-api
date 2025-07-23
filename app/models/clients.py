from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
import uuid

class Client(Base):
    __tablename__ = "clients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.current_timestamp())
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    marketable = Column(Boolean, nullable=True)
    
    # Foreign key to Franchise
    franchise_id = Column(UUID(as_uuid=True), ForeignKey('franchises.id'), nullable=False)

    # Relationships
    franchise = relationship("Franchise", back_populates="clients")
    orders = relationship("Order", back_populates="client")
    addresses = relationship("Address", back_populates="client")

class Address(Base):
    __tablename__ = "addresses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    street = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    entry = Column(String, nullable=False)
    door_number = Column(String, nullable=False)
    infos = Column(String, nullable=False)
    name = Column(String, nullable=False)
    
    # Foreign key to Client
    client_id = Column(UUID(as_uuid=True), ForeignKey('clients.id'), nullable=False)

    # Relationships
    client = relationship("Client", back_populates="addresses")