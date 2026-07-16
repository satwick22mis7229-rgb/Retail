from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.inventory import Inventory
from app.models.sale import Sale

router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"],
)


@router.get("/demand")
def demand_forecast(db: Session = Depends(get_db)):
    sales = db.query(Sale).all()
    inventory_items = db.query(Inventory).all()

    total_units_sold = sum(sale.quantity for sale in sales)
    tracked_products = max(1, len(inventory_items))
    baseline_daily_demand = round(total_units_sold / tracked_products, 2)

    return {
        "status": "baseline_ready",
        "model_stage": "rule_based_baseline",
        "next_step": "replace baseline with XGBoost or LightGBM in Module 6",
        "signals": {
            "total_units_sold": total_units_sold,
            "tracked_products": tracked_products,
            "baseline_daily_demand": baseline_daily_demand,
        },
    }
