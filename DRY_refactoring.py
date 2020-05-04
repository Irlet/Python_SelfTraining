
def get_number(request):
    while True:
        try:
            number = float(input(f"Enter {request}: "))
            if number <= 0:
                print("Must be positive")
                continue
            break
        except ValueError:
            print("Must be a number")
    return number


length1 = get_number("the length of the first side of the rectangle")
length2 = get_number("the length of the second side of the rectangle")
print(f"Rectangle area: {round((length1 * length2), 4)}")


"""
while True:
    try:
        length1 = float(input("Enter the length of the first side of the rectangle: "))
        if length1 <= 0:
            print("Must be positive")
            continue
        break
    except ValueError:
        print("Must be a number")
while True:
    try:
        length2 = float(input("Enter the length of the second side of the rectangle: "))
        if length2 <= 0:
            print("Must be positive")
            continue
        break
    except ValueError:
        print("Must be a number")


print(f"Rectangle area: {length1 * length2}")
"""
