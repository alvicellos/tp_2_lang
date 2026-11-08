from fastapi import FastAPI
from models import generate_text

app = FastAPI()
@app.get("/translate")
def serve_language_model_controller(prompt: str):    
    output = generate_text(prompt)
    return {
        "original_message": prompt,
        "message_translated": output
    }    
