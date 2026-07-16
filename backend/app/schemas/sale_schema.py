from pydantic import BaseModel


class SaleCreate(BaseModel):
    customer_id: int
    product_id: int
    warehouse_id: int | None = None
    quantity: int
    unit_price: float = 0.0
    total_amount: float = 0.0
