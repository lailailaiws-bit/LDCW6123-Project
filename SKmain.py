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
    if budget < 100:
        return "low"
    elif budget <= 250:
        return "medium"
    else :
        return "high"

def recommend_accommodation(total_people, budget):
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


# print('Welcome to Airbnb filter! \n'
#       'A place where we will recommend your suite tier based on your budget!')
def user_input():
    try:
        total_people = float(input('How many people are going on the trip? '))
        budget = float(input("What's your budget for the trip (in RM)? "))
        return total_people , budget
    except ValueError:
        print('Please enter a valid numerical number.')
        user_input()

test = user_input()
answer = recommend_accommodation(test[0], test[1])
print(answer)