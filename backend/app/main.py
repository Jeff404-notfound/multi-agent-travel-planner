from app.travel_graph import travel_graph

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

class TravelPlanRequest(BaseModel):
    destination: str
    interests: str
    days: int
    travelers: int
    budget: float


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
@app.post("/api/travel/plan")
def create_travel_plan(request: TravelPlanRequest):

    initial_state = {
        "destination": request.destination,
        "interests": request.interests,
        "days": request.days,
        "travelers": request.travelers,
        "budget": request.budget,
    }

    result = travel_graph.invoke(initial_state)

    return {
        "destination": result["destination"],
        "interests": result["interests"],
        "days": result["days"],
        "travelers": result["travelers"],
        "budget": result["budget"],
        "activities": result["activities"],
        "stays": result["stays"],
        "budget_summary": result["budget_summary"],
    }
