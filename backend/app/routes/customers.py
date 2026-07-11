from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.customer import Customer

from app.schemas.customer_schema import CustomerCreate

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post("/")
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    new_customer = Customer(
        name=customer.name,
        email=customer.email,
        phone=customer.phone,
        address=customer.address
    )

    db.add(new_customer)

    db.commit()

    db.refresh(new_customer)

    return new_customer


@router.get("/")
def get_customers(
    db: Session = Depends(get_db)
):
    return db.query(Customer).all()