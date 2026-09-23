from dataclasses import dataclass

@dataclass
class Tier :
    name: str
    description: str
    rating: float
Tiers = {
    Tier(
        name = "Shared room",
        description = "A room where you will sleep with other people.",
        rating = 1.5
    ),
    Tier(
        name = "Private Room",
        description = "A personal room that doesn't needed to be shared with others.",
        rating = 3.5
    ),
    Tier(
        name = "Entire housing unit",
        description = "A housing unit (e.g: an apartment or a bangalow) contains multiple private rooms.\n "
                      "You will not need to share with others too",
        rating = 5.0

    )
}



print('Welcome to Airbnb filter! \n'
      'A place where we will recommend your suite tier based on your budget!')
def user_input():
    try:
        Total_people = float(input('How many people are going on the trip? '))
        budget = float(input("What's your budget for the trip (in RM)? "))
        return Total_people, budget
    except ValueError:
        print('Please enter a valid numerical number.')
        user_input()


def classify_budget(Total_people, budget):
    if budget < 100:
        budget_tier = "low"
    elif budget <= 250:
        budget_tier = "medium"
    else :
        budget_tier = "high"

