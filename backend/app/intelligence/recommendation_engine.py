class RecommendationEngine:
    def generate(self, state: dict, risks: dict) -> list[str]:
        recommendations: list[str] = []

        if risks["inventory_risk"] != "low":
            recommendations.append(
                "Prioritize reorder-point logic and stockout prediction for low-stock products."
            )

        if risks["supplier_risk"] == "high":
            recommendations.append(
                "Register supplier lead times and alternate suppliers before enabling simulations."
            )

        if not recommendations:
            recommendations.append(
                "Proceed to demand forecasting using the stabilized retail data model."
            )

        return recommendations
