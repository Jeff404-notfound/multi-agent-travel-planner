from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import ChatOllama

app = FastAPI()

llm = ChatOllama(
    model="qwen3:4b",
    base_url="http://172.30.48.1:11434",
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {
        "message": "Multi-Agent Travel Planner API is running"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    response = llm.invoke(request.message)

    return {
        "response": response.content
    }
