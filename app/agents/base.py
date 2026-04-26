from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentInput:
    user_id: str
    message: str
    context: dict[str, Any] = field(default_factory=dict)
    memory: list[str] = field(default_factory=list)


@dataclass
class AgentOutput:
    agent_name: str
    summary: str
    actions: list[str] = field(default_factory=list)
    data: dict[str, Any] = field(default_factory=dict)


class Agent(ABC):
    name: str

    @abstractmethod
    def can_handle(self, text: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def run(self, payload: AgentInput) -> AgentOutput:
        raise NotImplementedError
