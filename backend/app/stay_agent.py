from langchain_ollama import ChatOllama
from pydantic import BaseModel
from typing import List


class StayOption(BaseModel):
    name: str
    accommodation_type: str
    price_per_night: float
    total_cost: float
    description: str


class StayList(BaseModel):
    stays: List[StayOption]


llm = ChatOllama(
    model="qwen3:4b",
    base_url="http://172.30.48.1:11434",
    temperature=0,
    num_ctx=2048,
    reasoning=False,
)


structured_llm = llm.with_structured_output(StayList)


def stay_agent(destination: str, days: int, travelers: int):
    prompt = f"""
You are a travel accommodation planning agent.

Destination: {destination}
Trip duration: {days} days
Number of travelers: {travelers}

Suggest 3 realistic accommodation options.

For each option provide:
- name
- accommodation type
- estimated price per night in INR
- estimated total cost for the entire stay
- short description

Use approximate prices only.
Do NOT claim these are live booking prices.
Do NOT invent availability.

Calculate total cost based on the trip duration.
"""

    return structured_llm.invoke(prompt)
