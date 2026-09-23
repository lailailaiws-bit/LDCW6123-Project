print('Welcome to Airbnb filter! \n'
      'A place where we will recommend your suite tier based on your budget!')
def user_input():
    try:
        Total_people = float(input('How many people are going on the trip? '))
        Budget = float(input("What's your budget for the trip (in RM)? "))
    except ValueError:
        print('Please enter a valid numerical number.')
        user_input()
user_input()