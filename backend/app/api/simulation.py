from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.digital_twin.simulator import Simulator
from app.digital_twin.state import SimulationEvent
from app.intelligence.retail_state_engine import RetailStateEngine
from app.models.inventory import Inventory
from app.models.sale import Sale
from app.models.supplier import Supplier

router = APIRouter(
    prefix="/simulation",
    tags=["Simulation"],
)


@router.post("/run")
def run_simulation(event: SimulationEvent, db: Session = Depends(get_db)):
    state_engine = RetailStateEngine()
    simulator = Simulator()

    state = state_engine.build_state(
        inventory_items=db.query(Inventory).all(),
        sales=db.query(Sale).all(),
        suppliers=db.query(Supplier).all(),
    )

    return simulator.run(state, event)
