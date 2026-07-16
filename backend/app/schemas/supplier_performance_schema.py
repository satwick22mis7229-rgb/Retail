from pydantic import BaseModel


class SupplierPerformanceCreate(BaseModel):
    supplier_id: int
    on_time_delivery_rate: float = 0.0
    average_lead_time_days: float = 0.0
    defect_rate: float = 0.0
    delay_incidents: int = 0
