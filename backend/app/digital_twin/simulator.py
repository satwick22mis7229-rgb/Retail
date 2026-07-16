from app.digital_twin.event_engine import EventEngine
from app.digital_twin.state import SimulationEvent


class Simulator:
    def __init__(self, event_engine: EventEngine | None = None) -> None:
        self.event_engine = event_engine or EventEngine()

    def run(self, state: dict, event: SimulationEvent) -> dict:
        return {
            "status": "simulation_placeholder",
            "cloned_state": self.event_engine.apply(state, event),
        }
