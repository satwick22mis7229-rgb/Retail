from app.models.supplier import Supplier


class SupplierService:
    def summarize_suppliers(self, suppliers: list[Supplier]) -> dict:
        contactable_suppliers = [
            supplier for supplier in suppliers
            if supplier.email or supplier.phone
        ]

        return {
            "supplier_count": len(suppliers),
            "contactable_suppliers": len(contactable_suppliers),
        }
