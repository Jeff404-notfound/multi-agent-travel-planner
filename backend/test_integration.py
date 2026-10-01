from app.activity_agent import activity_agent
from app.stay_agent import stay_agent
from app.budget_agent import budget_agent


# 1. Get activities
activities = activity_agent(
    destination="Goa",
    interests="beaches, food and sightseeing",
    days=3
)

# Calculate total activity cost
activity_cost = sum(
    activity.estimated_cost
    for activity in activities.activities
)


# 2. Get accommodation options
stays = stay_agent(
    destination="Goa",
    days=3,
    travelers=2
)

# For now, select the first stay option
selected_stay = stays.stays[0]


# 3. Send actual results to Budget Agent
budget = budget_agent(
    stay_cost=selected_stay.total_cost,
    activity_cost=activity_cost,
    days=3,
    budget=15000
)


# 4. Display everything
print("\n===== ACTIVITIES =====")
for activity in activities.activities:
    print(
        f"{activity.name} - "
        f"₹{activity.estimated_cost}"
    )

print("\n===== SELECTED STAY =====")
print(selected_stay)

print("\n===== BUDGET =====")
print(budget)
