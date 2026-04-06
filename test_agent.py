from agno.os import AgentOS
from agno.agent import Agent
#from agno.models.groq import Groq   
from agno.models.openai import OpenAIChat


import os
from dotenv import load_dotenv
load_dotenv()   

assistant = Agent(
    name="Agno Assistant",
    model=OpenAIChat(id="gpt-5-nano"),
    instructions="you are a helpful AI assistant.",
    markdown=True,
    debug_mode=True
)

agent_os = AgentOS(
    name="My AgentOS",
    description="My AgentOS is a helpful AI assistant.",
    agents=[assistant]
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="test_agent:app", reload=True)