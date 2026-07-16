from app.models.inventory import Inventory


class InventoryService:
    low_stock_threshold = 20

    def summarize_inventory(self, inventory_items: list[Inventory]) -> dict:
        total_units = sum(item.quantity for item in inventory_items)
        low_stock_items = [
            item for item in inventory_items
            if item.quantity < self.low_stock_threshold
        ]

        return {
            "tracked_items": len(inventory_items),
            "total_units": total_units,
            "low_stock_items": len(low_stock_items),
            "low_stock_threshold": self.low_stock_threshold,
        }
