from pydantic import BaseModel


class BudgetSummary(BaseModel):
    stay_cost: float
    activity_cost: float
    food_cost: float
    transport_cost: float
    total_cost: float
    remaining_budget: float
    within_budget: bool


def budget_agent(
    stay_cost: float,
    activity_cost: float,
    days: int,
    budget: float,
):
    # Estimated costs for food and local transport
    food_cost = days * 500
    transport_cost = days * 300

    total_cost = (
        stay_cost
        + activity_cost
        + food_cost
        + transport_cost
    )

    remaining_budget = budget - total_cost

    return BudgetSummary(
        stay_cost=stay_cost,
        activity_cost=activity_cost,
        food_cost=food_cost,
        transport_cost=transport_cost,
        total_cost=total_cost,
        remaining_budget=remaining_budget,
        within_budget=total_cost <= budget,
    )
