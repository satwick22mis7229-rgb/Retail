class AssistantService:
    def get_placeholder_response(self, question: str) -> dict:
        return {
            "question": question,
            "status": "coming soon",
        }
