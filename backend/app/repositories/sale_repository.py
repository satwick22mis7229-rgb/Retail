from sqlalchemy.orm import Session

from app.models.sale import Sale


class SaleRepository:
    def list_all(self, db: Session) -> list[Sale]:
        return db.query(Sale).all()
