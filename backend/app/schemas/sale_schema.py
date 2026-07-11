from pydantic import BaseModel


class SaleCreate(BaseModel):
    customer_id: int
    product_id: int
    quantity: int