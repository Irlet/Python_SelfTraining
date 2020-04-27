# Ask over text and check: no. of characters, find vowels, every second char., no. of letters in words,
# find indicated character and element

my_text = input("Enter text: ")
number_of_text_char = len(my_text)
my_text_splitted = my_text.split()
vowels = "AaEeIiOoUuYy"
vowels_in_text = []
every_second_char = []

print(f"Number of characters in text: {number_of_text_char}")

for letter in my_text:
    if letter in vowels:
        vowels_in_text.append(letter)
print(f"Vowels in text: {vowels_in_text}")

for i in range(len(my_text)):
    if i % 2 != 0:
        every_second_char.append(my_text[i])
print(f"Every second charakters: {every_second_char}")

print("Number of letters in words: ")
for word in my_text_splitted:
    print(len(word))

char_number_to_find = input("Enter ref. number of character to find: ")
char_find = (my_text[int(char_number_to_find)-1])
print(f"'{char_find}'is the {char_number_to_find}. character")

element_to_find = input("Enter the element to find: ")
if element_to_find in my_text:
    print("Contain entered element")
else:
    print("Doesn't contain entered element")
