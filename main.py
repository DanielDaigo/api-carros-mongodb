from fastapi import FastAPI
from app.routers.carro_router import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "API de Carros Modular rodando com sucesso!"}