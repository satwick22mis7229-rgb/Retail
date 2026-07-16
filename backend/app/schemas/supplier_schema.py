from pydantic import BaseModel


class SupplierCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    lead_time_days: int = 0
    reliability_score: float = 0.0
