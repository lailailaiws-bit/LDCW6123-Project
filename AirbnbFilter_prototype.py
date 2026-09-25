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
        time.sleep(0.5)
        print("Please enter the correct numerical value to proceed")
    except:
         print("NO")
time.sleep(1)
while True:
    try:
        Budget = float(input('What is the budget for your stay? '))
        if Budget > 0:
            break
        time.sleep(0.5)
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

    elif 4 <= Guest <= 6:
        if Budget < 250:
            room_type = "Family Hostel"
            room_desc = "Single large shared room with 4 to 6 bunk beds."
        elif Budget <= 600:
            room_type = "3 Bedroom Condominium"
            room_desc = "A condominium fitted with 3 separate bedrooms, 2 bathrooms, a dining area, and a kitchen."
        elif Budget <= 1200:
            room_type = "Entire landed House"     
            room_desc = "Double-storey terrace or landed house with private parking and patio."
        elif Budget > 1200:
            room_type = "Penthouse"
            room_desc = "Dedicated private pool, spacious common areas, entertainment amenities."

    elif Guest > 6:
        if Budget < 500:
            room_type = "Group Dorm"
            room_desc = "Multiple shared dorm rooms"
        elif Budget <= 1000:
            room_type = "Entire Landed Homestay"
            room_desc = "Spacious landed house with 4 to 5, fitted with a barbecue area, multiple bathrooms, and a yard."
        elif Budget > 1000:
            room_type = "Luxury Villa"
            room_desc = "Gated private bungalow, pool, outdoor dining, and multiple luxury living spaces."

    time.sleep(1)
    print()
    print(f"Room Type = {room_type}")
    time.sleep(0.5)
    print(f"Room Description = {room_desc}")
    print()

except:
    print("Please enter the correct numerical value for the questions")