from app.budget_agent import budget_agent


result = budget_agent(
    stay_cost=5600,
    activity_cost=3450,
    days=3,
    budget=15000
)

print(result)
