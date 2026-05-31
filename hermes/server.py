from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests

app = FastAPI()

HASS_URL = os.getenv("HASS_URL")
HASS_TOKEN = os.getenv("HASS_TOKEN")


class ChatRequest(BaseModel):
    message: str


@app.post("/api/chat")
def chat(req: ChatRequest):
    text = req.message.lower()

    actions = []

    # SIMPLE TEST LOGIC
    if "light on" in text:
        actions.append(call_service("light", "turn_on", {"entity_id": "light.living_room"}))

    if "light off" in text:
        actions.append(call_service("light", "turn_off", {"entity_id": "light.living_room"}))

    return {
        "response": f"OK: {req.message}",
        "actions": actions
    }


def call_service(domain, service, data):
    if not HASS_URL or not HASS_TOKEN:
        return {"error": "missing config"}

    url = f"{HASS_URL}/api/services/{domain}/{service}"

    headers = {
        "Authorization": f"Bearer {HASS_TOKEN}",
        "Content-Type": "application/json"
    }

    requests.post(url, json=data, headers=headers)

    return {"called": f"{domain}.{service}"}