def even_or_odd(number):
    try:
        number_int = int(number)
    except ValueError:
        print("Must be an integer number")
        return

    if number_int == 0:
        print("Must be defferent from zero")
    elif number_int % 2 == 0:
        print(f"Number {number_int} is even")
    else:
        print(f"Number {number_int} is odd")


even_or_odd(input("Enter number to check: "))
