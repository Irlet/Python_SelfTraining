# KOCHA-LUBI-SZANUJE


def how_much_i_love_you(nb_petals):
    try:
        nb_petals_int = int(nb_petals)
    except ValueError:
        print("Must be a number")
        return

    love_options = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    set_of_options = len(love_options)
    final_option_index = (nb_petals_int % set_of_options) - 1
    if nb_petals_int > 0:
        print("You get: ")
        print(love_options[final_option_index] + "!")
    else:
        print("The flower must have at least one petal!")
    return love_options[final_option_index]


how_much_i_love_you(input("How many petals are in the flower: "))
