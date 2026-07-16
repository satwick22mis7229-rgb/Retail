from app.digital_twin.state import SimulationEvent


class EventEngine:
    def apply(self, state: dict, event: SimulationEvent) -> dict:
        simulated_state = dict(state)
        simulated_state["scenario"] = {
            "supplier_delay_days": event.supplier_delay_days,
            "demand_multiplier": event.demand_multiplier,
        }
        return simulated_state
