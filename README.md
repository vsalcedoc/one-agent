# one-agent

A minimal Python starter using Anthropic's Claude Agent SDK. The agent can read and search the current project, but cannot edit files or run shell commands.

## Setup

Requires Python 3.10 or later.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set your Anthropic API key and a Claude model ID. Get an API key from the [Claude Console](https://console.anthropic.com/).

## Run

```bash
python agent.py "Summarize the project structure"
```

The agent is also available as the async `run_agent(prompt)` function from `agent.py`:

```python
import asyncio
from agent import run_agent

response = asyncio.run(run_agent("Summarize the project structure"))
print(response)
```