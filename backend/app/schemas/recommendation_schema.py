from pydantic import BaseModel


class RecommendationCreate(BaseModel):
    product_id: int | None = None
    supplier_id: int | None = None
    recommendation_type: str
    priority: str = "medium"
    confidence_score: float = 0.0
    rationale: str
    execution_status: str = "pending"
