class RiskEngine:
    def calculate(self, state: dict) -> dict:
        low_stock_items = state["inventory"]["low_stock_items"]
        supplier_count = state["suppliers"]["supplier_count"]

        inventory_risk = "high" if low_stock_items >= 3 else "moderate" if low_stock_items else "low"
        supplier_risk = "high" if supplier_count == 0 else "low"

        return {
            "inventory_risk": inventory_risk,
            "supplier_risk": supplier_risk,
        }
