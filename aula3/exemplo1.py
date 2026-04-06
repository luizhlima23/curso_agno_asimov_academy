from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Agno API",
    description="API de IA",
    version="1.0.0",    
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}  

@app.get("/hello/{name}")
def read_hello(name: str):
    return {"message": f"Hello {name}"}   

if __name__ == "__main__":
    uvicorn.run("exemplo1:app", host="0.0.0.0", port=8000, reload=True) 

