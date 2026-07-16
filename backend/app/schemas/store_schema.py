from pydantic import BaseModel


class StoreCreate(BaseModel):
    name: str
    code: str
    location: str
    manager_name: str | None = None
