# Execução dos aplicativos — TP2 LangChain

O repositório contém três aplicativos independentes: respostas simuladas com LangChain e `FakeListLLM` (`questao_1`), tradução do inglês para o francês com OpenAI (`questao_2`) e tradução do inglês para o alemão com Helsinki-NLP e LangChain (`questao_3`).

## Clonando o repositório

Para baixar o projeto localmente, abra o terminal na pasta onde deseja armazená-lo e execute:

```powershell
git clone https://github.com/alvicellos/tp_2_lang
cd tp2_fast_api
```

Após acessar a pasta do projeto, siga as instruções de instalação abaixo.

## 1. Instalação

Na raiz do repositório, crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No Prompt de Comando do Windows, a ativação é feita com `.venv\Scripts\activate.bat`; no Linux/macOS, com `source .venv/bin/activate`.

Instale as dependências a partir do arquivo `requirements.txt` na raiz:

```powershell
python -m pip install -r requirements.txt
```

Na primeira execução da questão 3, o modelo e o tokenizer poderão ser baixados do Hugging Face; é necessária conexão com a internet para esse download.

## 2. Questão 1 — Respostas simuladas (LangChain + FakeListLLM)

No terminal com o ambiente ativado, acesse a pasta e inicie a API:

```powershell
cd questao_1
python -m uvicorn main:app --reload
```
A rota `/prompt_fake` aceita uma das três perguntas predefinidas: `O que é inteligência artificial?`, `O que é Machine Learning?` ou `O que é Deep Learning?`.

Acesse a documentação interativa (Swagger UI) em: http://127.0.0.1:8000/docs

## 3. Questão 2 — Tradução (LangChain + OpenAI)

Encerre o servidor anterior com `Ctrl+C`. A partir da raiz do repositório, configure a chave de acesso à API da OpenAI em um arquivo `.env` dentro de `questao_2`:

```dotenv
OPENAI_API_KEY=sua_chave_aqui
```

**Não envie o arquivo `.env` ao GitHub.** É necessário possuir uma chave válida e acesso à API da OpenAI, cujo uso pode gerar cobranças.

Acesse a pasta e inicie a API:

```powershell
cd questao_2
python -m uvicorn main:app --reload
```
Acesse a documentação interativa (Swagger UI) em: http://127.0.0.1:8000/docs

## 4. Questão 3 — Tradução (LangChain + Hugging Face)

Encerre o servidor anterior com `Ctrl+C`. A partir da raiz do repositório, acesse a pasta e inicie a API:

```powershell
cd questao_3
python -m uvicorn main:app --reload
```
Acesse a documentação interativa (Swagger UI) em: http://127.0.0.1:8000/docs

## 5. Observações

- Execute cada servidor a partir da pasta de sua respectiva questão, para que os imports locais sejam encontrados.
- Os exemplos utilizam a porta **8000**; execute apenas um servidor por vez nessa porta.
- Se aparecer erro de conexão, verifique se o servidor está em execução antes de fazer a requisição.
- Na execução da questão 2, confira se a chave `OPENAI_API_KEY` foi configurada corretamente.
- No Windows, caso não consiga ativar o ambiente, utilize o executável `..\.venv\Scripts\python.exe` dentro de cada pasta no lugar de `python`.