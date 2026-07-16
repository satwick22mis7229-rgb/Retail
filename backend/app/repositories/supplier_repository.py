from sqlalchemy.orm import Session

from app.models.supplier import Supplier


class SupplierRepository:
    def list_all(self, db: Session) -> list[Supplier]:
        return db.query(Supplier).all()
