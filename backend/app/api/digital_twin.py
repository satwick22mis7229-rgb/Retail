from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.digital_twin_service import DigitalTwinService

router = APIRouter(
    prefix="/digital-twin",
    tags=["Digital Twin"],
)


@router.get("/state")
def get_digital_twin_state(db: Session = Depends(get_db)):
    digital_twin_service = DigitalTwinService()
    return digital_twin_service.get_snapshot(db)
