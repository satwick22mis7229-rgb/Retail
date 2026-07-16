from fastapi import APIRouter
from pydantic import BaseModel

from app.services.assistant_service import AssistantService

router = APIRouter(
    prefix="/assistant",
    tags=["Assistant"],
)


class AssistantQuestion(BaseModel):
    question: str


@router.post("/query")
def analyze_question(payload: AssistantQuestion):
    assistant_service = AssistantService()
    return assistant_service.get_placeholder_response(payload.question)
