from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    
    # Foreign key to Franchise
    franchise_id = Column(UUID(as_uuid=True), ForeignKey('franchises.franchise_id'), nullable=False)

    # Relationships
    franchise = relationship("Franchise", back_populates="users")