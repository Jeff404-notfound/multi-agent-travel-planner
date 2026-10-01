from langchain_ollama import ChatOllama
from pydantic import BaseModel
from typing import List


class Activity(BaseModel):
    name: str
    category: str
    duration_hours: float
    estimated_cost: float
    description: str


class ActivityList(BaseModel):
    activities: List[Activity]



llm = ChatOllama(
    model="qwen3:4b",
    base_url="http://172.30.48.1:11434",
    temperature=0,
    num_ctx=4096,
)


structured_llm = llm.with_structured_output(ActivityList)


def activity_agent(destination: str, interests: str, days: int):
    prompt = f"""
You are a travel activity planning agent.

Destination: {destination}
Interests: {interests}
Trip duration: {days} days

Suggest useful tourist activities for this trip.

For each activity provide:
- name
- category
- duration in hours
- estimated cost in INR
- short description

Give realistic approximate costs.
Do not invent live booking availability.
"""

    return structured_llm.invoke(prompt)
