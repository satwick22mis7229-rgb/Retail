from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    sku = Column(String, unique=True, nullable=False)

    category = Column(String, nullable=False, default="general")

    price = Column(Float, nullable=False)

    cost_price = Column(Float, nullable=False)

    description = Column(Text)

    safety_stock = Column(Integer, nullable=False, default=0)

    reorder_point = Column(Integer, nullable=False, default=0)

    reorder_quantity = Column(Integer, nullable=False, default=0)

    is_active = Column(Boolean, nullable=False, default=True)

    preferred_supplier_id = Column(Integer, ForeignKey("suppliers.id"))

    preferred_supplier = relationship("Supplier", back_populates="products")
    inventory_items = relationship("Inventory", back_populates="product")
    shelves = relationship("Shelf", back_populates="product")
    sales = relationship("Sale", back_populates="product")
    forecasts = relationship("DemandForecast", back_populates="product")
    recommendations = relationship("Recommendation", back_populates="product")
    inventory_events = relationship("InventoryEvent", back_populates="product")
