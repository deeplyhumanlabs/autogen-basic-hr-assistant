import asyncio
from dotenv import load_dotenv

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()

async def main():
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini"
    )

    try:
        agent = AssistantAgent(
            name="hr_assistant",
            model_client=model_client,
            system_message="You are an HR assistant."
        )

        task = (
            "Write exactly five numbered lines describing the "
            "responsibilities of a Junior Python Developer. "
            "Do not include a heading or introductory text."
        )

        await Console(agent.run_stream(task=task))

    finally:
        await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())