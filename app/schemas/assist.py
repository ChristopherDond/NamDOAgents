from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class AssistRequest(BaseModel):
    user_id: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)
    context: dict[str, Any] = Field(default_factory=dict)


class StepResult(BaseModel):
    agent: str
    summary: str
    actions: list[str] = Field(default_factory=list)
    data: dict[str, Any] = Field(default_factory=dict)


class AssistResponse(BaseModel):
    reply: str
    steps: list[StepResult]
