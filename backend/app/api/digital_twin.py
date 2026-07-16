from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.digital_twin.twin_engine import TwinEngine
from app.models.inventory import Inventory
from app.models.sale import Sale
from app.models.supplier import Supplier

router = APIRouter(
    prefix="/digital-twin",
    tags=["Digital Twin"],
)


@router.get("/state")
def get_digital_twin_state(db: Session = Depends(get_db)):
    twin_engine = TwinEngine()
    inventory_items = db.query(Inventory).all()
    sales = db.query(Sale).all()
    suppliers = db.query(Supplier).all()

    return twin_engine.build_twin(
        inventory_items=inventory_items,
        sales=sales,
        suppliers=suppliers,
    )
