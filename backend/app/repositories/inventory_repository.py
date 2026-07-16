from sqlalchemy.orm import Session

from app.models.inventory import Inventory


class InventoryRepository:
    def list_all(self, db: Session) -> list[Inventory]:
        return db.query(Inventory).all()
