from __future__ import annotations

from app.agents.base import Agent, AgentInput, AgentOutput


class AutomationAgent(Agent):
    name = "automation"
    _keywords = (
        "automatiza",
        "automacao",
        "automação",
        "executa",
        "arquivo",
        "pasta",
        "agendar",
        "tarefa",
    )

    def can_handle(self, text: str) -> bool:
        normalized = text.lower()
        return any(k in normalized for k in self._keywords)

    def run(self, payload: AgentInput) -> AgentOutput:
        return AgentOutput(
            agent_name=self.name,
            summary=(
                "Fluxo de automacao detectado. O proximo passo e conectar ferramentas "
                "reais (calendario, shell seguro, APIs e n8n)."
            ),
            actions=[
                "Validar permissao do usuario para executar automacoes",
                "Gerar plano de etapas antes de acionar qualquer integracao",
            ],
            data={"request": payload.message},
        )
