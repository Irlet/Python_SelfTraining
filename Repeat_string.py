""" Write a function called repeatString which repeats the given String src exactly count times.

repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello" """


def repeat_str(repeat, string):
    return string * int(repeat)


print(repeat_str(3, 'Mam! '))
