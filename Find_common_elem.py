first_list = [2, 4, 6, 8, "dog", 3.14, 1024]
second_list = [3.14, "cat", "dog", 2, 0, 6]
common_elements = []

for element in first_list:
    if element in second_list:
        common_elements.append(element)
print(common_elements)

# another way (different prezentation on result):
for i in range(len(common_elements)):
    print(f"{i+1} -> {common_elements[i]}")

# another way (creating function):


def get_common_elements(first, second):
    result_list = []

    for element in first:
        if element in second:
            result_list.append(element)
    return result_list


def main():
    first_list2 = ["ogre", -100, 22, 1024]
    second_list2 = [-22, 1024, 0, "Shreck", "ogre", -100]
    print(get_common_elements(first_list2, second_list2))


main()
