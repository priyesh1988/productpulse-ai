from pydantic import BaseModel, Field


class Signal(BaseModel):
    source: str = Field(default="feedback")
    text: str
    segment: str = Field(default="general")
    severity: float = Field(default=0.5, ge=0.0, le=1.0)


class AnalyzeRequest(BaseModel):
    signals: list[Signal]


class PrioritizationItem(BaseModel):
    title: str
    frequency: int = Field(ge=0)
    revenue_impact: float = Field(ge=0.0, le=1.0)
    complexity: float = Field(ge=0.0, le=1.0)
    churn_risk: float = Field(ge=0.0, le=1.0)


class PrioritizeRequest(BaseModel):
    items: list[PrioritizationItem]


class CopilotRequest(BaseModel):
    question: str
    context: list[str] = []


class EventsRequest(BaseModel):
    events: list[dict]
