from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models.product import Product
from app.routes.products import router as product_router
from app.models.inventory import Inventory
from app.routes.inventory import router as inventory_router
from app.models.customer import Customer
from app.routes.customers import router as customer_router
from app.models.sale import Sale
from app.routes.sales import router as sales_router
from app.models.supplier import Supplier
from app.routes.suppliers import router as supplier_router
from app.models.warehouse import Warehouse
from app.routes.warehouse import router as warehouse_router
from app.routes.dashboard import router as dashboard_router

from app.database.database import (
    Base,
    engine
)

from app.models.user import User


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Retail Platform"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(
    dashboard_router,
    prefix="/dashboard",
    tags=["Dashboard"]
)

app.include_router(product_router)
app.include_router(inventory_router)
app.include_router(customer_router)
app.include_router(sales_router)
app.include_router(supplier_router)
app.include_router(warehouse_router)
app.include_router(dashboard_router)


@app.get("/")
def home():
    return {
        "message": "Smart Retail API Running"
    }