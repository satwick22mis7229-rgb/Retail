from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.inventory import Inventory

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/low-stock")
def low_stock(db: Session = Depends(get_db)):
    return (
        db.query(Inventory)
        .filter(Inventory.quantity < 20)
        .all()
    )
@router.get("/")
def get_inventory(db: Session = Depends(get_db)):
    return db.query(Inventory).all()


@router.post("/")
def add_inventory(
    product_id: int,
    quantity: int,
    db: Session = Depends(get_db)
):
    item = Inventory(
        product_id=product_id,
        quantity=quantity
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item