from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os
import requests

load_dotenv()

OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok", "message": "OpenRouter agent is live!"}


@app.post("/retell-webhook")
async def retell_webhook(request: Request):
    """Endpoint que recibe mensajes desde Retell y responde usando OpenRouter"""
    data = await request.json()
    user_message = data.get("message", "")

    payload = {
        "model": "gpt-4o-mini",  
        "messages": [
            {"role": "system", "content": "You are a friendly real estate assistant."},
            {"role": "user", "content": user_message},
        ],
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json",
    }

    response = requests.post(OPENROUTER_URL, json=payload, headers=headers).json()

    reply = response["choices"][0]["message"]["content"].strip()

    return {"response": reply}
