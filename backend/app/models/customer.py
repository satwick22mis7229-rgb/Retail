from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String)

    phone = Column(String)

    address = Column(String)

    segment = Column(String, nullable=False, default="general")

    loyalty_tier = Column(String, nullable=False, default="standard")

    sales = relationship("Sale", back_populates="customer")
