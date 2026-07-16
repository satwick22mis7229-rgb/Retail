from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String)

    phone = Column(String)

    address = Column(String)

    lead_time_days = Column(Integer, nullable=False, default=0)

    reliability_score = Column(Float, nullable=False, default=0.0)

    is_active = Column(Boolean, nullable=False, default=True)

    products = relationship("Product", back_populates="preferred_supplier")
    performance_records = relationship("SupplierPerformance", back_populates="supplier")
    purchase_orders = relationship("PurchaseOrder", back_populates="supplier")
    recommendations = relationship("Recommendation", back_populates="supplier")
