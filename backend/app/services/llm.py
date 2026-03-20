from __future__ import annotations

from app.core.config import settings


class LLMService:
    def __init__(self) -> None:
        self.model = settings.openai_model
        self.enabled = bool(settings.openai_api_key)

    async def answer(self, question: str, context: list[str]) -> dict:
        if not self.enabled:
            return {
                "mode": "mock",
                "answer": "LLM key is not configured. Returning local fallback guidance.",
                "recommended_actions": [
                    "Set OPENAI_API_KEY in backend/.env",
                    "Connect retrieval context from product data sources",
                    "Enable production evals before rollout",
                ],
                "context_used": context,
            }

        # Placeholder for a real OpenAI Responses API call.
        # Intentionally scaffolded for safe local development without secrets.
        return {
            "mode": "configured",
            "model": self.model,
            "answer": f"Plumb OpenAI Responses API here for question: {question}",
            "context_used": context,
        }


llm_service = LLMService()
