from sqlalchemy import Column, Integer, Float, ForeignKey

from app.database.database import Base


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(
        Integer,
        ForeignKey("customers.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    quantity = Column(Integer)

    total_amount = Column(Float)