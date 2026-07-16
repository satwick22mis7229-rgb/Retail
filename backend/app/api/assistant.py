from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.digital_twin.twin_engine import TwinEngine
from app.models.inventory import Inventory
from app.models.sale import Sale
from app.models.supplier import Supplier

router = APIRouter(
    prefix="/assistant",
    tags=["Assistant"],
)


class AssistantQuestion(BaseModel):
    question: str


@router.post("/analyze")
def analyze_question(payload: AssistantQuestion, db: Session = Depends(get_db)):
    twin_engine = TwinEngine()
    twin = twin_engine.build_twin(
        inventory_items=db.query(Inventory).all(),
        sales=db.query(Sale).all(),
        suppliers=db.query(Supplier).all(),
    )

    return {
        "question": payload.question,
        "status": "coordinator_stub_ready",
        "summary": "This assistant currently answers from live retail state summaries and is ready for RAG and agent routing.",
        "state_snapshot": twin["retail_state"],
        "recommendations": twin["recommendations"],
    }
