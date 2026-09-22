import time

print('Hi, Welcome to Airbnb rooms filter!')
time.sleep(1)
print("Are you looking for an Airbnb that's suitable for your upcoming stay?")
time.sleep(1)
Budget = float(input('What is your budget? '))
time.sleep(1)
Guest = int(input('How many rguest are staying over? '))

try:
    if Guest == 1 :
            if Budget < 100:
                 room_type = "Shared room"
                 room_desc = "A single bunk with a shared bathroom"
            elif Budget <= 200:
                 room_type = "Private room"
                 room_desc = "Private room in a shared house with shared common areas"
            elif Budget >= 200:
                 room_type = "Studio"
                 room_desc = "Full private unit with self check in, have private kitchen and bathroom."

    print(f"Room Type = {room_type}")
    print(f"Room Description = {room_desc}")

except:
    print("Please enter the correct numerical value for the questions")