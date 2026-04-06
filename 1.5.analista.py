from agno.agent  import Agent
#from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from agno.db.mysql import MySQLDb
from agno.models.openai import OpenAIChat

db = MySQLDb(db_url="mysql+pymysql://root:root@localhost:3306/agno")


from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    session_id="analista_financeiro",
    user_id="user_1",
    name="Analista Financeiro",
    model=OpenAIChat(id="gpt-5-nano"),
    tools=[YFinanceTools()],
    instructions="Você é um analista e tem diferentes clientes. Lembre-se de cada cliente, suas informações e preferências.",
    add_history_to_context=True,
    db=db,
    num_history_runs=3,
    enable_user_memories=True,
    add_memories_to_context=True,
    enable_agentic_memory=True
)
#agent.print_response("Ola, prefiro as respostas em formato de tabelas, gosto de poucas informações",session_id="petrobras_session_1",user_id="analista_petrobras")
#agent.print_response("Ola, prefiro as respostas em formato de texto, gosto de muitas informações",session_id="vale_session_1",user_id="analista_vale")


agent.print_response("Qual qual a cotação da petrobras?",session_id="petrobras_session_2",user_id="analista_petrobras")
agent.print_response("Qual qual a cotação da vale?",session_id="vale_session_2",user_id="analista_vale")

#agent.print_response("Quais empresas já consultamos a cotação?",session_id="petrobras_session",user_id="analista_petrobras")