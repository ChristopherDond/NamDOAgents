from __future__ import annotations

from app.agents.automation_agent import AutomationAgent
from app.agents.base import AgentInput, AgentOutput
from app.agents.knowledge_agent import KnowledgeAgent
from app.agents.planner_agent import PlannerAgent
from app.core.memory import InMemoryStore
from app.schemas.assist import AssistRequest, AssistResponse, StepResult


class Orchestrator:
    def __init__(self) -> None:
        self.memory = InMemoryStore()
        self.agents = [
            PlannerAgent(),
            AutomationAgent(),
            KnowledgeAgent(),
        ]

    def _select_agents(self, text: str) -> list:
        selected = [agent for agent in self.agents if agent.can_handle(text)]
        if selected:
            return selected
        return [PlannerAgent()]

    def process(self, request: AssistRequest) -> AssistResponse:
        recent = self.memory.get_recent(request.user_id)
        payload = AgentInput(
            user_id=request.user_id,
            message=request.message,
            context=request.context,
            memory=recent,
        )

        selected_agents = self._select_agents(request.message)
        outputs: list[AgentOutput] = [agent.run(payload) for agent in selected_agents]

        self.memory.append(request.user_id, request.message)

        steps = [
            StepResult(
                agent=out.agent_name,
                summary=out.summary,
                actions=out.actions,
                data=out.data,
            )
            for out in outputs
        ]

        reply = " | ".join(step.summary for step in steps)
        return AssistResponse(reply=reply, steps=steps)
