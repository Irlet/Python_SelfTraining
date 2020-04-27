""" The Arara are an isolated tribe found in the Amazon who count in pairs. 
For example one to eight is as follows:

1 = anane
2 = adak
3 = adak anane
4 = adak adak
5 = adak adak anane
6 = adak adak adak
7 = adak adak adak anane
8 = adak adak adak adak

Take a given number and return the Arara's equivalent.

e.g.

count_arara(3) # -> 'adak anane'

count_arara(8) # -> 'adak adak adak adak' """


def count_arara(n):
    if n == 1:
        arara_numbers = "anane"
    elif n % 2 == 0:
        arara_numbers = "adak "*int(n/2)
    else:
        arara_numbers = ("adak "*int((n-1)/2) + "anane")

    return arara_numbers.rstrip()


print(count_arara(2))
print(count_arara(8))
print(count_arara(9))
print(count_arara(12))
print(count_arara(28))
