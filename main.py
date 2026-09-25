import time
from dataclasses import dataclass

#What is a dataclass

#dataclass is a blueprint for objects that has same attributes
#classes' main job is holding attributes for objects
#dataclass is just a more efficient way to store objects that have the same attributes
#an attribute is a characteristic, property, or piece of metadata that describes or modifies a specific element.

#dataclass for different accommodation types
@dataclass
class Tier :
#declare the attributes' type
    name: str
    description: str
    rating: float

#assign different value for different objects on all attributes
#Tier is a class holding up an attributes for an object
#while Tiers is a dictionary, holding up all the objects, it acts as a shelf organising the objects nicely

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
#a dictionary that maps minimum budget tier requirements to number of people
Rules = {
    "low":  (1, 2),
    "mid":  (1, None),
    "high": (1, None),
}

#A dictionary that maps budget tiers to accommodation tiers
Tier_map = {
    "low":  Tiers["shared"],
    "mid":  Tiers["room"],
    "high": Tiers["unit"]
}

#=================Budget Logic==================
#for our budget logic, we'll classify budget amount into "low", "mid" & "high"
#we are able to achieve that with classify_budget function
#next, we'll use suitable_tier to find the suitable tier of accommodation for users.
#suitable_tier will filter the maximum people that'll suite for the budget to work by using Rules dictionary
#and use Tier_map dictionary to recommend the suitable tier of accommodation

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
    if max_people is not None and total_people > max_people :
        return None

    return Tier_map[budget_tier]


#Input code
#this part is the input codes where it'll get user's input
#if users type invalid values, it will loop until users type in valid answers

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
#print out recommended tier of accommodation for user

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
#codes where it allows the program to run

print('Welcome to Airbnb filter! \n'
      'A place where we will recommend suitable tier of accommodation\n'
      'based on your budget and number of people on your trip!')
time.sleep(1)
total_people, budget = user_input()
time.sleep(1)
tier = suitable_tier(total_people, budget)
time.sleep(1)
show_recommendation(tier)
