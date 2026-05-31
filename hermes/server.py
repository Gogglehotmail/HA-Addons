from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Hermes running"}

@app.post("/api/chat")
def chat(data: dict):
    message = data.get("message", "")
    return {
        "response": f"Received: {message}"
    }