from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.inventory import Inventory
from app.schemas.inventory_schema import InventoryCreate

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
    inventory: InventoryCreate,
    db: Session = Depends(get_db)
):
    item = Inventory(
        product_id=inventory.product_id,
        warehouse_id=inventory.warehouse_id,
        shelf_id=inventory.shelf_id,
        quantity=inventory.quantity,
        reserved_quantity=inventory.reserved_quantity,
        reorder_threshold=inventory.reorder_threshold,
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item
