from sqlalchemy.orm import Session

from app.digital_twin.simulator import Simulator
from app.digital_twin.state import SimulationEvent
from app.services.digital_twin_service import DigitalTwinService


class SimulationService:
    def __init__(
        self,
        digital_twin_service: DigitalTwinService | None = None,
        simulator: Simulator | None = None,
    ) -> None:
        self.digital_twin_service = digital_twin_service or DigitalTwinService()
        self.simulator = simulator or Simulator()

    def simulate(self, db: Session, event: SimulationEvent) -> dict:
        snapshot = self.digital_twin_service.get_snapshot(db)
        return self.simulator.run(snapshot, event)
