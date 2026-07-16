from sqlalchemy.orm import Session

from app.digital_twin.twin_engine import TwinEngine
from app.repositories.inventory_repository import InventoryRepository
from app.repositories.sale_repository import SaleRepository
from app.repositories.supplier_repository import SupplierRepository


class DigitalTwinService:
    def __init__(
        self,
        inventory_repository: InventoryRepository | None = None,
        sale_repository: SaleRepository | None = None,
        supplier_repository: SupplierRepository | None = None,
        twin_engine: TwinEngine | None = None,
    ) -> None:
        self.inventory_repository = inventory_repository or InventoryRepository()
        self.sale_repository = sale_repository or SaleRepository()
        self.supplier_repository = supplier_repository or SupplierRepository()
        self.twin_engine = twin_engine or TwinEngine()

    def get_snapshot(self, db: Session) -> dict:
        return self.twin_engine.build_twin(
            inventory_items=self.inventory_repository.list_all(db),
            sales=self.sale_repository.list_all(db),
            suppliers=self.supplier_repository.list_all(db),
        )
