class AlertEngine:
    def build_alerts(self, state: dict) -> list[str]:
        alerts: list[str] = []

        low_stock_count = state["inventory"]["low_stock_items"]
        if low_stock_count:
            alerts.append(f"{low_stock_count} products are below the low-stock threshold.")

        supplier_count = state["suppliers"]["supplier_count"]
        if supplier_count == 0:
            alerts.append("No suppliers are registered yet.")

        return alerts
