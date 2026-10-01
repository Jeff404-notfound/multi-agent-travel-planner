from app.stay_agent import stay_agent


result = stay_agent(
    destination="Goa",
    days=3,
    travelers=2
)

for stay in result.stays:
    print(stay)
