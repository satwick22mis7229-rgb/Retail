from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import (
    assistant_router,
    customer_router,
    dashboard_router,
    digital_twin_router,
    forecast_router,
    inventory_router,
    product_router,
    sales_router,
    simulation_router,
    supplier_router,
    warehouse_router,
)
from app.core.config import settings
from app.digital_twin.twin_engine import TwinEngine
from app.intelligence.retail_state_engine import RetailStateEngine
from app.models.customer import Customer
from app.models.demand_forecast import DemandForecast
from app.models.digital_twin_snapshot import DigitalTwinSnapshot
from app.models.inventory import Inventory
from app.models.inventory_event import InventoryEvent
from app.models.product import Product
from app.models.purchase_order import PurchaseOrder
from app.models.recommendation import Recommendation
from app.models.sale import Sale
from app.models.shelf import Shelf
from app.models.simulation_run import SimulationRun
from app.models.store import Store
from app.models.supplier import Supplier
from app.models.supplier_performance import SupplierPerformance
from app.models.user import User
from app.models.warehouse import Warehouse

def create_application() -> FastAPI:
    app = FastAPI(title=settings.app_name)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(product_router)
    app.include_router(inventory_router)
    app.include_router(customer_router)
    app.include_router(sales_router)
    app.include_router(supplier_router)
    app.include_router(warehouse_router)
    app.include_router(dashboard_router)
    app.include_router(digital_twin_router)
    app.include_router(forecast_router)
    app.include_router(simulation_router)
    app.include_router(assistant_router)

    retail_state_engine = RetailStateEngine()
    twin_engine = TwinEngine(retail_state_engine=retail_state_engine)

    @app.get("/")
    def home():
        return {
            "message": "Smart Retail API Running",
            "platform": "AI-Native Smart Retail Digital Twin Platform",
            "phase": "Module 2 - Database Redesign",
            "available_domains": [
                "retail_management",
                "retail_intelligence",
                "digital_twin",
                "forecasting",
                "simulation",
                "assistant",
            ],
            "digital_twin_ready": twin_engine.describe()["status"],
        }

    return app


app = create_application()
