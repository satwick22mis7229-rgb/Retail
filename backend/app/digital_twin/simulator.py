from app.digital_twin.event_engine import EventEngine
from app.digital_twin.state import SimulationEvent


class Simulator:
    def __init__(self, event_engine: EventEngine | None = None) -> None:
        self.event_engine = event_engine or EventEngine()

    def run(self, state: dict, event: SimulationEvent) -> dict:
        scenario_state = self.event_engine.apply(state, event)
        low_stock_items = scenario_state["inventory"]["low_stock_items"]

        estimated_stockout_products = max(
            low_stock_items,
            int(low_stock_items * event.demand_multiplier),
        )

        return {
            "scenario": scenario_state["scenario"],
            "estimated_stockout_products": estimated_stockout_products,
            "estimated_lost_sales": estimated_stockout_products * 1000 * max(1, event.supplier_delay_days),
            "status": "simulation_stub_ready",
        }
