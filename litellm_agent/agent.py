import os
import random
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

MODEL_GPT_40 = "openai/gpt-4.1"
MODEL_CLAUDE_SONNET = "claude-3-7-sonnet-20250219"
MODEL_GEMINI_2_5_FLASH = "gemini-2.5-flash"

def get_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't programmers like nature? It has too many bugs.",
        "Why do cows have hooves instead of feet? Because they lactose.",
        "Why did the bicycle fall over? Because it was two-tired!"
    ]
    return {"joke": random.choice(jokes)}

root_agent = Agent(
    model=LiteLlm(model=MODEL_GEMINI_2_5_FLASH, api_key=os.getenv("GOOGLE_API_KEY"), provider="google"),
    name='dad_joke_agent',
    description='Dad Joke Agent',
    instruction="""
    You are an helpful assistant that can tell jokes use the following tools
    - get_joke: to get a dad joke
    """,
    tools=[get_joke]
)
