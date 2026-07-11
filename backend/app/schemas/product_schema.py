from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    sku: str
    price: float
    cost_price: float
    description: str


class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    price: float
    cost_price: float
    description: str

    class Config:
        from_attributes = True