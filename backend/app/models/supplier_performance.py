from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class SupplierPerformance(Base):
    __tablename__ = "supplier_performance"

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    measured_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    on_time_delivery_rate = Column(Float, nullable=False, default=0.0)
    average_lead_time_days = Column(Float, nullable=False, default=0.0)
    defect_rate = Column(Float, nullable=False, default=0.0)
    delay_incidents = Column(Integer, nullable=False, default=0)

    supplier = relationship("Supplier", back_populates="performance_records")
