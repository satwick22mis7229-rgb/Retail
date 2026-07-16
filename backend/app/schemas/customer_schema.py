from pydantic import BaseModel


class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    segment: str = "general"
    loyalty_tier: str = "standard"
