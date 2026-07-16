from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
import csv
import io
from app.database.database import get_db

from app.models.sale import Sale
from app.models.customer import Customer
from app.models.product import Product
from app.models.inventory import Inventory

from app.schemas.sale_schema import SaleCreate

router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)
@router.get("/report")
def download_sales_report(
    db: Session = Depends(get_db)
):
    sales = db.query(Sale).all()

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow([
        "ID",
        "Customer ID",
        "Product ID",
        "Quantity",
        "Total Amount"
    ])

    for sale in sales:
        writer.writerow([
            sale.id,
            sale.customer_id,
            sale.product_id,
            sale.quantity,
            sale.total_amount
        ])

    output.seek(0)

    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=sales_report.csv"
        }
    )
@router.delete("/{sale_id}")
def delete_sale(
    sale_id: int,
    db: Session = Depends(get_db)
):
    sale = (
        db.query(Sale)
        .filter(Sale.id == sale_id)
        .first()
    )

    if not sale:
        raise HTTPException(
            status_code=404,
            detail="Sale not found"
        )

    db.delete(sale)
    db.commit()

    return {"message": "Deleted"}
@router.post("/")
def create_sale(
    sale: SaleCreate,
    db: Session = Depends(get_db)
):
    customer = (
        db.query(Customer)
        .filter(Customer.id == sale.customer_id)
        .first()
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    product = (
        db.query(Product)
        .filter(Product.id == sale.product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    inventory = (
        db.query(Inventory)
        .filter(
            Inventory.product_id == sale.product_id
        )
        .first()
    )

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )

    if inventory.quantity < sale.quantity:
        raise HTTPException(
            status_code=400,
            detail="Not enough stock"
        )

    inventory.quantity -= sale.quantity

    unit_price = sale.unit_price or product.price
    total = sale.total_amount or (unit_price * sale.quantity)

    new_sale = Sale(
        customer_id=sale.customer_id,
        product_id=sale.product_id,
        warehouse_id=sale.warehouse_id or inventory.warehouse_id,
        quantity=sale.quantity,
        unit_price=unit_price,
        total_amount=total,
    )

    db.add(new_sale)

    db.commit()

    db.refresh(new_sale)

    return {
        "message": "Sale completed",
        "total_amount": total
    }


@router.get("/")
def get_sales(
    db: Session = Depends(get_db)
):
    return db.query(Sale).all()
