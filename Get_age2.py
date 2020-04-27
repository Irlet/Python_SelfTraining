# extracts a number from the text


def get_age(text):

    str_list = text.split()
    for element in str_list:
        if element.isdigit():
            print(int(element))
            return(int(element))


get_age("I'm 7 years old")
get_age("I'm 9")
