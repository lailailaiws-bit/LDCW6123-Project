while True:
    try:
        Guest = int(input('How many guest are staying over? '))
        if Guest > 0:
            break
        print("Please enter the correct numerical value to proceed")
    except:
         print("NO")

while True:
    try:
        Budget = float(input('What is the budget for your stay? '))
        if Budget > 0:
            break
        print("Please enter the correct numerical value to proceed")
    except:
         print("NO")

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

print()
print(f"Room Type = {room_type}")
print(f"Room Description = {room_desc}")
