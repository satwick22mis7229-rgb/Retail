from app.models.sale import Sale


class SalesService:
    def summarize_sales(self, sales: list[Sale]) -> dict:
        total_revenue = sum(sale.total_amount for sale in sales)
        total_units = sum(sale.quantity for sale in sales)

        return {
            "sales_count": len(sales),
            "total_revenue": total_revenue,
            "total_units_sold": total_units,
        }
