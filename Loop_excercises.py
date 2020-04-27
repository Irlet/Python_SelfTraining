my_list = ['I', 'wish', 'You', 'a', 'marry', 'Christmas']


def print_every_element_using_for_loop(my_list):
    for element in my_list:
        print(element)


print_every_element_using_for_loop(my_list)


def print_every_element_using_for_loop_and_indexes(my_list):
    for i in range(len(my_list)):
        print(my_list[i])


print_every_element_using_for_loop_and_indexes(my_list)


def print_every_element_using_while_loop(my_list):
    i = 0
    while i < len(my_list):
        print(my_list[i])
        i += 1


print_every_element_using_while_loop(my_list)
