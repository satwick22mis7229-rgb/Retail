from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class Shelf(Base):
    __tablename__ = "shelves"

    id = Column(Integer, primary_key=True, index=True)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"))
    code = Column(String, nullable=False)
    zone = Column(String, nullable=False, default="general")
    capacity = Column(Integer, nullable=False, default=0)

    warehouse = relationship("Warehouse", back_populates="shelves")
    product = relationship("Product", back_populates="shelves")
    inventory_items = relationship("Inventory", back_populates="shelf")
