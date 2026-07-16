from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class InventoryEvent(Base):
    __tablename__ = "inventory_events"

    id = Column(Integer, primary_key=True, index=True)
    inventory_id = Column(Integer, ForeignKey("inventory.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    event_type = Column(String, nullable=False)
    quantity_change = Column(Integer, nullable=False)
    unit_cost = Column(Float, nullable=False, default=0.0)
    event_timestamp = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    reason = Column(String)

    inventory = relationship("Inventory", back_populates="events")
    product = relationship("Product", back_populates="inventory_events")
