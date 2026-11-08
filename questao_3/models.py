from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain_huggingface import HuggingFacePipeline
import torch

def pipeline_langchain():
    modelo = "Helsinki-NLP/opus-mt-en-de"
    tokenizer = AutoTokenizer.from_pretrained(modelo, clean_up_tokenization_spaces=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(modelo)
    
    device = 0 if torch.cuda.is_available() else -1

    pipe = pipeline(
        "translation",
        model=model,
        tokenizer=tokenizer,
        device=device,    
        max_new_tokens=100,    
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    chain = llm
    return chain

modelo_carregado = pipeline_langchain()

def generate_text(texto) -> str:
    return modelo_carregado.invoke(texto)