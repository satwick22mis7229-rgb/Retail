from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    sku: str
    category: str = "general"
    price: float
    cost_price: float
    description: str = ""
    safety_stock: int = 0
    reorder_point: int = 0
    reorder_quantity: int = 0
    preferred_supplier_id: int | None = None


class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    category: str
    price: float
    cost_price: float
    description: str
    safety_stock: int
    reorder_point: int
    reorder_quantity: int

    class Config:
        from_attributes = True
