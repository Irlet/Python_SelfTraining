# extracts an age from the text


def get_age(age):
    # your code here

    year = []
    for word in age.split():
        try:
            year.append(int(word))
        except ValueError:
            pass
    return(year)


print(get_age("I'm 4 years old"))
