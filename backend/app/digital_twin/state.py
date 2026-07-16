from pydantic import BaseModel, Field


class SimulationEvent(BaseModel):
    supplier_delay_days: int = Field(default=0, ge=0)
    demand_multiplier: float = Field(default=1.0, gt=0)
