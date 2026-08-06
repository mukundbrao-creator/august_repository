print("=" * 30)
print("Welcome to Ride Builder!")
print("=" * 30)
print()

print("Step 1: Pick your vehicle. ")
print("Option 1: Bike")
print("Option 2: Car")
print()

choice = int(input("Enter 1 or 2: "))
print()

if choice == 1:
    print("Step 2: Pick your bike type.")
    print("1 - Scooty")
    print("2 - Mountain Bike")
    print("3 - Sports Bike")
    print()
    
    bike_type = int(input("Enter 1, 2, or 3: "))
    print()
    if bike_type == 1:
        print("You picked: Scooty")
        print("Top speed: 80km/h")
        print("Best for: City Roads")
    elif bike_type == 2:
        print("You picked: Mountain Bike")
        print("Top speed: 40km/h")
        print("Best for: Off-road trails")
    elif bike_type == 3:
        print("You picked: Sports Bike")
        print("Top speed: 200km/h")
        print("Best for: Racing")
    else:
        print("That was not a valid choice.")
        print("Please pick 1, 2, or 3.")
elif choice == 2:
    print("Step 2: Pick your car type. ")
    print("1 - Sedan")
    print("2 - SUV")
    print("3 - Hatchback")
    print()

    car_type = int(input("Pick 1, 2, or 3: "))
    if car_type == 1:
        print("You picked: Sedan")
        print("Seats: 5")
        print("Best for: Family trips")
    elif car_type == 2:
        print("You picked: SUV")
        print("Seats: 7")
        print("Best for: Offroad Adventures")
    elif car_type == 3:
        print("You picked: Hatchback")
        print("Seats: 4")
        print("Best for: Small errands with car")
    else:
        print("That was not a valid choice.")
        print("Please pick 1, 2, or 3.")
else: 
    print("That was not a valid choice.")
    print("Please enter 1 for Bike or 2 for Car.")

print()
print("=" * 30)
print("Your custom ride is ready! ")
print("Enjoy your journey!")
print("=" * 30)