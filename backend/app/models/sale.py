from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False,
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False,
    )

    warehouse_id = Column(
        Integer,
        ForeignKey("warehouses.id"),
    )

    quantity = Column(Integer, nullable=False)

    unit_price = Column(Float, nullable=False, default=0.0)

    total_amount = Column(Float, nullable=False, default=0.0)

    sold_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    customer = relationship("Customer", back_populates="sales")
    product = relationship("Product", back_populates="sales")
    warehouse = relationship("Warehouse", back_populates="sales")
