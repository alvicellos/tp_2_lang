from fastapi import FastAPI
from models import traduzir_texto_open

app = FastAPI()
@app.get("/translate_open")

def traduzir(prompt_user: str):
    texto_traduzido = traduzir_texto_open(prompt_user)
    return {"traducao": texto_traduzido}