while True:
    print("Welcome to the elevator")
    floor_select = int(input("Please select floor 1-10:  "))
    current_floor = int(input("Enter the current floor: "))
    if floor_select==current_floor:
        print("Your have arrived {} floor". format(floor_select))
    while floor_select > current_floor:
        print("Elevator is going up and you are currently on the floor number {}".format(current_floor))
        current_floor += 1
        if floor_select == current_floor:
            print("Your have arrived the floor number {}".format(floor_select))
            break
    while floor_select < current_floor:
        print("Elevator is going down and you are currently on the floor number {}".format(current_floor))
        current_floor -= 1
        if floor_select == current_floor:
            print("Your have arrived  the floor number {}".format(floor_select))
            break

