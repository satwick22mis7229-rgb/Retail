from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.digital_twin.state import SimulationEvent
from app.services.simulation_service import SimulationService

router = APIRouter(
    prefix="/simulate",
    tags=["Simulation"],
)


@router.post("/")
def run_simulation(event: SimulationEvent, db: Session = Depends(get_db)):
    simulation_service = SimulationService()
    return simulation_service.simulate(db, event)
