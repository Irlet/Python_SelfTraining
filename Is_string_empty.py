def is_string_empty(my_string):
    if not my_string:
        print("Is empty")
    else:
        print("Is not empty")


is_string_empty(input("Enter your text: "))

# another way:


def is_string_empty2(my_string2):
    if my_string2 == "":
        print("Is empty")
    else:
        print("Is not empty")


is_string_empty2(input("Enter your another text: "))
