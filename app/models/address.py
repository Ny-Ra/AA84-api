from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    entry = Column(String, nullable=False)
    door_number = Column(String, nullable=False)
    infos = Column(String, nullable=False)
    name = Column(String, nullable=False)
    
    # Foreign key to Client
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)

    # Relationships
    client = relationship("Client", back_populates="addresses")