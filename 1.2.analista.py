from agno.agent  import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools


from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools()],
    instructions="use tabelas para mostrar a informação final. Não inclua nenhum outro texto."
)
agent.print_response("Qual qual a cotação da ação da Apple (AAPL) hoje?", stream=True)