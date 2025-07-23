from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import uuid

class Franchise(Base):
    __tablename__ = "franchises"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)

    # Relationships
    restaurants = relationship("Restaurant", back_populates="franchise")
    clients = relationship("Client", back_populates="franchise")
    users = relationship("User", back_populates="franchise")
    categories = relationship("ProductCategory", back_populates="franchise")
    supp_categories = relationship("SupplementCategory", back_populates="franchise")
    ingredients = relationship("Ingredient", back_populates="franchise")
    products = relationship("Product", back_populates="franchise")