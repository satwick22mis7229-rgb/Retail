from pydantic import BaseModel


class AlertCreate(BaseModel):
    store_id: int
    alert_type: str
    severity: str = "medium"
    status: str = "open"
    title: str
    message: str
