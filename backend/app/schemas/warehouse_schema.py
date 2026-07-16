from pydantic import BaseModel


class WarehouseCreate(BaseModel):
    store_id: int
    name: str
    location: str
    capacity: float = 0.0
