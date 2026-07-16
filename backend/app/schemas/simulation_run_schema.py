from pydantic import BaseModel


class SimulationRunCreate(BaseModel):
    store_id: int
    scenario_name: str
    scenario_payload: dict
    result_payload: dict = {}
