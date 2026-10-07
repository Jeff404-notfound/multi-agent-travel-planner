from typing import TypedDict

from langgraph.graph import StateGraph, START, END


class TravelState(TypedDict):
    destination: str
    interests: str
    days: int
    travelers: int
    budget: float

    activities: object
    stays: object
    budget_summary: object


def activity_node(state: TravelState):
    from app.activity_agent import activity_agent

    result = activity_agent(
        destination=state["destination"],
        interests=state["interests"],
        days=state["days"],
    )

    return {
        "activities": result
    }


def stay_node(state: TravelState):
    from app.stay_agent import stay_agent

    result = stay_agent(
        destination=state["destination"],
        days=state["days"],
        travelers=state["travelers"],
    )

    return {
        "stays": result
    }


def budget_node(state: TravelState):
    from app.budget_agent import budget_agent

    activity_cost = sum(
        activity.estimated_cost
        for activity in state["activities"].activities
    )

    selected_stay = min(
    state["stays"].stays,
    key=lambda stay: stay.total_cost
    )

    result = budget_agent(
        stay_cost=selected_stay.total_cost,
        activity_cost=activity_cost,
        days=state["days"],
        budget=state["budget"],
    )

    return {
        "budget_summary": result
    }


graph_builder = StateGraph(TravelState)

graph_builder.add_node("activity", activity_node)
graph_builder.add_node("stay", stay_node)
graph_builder.add_node("budget", budget_node)

graph_builder.add_edge(START, "activity")
graph_builder.add_edge("activity", "stay")
graph_builder.add_edge("stay", "budget")
graph_builder.add_edge("budget", END)

travel_graph = graph_builder.compile()
