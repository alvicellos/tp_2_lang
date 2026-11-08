import requests
import sys

def traduzir(texto):
    resposta = requests.get(
        "http://127.0.0.1:8000/translate",
        params={"prompt": texto}
    )
    return resposta.json()['message_translated']

if __name__ == "__main__" and sys.argv[1] != None :
    texto = sys.argv[1]
    print(traduzir(texto))
    
    