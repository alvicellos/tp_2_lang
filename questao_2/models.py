from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

template = ChatPromptTemplate.from_messages([
    ("system", "You are an English to French translator."),
    ("user", "Translate this to French: {text}")
])

chain = template | llm

def traduzir_texto_open(prompt: str) -> str:
    response = chain.invoke({"text": prompt})
    return response.content