from datetime import date

from pydantic import BaseModel


class DemandForecastCreate(BaseModel):
    product_id: int
    forecast_date: date
    predicted_units: float
    confidence_score: float = 0.0
    model_name: str = "baseline"
