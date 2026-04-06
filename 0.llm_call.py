from agno.models.groq import Groq
from agno.models.message import Message

from dotenv import load_dotenv
load_dotenv()

model = Groq(id="llama-3.3-70b-versatile")
msg = Message(
    role="user", 
    content=[{"type": "text", "text": "Olá, meu nome é Luiz"}]
)
response = model.response([msg])

print(response.content)
