# Project:  ©Shiny Paint Calculator
# Editor: Kevin Wong


# computeRectangleArea
def computeRectangleArea(length, width):
    return int(length * width)


# computeRectangleWallsArea
def computeRectangleWallsArea():
    length = float(input("Enter the length of the room in feet: "))
    width = float(input("Enter the width of the room in feet: "))
    height = float(input("Enter the height of the room in feet: "))
    total_area = 2 * (length * (height + width))
    return int(total_area)


# computeSquareArea
def computeSquareArea(side_length):
    return int(side_length * side_length)


# computeSquareWallsArea
def computeSquareWallsArea():
    side_length = float(input("Enter the side length of the room in feet: "))
    return int(side_length * side_length * 4)


# computeCustomWallsArea
def computeCustomWallsArea():
    walls_qty = int(input("How many walls are there in the room: "))
    custom_area = 0

    for i in range(walls_qty):
        custom_length = float(input(f"Enter the length of wall {i+1} in feet: "))
        custom_width = float(input(f"Enter the width of wall {i+1} in feet: "))
        custom_area += int(custom_length * custom_width)
    return custom_area


# computeWindowsDoorsArea
def computeWindowsDoorsArea():
    wd_qty = int(input("How many windows or doors are there in the room: "))
    wd_area = 0

    for i in range(wd_qty):
        wd_length = float(input(f"Enter the length of window/door {i+1} in feet: "))
        wd_width = float(input(f"Enter the width of window/door {i+1} in feet: "))
        wd_area += int(wd_length * wd_width)
    return wd_area


# computeGallons
def computeGallons(paint_area, sqft_per_gallon):
    sqft_per_gallon = 350
    if sqft_per_gallon == 0:
        return None
    return int(paint_area / sqft_per_gallon)


# computePaintPrice
def computePaintPrice(paint_area, paint_price_per_gallon):
    paint_price_per_gallon = 42
    return int(paint_area * paint_price_per_gallon)


# computeRoomArea
def computeRoomArea(room_number):
    print("Room:", room_number)
    print("Select the shape of the room:")
    print("1 - Rectangle")
    print("2 - Square")
    print("3 - Custom")
    room_number = int(input("Enter your option: "))

    if room_number == 1:
        room_area = computeRectangleWallsArea()
    elif room_number == 2:
        room_area = computeSquareWallsArea()
    elif room_number == 3:
        room_area = computeCustomWallsArea()
    else:
        print("Invalid option. Please select a valid shape.")
        return room_number(int(input()))

    wd_area = computeWindowsDoorsArea()
    room_area -= wd_area

    sqft_per_gallon = 350  # Assuming 1 gallon can cover 350 sqft
    paint_price_per_gallon = 42  # Assuming the cost of 1 gallon is $42
    gallons_needed = computeGallons(room_area, sqft_per_gallon)
    total_cost = computePaintPrice(room_area, paint_price_per_gallon)

    print("Area to be painted is", room_area, "ft^2.")
    print("This will require", gallons_needed, "gallons of paint.")
    print("The cost to paint the room is $" + str(total_cost))


# Get the number of rooms from the user
print("Welcome to Shiny Paint Company Limited for painting service!")

while True:
    try:
        num_rooms = int(input("How many rooms do you want to paint: "))
        # If the input is an integer, break out of the loop
        break
    except ValueError:
        # If the input is not an integer, display an error message and ask for input again
        print("Invalid input! Please enter a valid number of rooms.")

print("Thank you!")

# Loop through each room and call the computeRoomArea function
for room_number in range(1, num_rooms + 1):
    computeRoomArea(room_number)


while True:
    try:
        ValueError(computeCustomWallsArea())
        break
    except NotImplementedError:
        print("Test not good")
