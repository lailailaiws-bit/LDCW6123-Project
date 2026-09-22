import time

print('Hi, Welcome to Airbnb rooms filter!')
time.sleep(1)
print("Are you looking for an Airbnb that's suitable for your upcoming stay?")
time.sleep(1)
while True:
    try:
        Guest = int(input('How many guest are staying over? '))
        if Guest > 0:
            break
        print("Please enter the correct numerical value to proceed")
    except:
         print("NO")
time.sleep(1)
while True:
    try:
        Budget = float(input('What is the budget for your stay? '))
        if Budget > 0:
            break
        print("Please enter the correct numerical value to proceed")
    except:
         print("NO")

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

    elif 2 <= Guest <= 3:
        if Budget < 150:
             room_type = "Beds in Shared room"
             room_desc = "2 to 3 beds in a co-living flat"
        elif Budget <= 250:
             room_type = "Private Master Bedroom"
             room_desc = "A large room with Queen/King size bed and an attached bathroom"
        elif Budget <= 500:
             room_type = "Entire 1 to 2 Bedroom unit"
             room_desc = "A complete private condominium with a living room, kitchen, gym, and pool access."
        elif Budget <= 500:
             room_type = "Private Suite"
             room_desc = "Comes with high-floor view, designer interior, and fitted with premium building amentities"
             
         
    print()
    print(f"Room Type = {room_type}")
    print(f"Room Description = {room_desc}")

except:
    print("Please enter the correct numerical value for the questions")