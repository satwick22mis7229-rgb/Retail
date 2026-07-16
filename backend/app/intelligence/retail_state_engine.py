from app.services.inventory_service import InventoryService
from app.services.sales_service import SalesService
from app.services.supplier_service import SupplierService


class RetailStateEngine:
    def __init__(
        self,
        inventory_service: InventoryService | None = None,
        sales_service: SalesService | None = None,
        supplier_service: SupplierService | None = None,
    ) -> None:
        self.inventory_service = inventory_service or InventoryService()
        self.sales_service = sales_service or SalesService()
        self.supplier_service = supplier_service or SupplierService()

    def build_state(
        self,
        *,
        inventory_items: list,
        sales: list,
        suppliers: list,
    ) -> dict:
        return {
            "inventory": self.inventory_service.summarize_inventory(inventory_items),
            "sales": self.sales_service.summarize_sales(sales),
            "suppliers": self.supplier_service.summarize_suppliers(suppliers),
        }
