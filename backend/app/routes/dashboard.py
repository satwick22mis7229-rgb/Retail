from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.database import SessionLocal
from app.models.product import Product
from app.models.customer import Customer
from app.models.sale import Sale

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.get("/top-products")
def top_products(db: Session = Depends(get_db)):

    result = (
        db.query(
            Sale.product_id,
            func.sum(Sale.quantity).label("total")
        )
        .group_by(Sale.product_id)
        .order_by(func.sum(Sale.quantity).desc())
        .limit(5)
        .all()
    )

    return [
        {
            "product_id": row.product_id,
            "total": row.total
        }
        for row in result
    ]
    
@router.get("/profit")
def profit(db: Session = Depends(get_db)):

    sales = db.query(Sale).all()

    profit = 0

    for sale in sales:

        product = (
            db.query(Product)
            .filter(Product.id == sale.product_id)
            .first()
        )

        if product:
            profit += (
                product.price -
                product.cost_price
            ) * sale.quantity

    return {"profit": profit}
@router.get("/")
def dashboard(db: Session = Depends(get_db)):
    total_products = db.query(Product).count()
    total_customers = db.query(Customer).count()
    total_sales = db.query(Sale).count()

    revenue = (
        db.query(func.sum(Sale.total_amount))
        .scalar()
    ) or 0

    return {
        "total_products": total_products,
        "total_customers": total_customers,
        "total_sales": total_sales,
        "total_revenue": revenue
    }