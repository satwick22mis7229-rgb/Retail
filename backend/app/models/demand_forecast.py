from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class DemandForecast(Base):
    __tablename__ = "demand_forecasts"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    forecast_date = Column(Date, nullable=False)
    predicted_units = Column(Float, nullable=False)
    confidence_score = Column(Float, nullable=False, default=0.0)
    model_name = Column(String, nullable=False, default="baseline")
    model_version = Column(String, nullable=False, default="v1")
    forecast_horizon = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    product = relationship("Product", back_populates="forecasts")
