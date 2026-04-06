from agno.agent  import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.db.mysql import MySQLDb

db = MySQLDb(db_url="mysql+pymysql://root:root@localhost:3306/agno")


from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    session_id="analista_financeiro",
    user_id="user_1",
    name="Analista Financeiro",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools()],
    instructions="use tabelas para mostrar a informação final. Não inclua nenhum outro texto.",
    add_history_to_context=True,
    db=db,
    num_history_runs=3
)
agent.print_response("Qual qual a cotação da petrobras?",session_id="petrobras_session",user_id="analista_petrobras")
agent.print_response("Qual qual a cotação da vale?",session_id="vale_session",user_id="analista_vale")
agent.print_response("Quais empresas já consultamos a cotação?",session_id="petrobras_session",user_id="analista_petrobras")