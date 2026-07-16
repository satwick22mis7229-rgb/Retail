from fastapi import APIRouter

from app.services.forecast_service import ForecastService

router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"],
)


@router.get("/")
def get_forecast():
    forecast_service = ForecastService()
    return forecast_service.get_placeholder()
