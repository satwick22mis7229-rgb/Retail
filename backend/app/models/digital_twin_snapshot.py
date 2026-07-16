from sqlalchemy import Column, DateTime, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class DigitalTwinSnapshot(Base):
    __tablename__ = "digital_twin_snapshots"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)
    snapshot_payload = Column(JSON, nullable=False, default=dict)
    snapshot_version = Column(String, nullable=False, default="v1")
    state_hash = Column(String, index=True)
    created_by = Column(String, nullable=False, default="system")
    captured_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    store = relationship("Store", back_populates="twin_snapshots")
