from app.activity_agent import activity_agent

result = activity_agent(
    destination="Goa",
    interests="beaches, food and sightseeing",
    days=3
)

for activity in result.activities:
    print(activity)
