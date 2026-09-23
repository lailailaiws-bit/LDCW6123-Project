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
test = user_input()
print(test)
def accommodation_filter(Total_people, budget):
    if budget < 100:
        budget_tier = "low"
    elif budget <= 250:
        budget_tier = "medium"
    else :
        budget_tier = "high"

