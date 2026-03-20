class VectorStore:
    def __init__(self) -> None:
        self.provider = "qdrant+pgvector"

    async def health(self) -> dict:
        return {"provider": self.provider, "status": "not_connected_in_scaffold"}

    async def retrieve(self, query: str) -> list[dict]:
        return [
            {
                "id": "demo-1",
                "score": 0.89,
                "text": f"Placeholder retrieved context for query: {query}",
            }
        ]


vector_store = VectorStore()
