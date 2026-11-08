from langchain_core.prompts import PromptTemplate
from langchain_core.language_models.fake import FakeListLLM
from typing import Literal

fake_llm = FakeListLLM(
    responses=[
        "Inteligência Artificial é a área da computação que desenvolve sistemas capazes de realizar tarefas que normalmente exigem inteligência humana, como reconhecer padrões e tomar decisões.",
        "Machine Learning é uma subárea da Inteligência Artificial que permite aos sistemas aprender padrões a partir de dados, sem precisar de regras explicitamente programadas para cada situação.",
        "Deep Learning é uma subárea do Machine Learning que utiliza redes neurais com múltiplas camadas para aprender padrões complexos, sendo aplicada em imagens, linguagem natural e reconhecimento de voz."
    ]
)

perguntas = Literal[
    "O que é inteligência artificial?",
    "O que é Machine Learning?",
    "O que é Deep Learning?"
]

prompt = PromptTemplate.from_template(
    "Explique {assunto} de forma resumida."
)

chain = prompt | fake_llm

def gerar_explicacao(assunto: str) -> str:
    resposta = chain.invoke({"assunto": assunto})
    return resposta