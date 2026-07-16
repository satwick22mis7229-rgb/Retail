from app.api.assistant import router as assistant_router
from app.api.customers import router as customer_router
from app.api.dashboard import router as dashboard_router
from app.api.digital_twin import router as digital_twin_router
from app.api.forecast import router as forecast_router
from app.api.inventory import router as inventory_router
from app.api.products import router as product_router
from app.api.sales import router as sales_router
from app.api.simulation import router as simulation_router
from app.api.suppliers import router as supplier_router
from app.api.warehouses import router as warehouse_router

__all__ = [
    "assistant_router",
    "customer_router",
    "dashboard_router",
    "digital_twin_router",
    "forecast_router",
    "inventory_router",
    "product_router",
    "sales_router",
    "simulation_router",
    "supplier_router",
    "warehouse_router",
]
