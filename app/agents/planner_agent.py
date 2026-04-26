from __future__ import annotations

from app.agents.base import Agent, AgentInput, AgentOutput


class PlannerAgent(Agent):
    name = "planner"
    _keywords = (
        "plano",
        "organiza",
        "organizar",
        "rotina",
        "estudo",
        "projeto",
        "meta",
    )

    def can_handle(self, text: str) -> bool:
        normalized = text.lower()
        return any(k in normalized for k in self._keywords)

    def run(self, payload: AgentInput) -> AgentOutput:
        return AgentOutput(
            agent_name=self.name,
            summary=(
                "Intencao de planejamento detectada. O agente pode quebrar objetivos "
                "em etapas e prioridades."
            ),
            actions=[
                "Definir objetivo principal",
                "Quebrar em tarefas semanais e diarias",
            ],
            data={"goal": payload.message},
        )
