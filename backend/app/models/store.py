from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, unique=True, nullable=False)
    location = Column(String, nullable=False)
    manager_name = Column(String)

    warehouses = relationship("Warehouse", back_populates="store")
    alerts = relationship("Alert", back_populates="store")
    simulation_runs = relationship("SimulationRun", back_populates="store")
    twin_snapshots = relationship("DigitalTwinSnapshot", back_populates="store")
