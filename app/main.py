from __future__ import annotations

from fastapi import FastAPI

from app.core.orchestrator import Orchestrator
from app.schemas.assist import AssistRequest, AssistResponse

app = FastAPI(title="JangUI Core", version="0.1.0")
orchestrator = Orchestrator()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/assist", response_model=AssistResponse)
def assist(request: AssistRequest) -> AssistResponse:
    return orchestrator.process(request)
