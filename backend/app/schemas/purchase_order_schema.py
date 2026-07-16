from datetime import datetime

from pydantic import BaseModel


class PurchaseOrderCreate(BaseModel):
    supplier_id: int
    warehouse_id: int
    status: str = "pending"
    expected_delivery_at: datetime | None = None
    total_amount: float = 0.0
