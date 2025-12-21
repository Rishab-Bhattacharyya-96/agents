from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Greeting agent',
    instruction="""You are an helpful assistant that greets users.
    
    Ask the user for their name and greet them warmly.
    """,
)

