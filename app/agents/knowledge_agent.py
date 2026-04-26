from __future__ import annotations

from app.agents.base import Agent, AgentInput, AgentOutput


class KnowledgeAgent(Agent):
    name = "knowledge"
    _keywords = (
        "pesquisa",
        "buscar",
        "resumo",
        "explica",
        "o que e",
        "oq e",
        "como funciona",
    )

    def can_handle(self, text: str) -> bool:
        normalized = text.lower()
        return any(k in normalized for k in self._keywords)

    def run(self, payload: AgentInput) -> AgentOutput:
        return AgentOutput(
            agent_name=self.name,
            summary=(
                "Pedido de conhecimento detectado. Este agente prepara consultas e "
                "respostas resumidas para o usuario."
            ),
            actions=[
                "Coletar fontes confiaveis",
                "Gerar resumo curto e objetivo",
            ],
            data={"query": payload.message},
        )
