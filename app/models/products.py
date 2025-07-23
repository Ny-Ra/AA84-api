from sqlalchemy import Column, String, Boolean, ForeignKey, Text, Numeric, CheckConstraint, Index, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import uuid

# Association table for Ingredient-Product many-to-many relationship
ingredient_product = Table(
    'ingredient_product',
    Base.metadata,
    Column('ingredient_id', UUID(as_uuid=True), ForeignKey('ingredients.id'), primary_key=True),
    Column('product_id', UUID(as_uuid=True), ForeignKey('products.id'), primary_key=True)
)

class ProductCategory(Base):
    __tablename__ = "product_categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    
    # Self-referencing foreign key for parent category
    parent_category_id = Column(UUID(as_uuid=True), ForeignKey('product_categories.id'), nullable=True)
    
    # Foreign key to Franchise
    franchise_id = Column(UUID(as_uuid=True), ForeignKey('franchises.id'), nullable=False)

    # Relationships
    parent_category = relationship("ProductCategory", remote_side=[id], back_populates="child_categories")
    child_categories = relationship("ProductCategory", back_populates="parent_category")
    franchise = relationship("Franchise", back_populates="categories")
    products = relationship("Product", back_populates="category")

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    
    # Foreign key to Franchise
    franchise_id = Column(UUID(as_uuid=True), ForeignKey('franchises.id'), nullable=False)

    # Relationships
    franchise = relationship("Franchise", back_populates="ingredients")
    products = relationship("Product", secondary=ingredient_product, back_populates="ingredients")

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    vat = Column(String, nullable=True)
    image = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    additionnal_sale = Column(Boolean, nullable=True, default=False)
    
    # Foreign keys
    category_id = Column(UUID(as_uuid=True), ForeignKey('product_categories.id'), nullable=False)
    franchise_id = Column(UUID(as_uuid=True), ForeignKey('franchises.id'), nullable=False)

    # Relationships
    category = relationship("ProductCategory", back_populates="products")
    ingredients = relationship("Ingredient", secondary=ingredient_product, back_populates="products")
    status = relationship("ProductAvailability", back_populates="product", cascade="all, delete-orphan")
    supplement_product = relationship("SupplementProduct", back_populates="product", cascade="all, delete-orphan")
    franchise = relationship("Franchise", back_populates="products")
    order_item = relationship("OrderItem", back_populates="product")

    # Constraints
    __table_args__ = (
        CheckConstraint('price > 0', name='positive_price'),
        Index('idx_product_franchise_category', 'franchise_id', 'category_id'),
        Index('idx_product_name_franchise', 'franchise_id', 'name'),
    )

class SupplementCategory(Base):
    __tablename__ = "supplement_categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    
    # Foreign key to Franchise
    franchise_id = Column(UUID(as_uuid=True), ForeignKey('franchises.id'), nullable=False)

    # Relationships
    franchise = relationship("Franchise", back_populates="supp_categories")
    supplements = relationship("Supplement", back_populates="category")
    supplement_product = relationship("SupplementProduct", back_populates="category")

class Supplement(Base):
    __tablename__ = "supplements"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    image = Column(String, nullable=True)
    
    # Foreign key to SupplementCategory
    category_id = Column(UUID(as_uuid=True), ForeignKey('supplement_categories.id'), nullable=False)

    # Relationships
    category = relationship("SupplementCategory", back_populates="supplements")
    extra = relationship("OrderItemExtra", back_populates="supplement")

class SupplementProduct(Base):
    __tablename__ = "supplement_products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    number_free = Column(String, nullable=True)
    min = Column(String, nullable=True)
    max = Column(String, nullable=True)
    
    # Foreign keys
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey('supplement_categories.id'), nullable=False)

    # Relationships
    product = relationship("Product", back_populates="supplement_product")
    category = relationship("SupplementCategory", back_populates="supplement_product")

class ProductAvailability(Base):
    __tablename__ = "product_availabilities"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    availability = Column(Boolean, nullable=False, default=True)
    
    # Foreign keys
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
    restaurant_id = Column(UUID(as_uuid=True), ForeignKey('restaurants.id'), nullable=False)

    # Relationships
    product = relationship("Product", back_populates="status")
    restaurant = relationship("Restaurant", back_populates="status")