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
    num_ctx=2048,
    reasoning=False,
)


structured_llm = llm.with_structured_output(ActivityList)


def activity_agent(destination: str, interests: str, days: int):
    prompt = f"""
You are a travel activity planning agent.

Destination: {destination}
Interests: {interests}
Trip duration: {days} days

Suggest exactly 4 activities that are relevant to the destination and the user's interests.


Rules:
- Every activity must take place in {destination}.
- Use generic activity names whenever possible.
- Do NOT mention specific businesses, restaurants, hotels, resorts, markets, beaches, islands, cities, or attractions by name.
- Do NOT use locations from another city, state, or country.
- Do NOT suggest flights, trains, buses, hotels, accommodation, or transportation.
- If you are uncertain about a specific location, describe the activity generically instead.
- Use realistic approximate costs in INR.
- Keep descriptions short and factual.
- Do not claim live availability or booking information.

For each activity provide:
- name
- category
- duration in hours
- estimated cost in INR
- short description
"""

    return structured_llm.invoke(prompt)
