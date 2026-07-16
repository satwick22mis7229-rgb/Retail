from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False,
    )

    warehouse_id = Column(
        Integer,
        ForeignKey("warehouses.id"),
        nullable=False,
    )

    shelf_id = Column(
        Integer,
        ForeignKey("shelves.id"),
    )

    quantity = Column(Integer, nullable=False, default=0)

    reserved_quantity = Column(Integer, nullable=False, default=0)

    reorder_threshold = Column(Integer, nullable=False, default=0)

    stockout_risk = Column(Float, nullable=False, default=0.0)

    status = Column(String, nullable=False, default="in_stock")

    product = relationship("Product", back_populates="inventory_items")
    warehouse = relationship("Warehouse", back_populates="inventory_items")
    shelf = relationship("Shelf", back_populates="inventory_items")
    events = relationship("InventoryEvent", back_populates="inventory")
