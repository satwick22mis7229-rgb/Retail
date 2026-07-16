from pydantic import BaseModel


class InventoryCreate(BaseModel):
    product_id: int
    warehouse_id: int
    shelf_id: int | None = None
    quantity: int
    reserved_quantity: int = 0
    reorder_threshold: int = 0
