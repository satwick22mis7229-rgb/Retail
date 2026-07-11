from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.product import Product
from app.schemas.product_schema import ProductCreate

router = APIRouter(prefix="/products", tags=["Products"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return {"message": "Product not found"}

    db.delete(product)
    db.commit()

    return {"message": "Deleted"}
@router.put("/{product_id}")
def update_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    db_product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not db_product:
        return {"message": "Product not found"}

    db_product.name = product.name
    db_product.sku = product.sku
    db_product.price = product.price
    db_product.cost_price = product.cost_price
    db_product.description = product.description

    db.commit()
    db.refresh(db_product)

    return db_product
@router.post("/")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    new_product = Product(
        name=product.name,
        sku=product.sku,
        price=product.price,
        cost_price=product.cost_price,
        description=product.description
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product