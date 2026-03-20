from fastapi import APIRouter, HTTPException

from app.api.models import AnalyzeRequest, CopilotRequest, EventsRequest, PrioritizeRequest
from app.services.analysis import summarize_signals
from app.services.llm import llm_service
from app.services.prioritizer import rank_items
from app.services.vector_store import vector_store

router = APIRouter(prefix="/api/v1")


@router.post("/analyze")
async def analyze(req: AnalyzeRequest) -> dict:
    if not req.signals:
        raise HTTPException(status_code=400, detail="signals cannot be empty")
    return summarize_signals(req.signals)


@router.post("/prioritize")
async def prioritize(req: PrioritizeRequest) -> dict:
    if not req.items:
        raise HTTPException(status_code=400, detail="items cannot be empty")
    return {"ranked": rank_items(req.items)}


@router.post("/copilot")
async def copilot(req: CopilotRequest) -> dict:
    retrieved = await vector_store.retrieve(req.question)
    merged_context = req.context + [item["text"] for item in retrieved]
    return await llm_service.answer(req.question, merged_context)


@router.post("/events")
async def ingest_events(req: EventsRequest) -> dict:
    return {"ingested": len(req.events), "status": "accepted"}


@router.get("/vector-health")
async def vector_health() -> dict:
    return await vector_store.health()
