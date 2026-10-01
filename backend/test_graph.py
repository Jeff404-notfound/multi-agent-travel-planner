from app.travel_graph import travel_graph


result = travel_graph.invoke(
    {
        "destination": "Goa",
        "interests": "beaches, food and sightseeing",
        "days": 3,
        "travelers": 2,
        "budget": 15000,
    }
)


print("\n===== ACTIVITIES =====")

for activity in result["activities"].activities:
    print(
        f"{activity.name} - "
        f"₹{activity.estimated_cost}"
    )


print("\n===== SELECTED STAY =====")

print(result["stays"].stays[0])


print("\n===== BUDGET SUMMARY =====")

print(result["budget_summary"])
