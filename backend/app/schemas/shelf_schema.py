from pydantic import BaseModel


class ShelfCreate(BaseModel):
    warehouse_id: int
    product_id: int | None = None
    code: str
    zone: str = "general"
    capacity: int = 0
