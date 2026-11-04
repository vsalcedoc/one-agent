import asyncio
import os
import sys

from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query
from dotenv import load_dotenv

load_dotenv()


async def run_agent(prompt: str) -> str:
    if not os.getenv("ANTHROPIC_API_KEY"):
        raise RuntimeError("Set ANTHROPIC_API_KEY in your .env file.")

    if not prompt.strip():
        raise ValueError("Provide a prompt for the agent.")

    options = ClaudeAgentOptions(
        model=os.getenv("CLAUDE_MODEL") or None,
        tools=["Read", "Glob", "Grep"],
        allowed_tools=["Read", "Glob", "Grep"],
    )

    result = ""
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, ResultMessage) and message.subtype == "success":
            result = message.result or ""

    return result


def main() -> None:
    prompt = " ".join(sys.argv[1:]).strip()

    try:
        print(asyncio.run(run_agent(prompt)))
    except Exception as error:
        print(f"Agent failed: {error}", file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()