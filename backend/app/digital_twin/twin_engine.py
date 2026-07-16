from app.intelligence.alert_engine import AlertEngine
from app.intelligence.recommendation_engine import RecommendationEngine
from app.intelligence.retail_state_engine import RetailStateEngine
from app.intelligence.risk_engine import RiskEngine


class TwinEngine:
    def __init__(
        self,
        retail_state_engine: RetailStateEngine | None = None,
        alert_engine: AlertEngine | None = None,
        risk_engine: RiskEngine | None = None,
        recommendation_engine: RecommendationEngine | None = None,
    ) -> None:
        self.retail_state_engine = retail_state_engine or RetailStateEngine()
        self.alert_engine = alert_engine or AlertEngine()
        self.risk_engine = risk_engine or RiskEngine()
        self.recommendation_engine = recommendation_engine or RecommendationEngine()

    def build_twin(self, *, inventory_items: list, sales: list, suppliers: list) -> dict:
        retail_state = self.retail_state_engine.build_state(
            inventory_items=inventory_items,
            sales=sales,
            suppliers=suppliers,
        )
        risks = self.risk_engine.calculate(retail_state)

        return {
            "status": "ready",
            "retail_state": retail_state,
            "alerts": self.alert_engine.build_alerts(retail_state),
            "risks": risks,
            "recommendations": self.recommendation_engine.generate(retail_state, risks),
        }

    def describe(self) -> dict:
        return {
            "status": "ready",
            "engines": [
                "retail_state_engine",
                "alert_engine",
                "risk_engine",
                "recommendation_engine",
            ],
        }
