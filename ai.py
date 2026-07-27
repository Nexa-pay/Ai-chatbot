import requests
from prompts import SYSTEM_PROMPT

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "qwen2.5:3b"


def load_knowledge():
    try:
        with open("knowledge.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""


def ask_ai(user_message: str) -> str:
    knowledge = load_knowledge()

    prompt = f"""
{SYSTEM_PROMPT}

Knowledge:
{knowledge}

User:
{user_message}

Assistant:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.3,
                "num_predict": 25
            }
        },
        timeout=60,
    )

    response.raise_for_status()

    answer = response.json()["response"].strip()

    # Safety limit: maximum 12 words
    words = answer.split()
    if len(words) > 12:
        answer = " ".join(words[:12])

    return answer
