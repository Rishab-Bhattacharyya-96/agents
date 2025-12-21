from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from datetime import datetime

def get_current_time():
    """
    get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

root_agent = Agent(
    name="basic_search_agent",
    model="gemini-2.5-flash",
    description="Tool agent",
    instruction="""You are an helpful assistant that can use the following tools
    - get_current_time: to get the current time
    """,
    # google_search is a pre-built tool which allows the agent to perform Google searches.
    tools=[get_current_time]
)
