from app.intelligence.retail_state_engine import RetailStateEngine


class TwinEngine:
    def __init__(
        self,
        retail_state_engine: RetailStateEngine | None = None,
    ) -> None:
        self.retail_state_engine = retail_state_engine or RetailStateEngine()

    def build_twin(self, *, inventory_items: list, sales: list, suppliers: list) -> dict:
        return {
            "status": "ready",
            "snapshot": self.retail_state_engine.build_state(
                inventory_items=inventory_items,
                sales=sales,
                suppliers=suppliers,
            ),
        }

    def describe(self) -> dict:
        return {
            "status": "ready",
            "engines": [
                "retail_state_engine",
                "twin_engine",
            ],
        }
