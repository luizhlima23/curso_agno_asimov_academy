#---------------------------------------------------------
#conta corrente bancária - FastApi
#Gerenciar saques e depositos de clientes
#---------------------------------------------------------

#imports
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field

app = FastAPI(
    title="Conta Corrente",
    description="API de conta corrente",
    version="1.0.0",
)

#---------------------------------------------------------
#Adicionar clientes

db_clientes={
    "Joao":0,
    "Maria":0,
    "Pedro":0,
}

#---------------------------------------------------------
#Criar endpoint para Home
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Conta Corrente"}


#criar classe para as movimentações (saques e depósitos) OBS: usar pydantic (para não acontecer erros)

class Movimentacao(BaseModel):
    cliente: str = Field(..., description="Nome do cliente")
    valor: float = Field(...,gt=0, description="Valor da movimentação")

#---------------------------------------------------------
#Criar endpoint para consultar o saldo

@app.post("/saldo")
def saldo(cliente: str):
    return {"saldo do cliente é": db_clientes[cliente]}

#---------------------------------------------------------
#Criar endpoint para realizar saques 

@app.post("/saque")
def saque(movimentacao: Movimentacao):
    db_clientes[movimentacao.cliente] -= movimentacao.valor
    return {"mensagem": {"cliente": movimentacao.cliente, "valor_movimentacao": movimentacao.valor, "saldo_atual": db_clientes[movimentacao.cliente]}}
        
#---------------------------------------------------------
#Criar endpoint para realizar depositos
@app.post("/deposito")
def deposito(movimentacao: Movimentacao):
    db_clientes[movimentacao.cliente] += movimentacao.valor
    return {"mensagem": {"cliente": movimentacao.cliente, "valor_movimentacao": +movimentacao.valor, "saldo_atual": db_clientes[movimentacao.cliente]}}


#run
if __name__ == "__main__":
    uvicorn.run("exemplo2:app", host="0.0.0.0", port=8000, reload=True)