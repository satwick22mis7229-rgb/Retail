from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.warehouse import Warehouse

from app.schemas.warehouse_schema import WarehouseCreate

router = APIRouter(
    prefix="/warehouse",
    tags=["Warehouse"]
)


@router.post("/")
def create_warehouse(
    warehouse: WarehouseCreate,
    db: Session = Depends(get_db)
):
    data = Warehouse(
        store_id=warehouse.store_id,
        name=warehouse.name,
        location=warehouse.location,
        capacity=warehouse.capacity,
    )

    db.add(data)
    db.commit()
    db.refresh(data)

    return data


@router.get("/")
def get_warehouse(
    db: Session = Depends(get_db)
):
    return db.query(Warehouse).all()
