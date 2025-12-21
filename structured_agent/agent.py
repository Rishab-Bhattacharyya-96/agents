from google.adk.agents.llm_agent import Agent
from pydantic import BaseModel, Field

class EmailContent(BaseModel):
    subject: str = Field(description="The subject of the email. Should be concise and relevant.")
    body: str = Field(description="The body of the email. Should be well formatted and detailed.")

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='An email generation agent',
    instruction="""
    You are an Email Generation Assistant.
    You write professional emails based on user's request.

    Guidelines:
    - Create a concise and relevant subject line.
    - Write a professional email body with a greeting, clear message, and closing.
    - Ensure proper formatting and grammar.

    IMPORTANT: Respond only in JSON format as per the provided schema.
    {
        "subject": "Email Subject Here",
        "body": "Email body content here."
    }
    """,
    output_schema=EmailContent, # Enforce JSON output
    output_key="email" # The key in the response where the JSON will be found
)
