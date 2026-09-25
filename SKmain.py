import time
from dataclasses import dataclass

#dataclass for different accommodation types
@dataclass
class Tier :
    name: str
    description: str
    rating: float
Tiers = {
    "shared": Tier(
        name = "Shared room",
        description = "A room where you will sleep with other people.",
        rating = 1.5
    ),
    "room": Tier(
        name = "Private Room",
        description = "A personal room that doesn't needed to be shared with others.",
        rating = 3.5
    ),
    "unit": Tier(
        name = "Entire housing unit",
        description = "A housing unit (e.g: an apartment or a bangalow) contains multiple private rooms.\n "
                      "You will not need to share with others too",
        rating = 5.0

    )
}

#----Rules-----
#map minimum budget tier requirements to number of people
Rules = {
    "low":  (1, 2),
    "mid":  (1, None),
    "high": (1, None),
}

#Map budget tiers to accommodation tiers
Tier_map = {
    "low":  Tiers["shared"],
    "mid":  Tiers["room"],
    "high": Tiers["unit"]
}

#=================Budget Logic==================
def classify_budget(budget: float):
    if budget <= 100:
        return "low"
    elif budget <= 250:
        return "mid"
    else :
        return "high"

def suitable_tier(total_people, budget):
    budget_tier = classify_budget(budget)
    bounds = Rules.get(budget_tier)
    if bounds == None:
        return None

    min_people, max_people = bounds
    if total_people < min_people :
        return None
    if max_people is not None and total_people > max_people :
        return None

    return Tier_map[budget_tier]


#Input code
def user_input():
    while True:
        try:
            total_people = int(input('How many people are going on the trip? '))
            budget = float(input("What's your nightly budget for accommodation (in RM)? "))
        except ValueError:
            print('️️⚠️ Please enter a valid numerical number.')
            continue

        if budget <= 0:
            print("⚠️  Budget must be greater than 0.")
            continue
        if total_people < 1:
            print("⚠️  Party size must be at least 1.")
            continue

        return total_people, budget


#Output code
def show_recommendation(tier):
    print()
    if tier is None:
        print("😕 No matching tier found.")
        print("Try adjusting your budget or number of people.")
        return

    print(f"Recommended: {tier.name}")
    print(f"{tier.description}")
    print(f"Rating: {tier.rating}/5.0")

#============RUNNING=================
print('Welcome to Airbnb filter! \n'
      'A place where we will recommend suitable tier of accommodation\n'
      'based on your budget and number of people on your trip!')
time.sleep(1)
total_people, budget = user_input()
time.sleep(1)
tier = suitable_tier(total_people, budget)
time.sleep(1)
show_recommendation(tier)
