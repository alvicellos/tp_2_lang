from fastapi import APIRouter
from models import gerar_explicacao, perguntas

router = APIRouter()

@router.get("/prompt_fake")
async def responder_fake(prompt: perguntas):
    resposta = gerar_explicacao(prompt)
    return {"resposta": resposta}