from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True, index=True)

    store_id = Column(
        Integer,
        ForeignKey("stores.id"),
        nullable=False,
    )

    name = Column(String, nullable=False)

    location = Column(String)

    capacity = Column(Float, nullable=False, default=0.0)

    utilization_rate = Column(Float, nullable=False, default=0.0)

    store = relationship("Store", back_populates="warehouses")
    shelves = relationship("Shelf", back_populates="warehouse")
    inventory_items = relationship("Inventory", back_populates="warehouse")
    purchase_orders = relationship("PurchaseOrder", back_populates="warehouse")
    sales = relationship("Sale", back_populates="warehouse")
