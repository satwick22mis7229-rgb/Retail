from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.supplier import Supplier

from app.schemas.supplier_schema import SupplierCreate

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)


@router.post("/")
def create_supplier(
    supplier: SupplierCreate,
    db: Session = Depends(get_db)
):
    new_supplier = Supplier(
        name=supplier.name,
        email=supplier.email,
        phone=supplier.phone,
        address=supplier.address
    )

    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)

    return new_supplier


@router.get("/")
def get_suppliers(
    db: Session = Depends(get_db)
):
    return db.query(Supplier).all()