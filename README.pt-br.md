[English Version](./README.md)

# JangUI

Um sistema de orquestração multi-agente construído com FastAPI que coordena agentes autônomos para tarefas de gestão de conhecimento, planejamento e automação.

## Visão Geral

JangUI é um framework para construir sistemas inteligentes com múltiplos agentes especializados que trabalham juntos para realizar tarefas complexas. Oferece:

- **Múltiplos Tipos de Agentes**: Agentes de conhecimento, planejamento e automação
- **Orquestração Centralizada**: Coordena interações entre agentes e execução de tarefas
- **Gestão de Memória**: Estado persistente e contexto nas operações dos agentes
- **API REST**: Interface baseada em FastAPI para interação com agentes

## Estrutura do Projeto

```
JangUI/
├── app/
│   ├── agents/              # Implementação dos agentes
│   │   ├── base.py         # Classe base do agente
│   │   ├── knowledge_agent.py
│   │   ├── planner_agent.py
│   │   ├── automation_agent.py
│   │   └── __init__.py
│   ├── core/               # Componentes principais do sistema
│   │   ├── orchestrator.py # Coordenação de agentes
│   │   └── memory.py       # Gestão de estado
│   ├── schemas/            # Modelos Pydantic
│   │   ├── assist.py
│   │   └── __init__.py
│   └── main.py            # Ponto de entrada da aplicação FastAPI
├── requirements.txt        # Dependências Python
├── run.ps1                # Script de inicialização para Windows
└── README.md              # Este arquivo
```

## Requisitos

- Python 3.8+
- FastAPI 0.116.1
- Uvicorn 0.35.0
- Pydantic 2.11.7

## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd JangUI
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando a Aplicação

### No Windows (PowerShell):
```bash
.\run.ps1
```

### Inicialização manual:
```bash
python -m uvicorn app.main:app --app-dir . --host 127.0.0.1 --port 8000 --reload
```

A API estará disponível em `http://127.0.0.1:8000`

## Agentes

### Agente de Conhecimento
Gerencia recuperação de informações e consultas na base de conhecimento.

### Agente de Planejamento
Cria e gerencia planos de tarefas e estratégias de execução.

### Agente de Automação
Executa tarefas automatizadas e processos.

## Documentação da API

Quando em execução, acesse a documentação interativa da API:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Desenvolvimento

O projeto usa o recurso de recarga automática do FastAPI para desenvolvimento. Modifique as implementações dos agentes ou componentes principais e as mudanças serão refletidas imediatamente ao salvar.

## Licença

[Adicione informações de licença aqui]

## Contribuindo

[Adicione diretrizes de contribuição aqui]
