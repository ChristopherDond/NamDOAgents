# JangUI

A multi-agent AI orchestration system built with FastAPI that coordinates autonomous agents for knowledge management, planning, and automation tasks.

## Overview

JangUI is a framework for building intelligent systems with multiple specialized agents that work together to accomplish complex tasks. It provides:

- **Multiple Agent Types**: Knowledge, Planner, and Automation agents
- **Centralized Orchestration**: Coordinates agent interactions and task execution
- **Memory Management**: Persistent state and context across agent operations
- **REST API**: FastAPI-based interface for agent interaction

## Project Structure

```
JangUI/
├── app/
│   ├── agents/              # Agent implementations
│   │   ├── base.py         # Base agent class
│   │   ├── knowledge_agent.py
│   │   ├── planner_agent.py
│   │   ├── automation_agent.py
│   │   └── __init__.py
│   ├── core/               # Core system components
│   │   ├── orchestrator.py # Agent coordination
│   │   └── memory.py       # State management
│   ├── schemas/            # Pydantic models
│   │   ├── assist.py
│   │   └── __init__.py
│   └── main.py            # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── run.ps1                # Windows startup script
└── README.md              # This file
```

## Requirements

- Python 3.8+
- FastAPI 0.116.1
- Uvicorn 0.35.0
- Pydantic 2.11.7

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd JangUI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### On Windows (PowerShell):
```bash
.\run.ps1
```

### Manual startup:
```bash
python -m uvicorn app.main:app --app-dir . --host 127.0.0.1 --port 8000 --reload
```

The API will be available at `http://127.0.0.1:8000`

## Agents

### Knowledge Agent
Handles information retrieval and knowledge base queries.

### Planner Agent
Creates and manages task plans and execution strategies.

### Automation Agent
Executes automated tasks and processes.

## API Documentation

Once running, access the interactive API documentation:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Development

The project uses FastAPI's automatic reload feature for development. Modify agent implementations or core components and changes will be reflected immediately on save.

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
