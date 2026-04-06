from agno.agent  import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq

from dotenv import load_dotenv
load_dotenv()

def celsius_to_fahrenheit(temperatura_celsius: float):
    """
    Converte uma temperatura em graus Celsius para Fahrenheit.

    Args:
        temperatura_celsius (float): A temperatura em graus Celsius.

    Returns:
        float: A temperatura em graus Fahrenheit.
    """
    return (temperatura_celsius * 9/5) + 32
    

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[TavilyTools(),celsius_to_fahrenheit],
    debug_mode=True

)

agent.print_response("Use suas ferramentas para pesquisar a temperatura de hoje em Ituiutaba-MG em fahrenheit")