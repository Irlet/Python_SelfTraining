# exercise 1
x = ["a", "b", "c", "d"]
y = ["e", "f", "g", "h"]

print(x[:3]+y[:2])

# exercise 2
first_text = "Abcdefgh"
second_text = "Jklmnopq"
len1 = len(first_text)
len2 = len(second_text)


def join_backwards_last_six_letters(first_text, second_text):

    backward_txt1 = []
    backward_txt2 = []

    for i in range(len1):
        backward_txt1.append(first_text[i])
    for i in range(len2):
        backward_txt2.append(second_text[i])
    ''' these two 'for' can be done faster:
    backward_txt1 = list(first_text)
    backward_txt2 = list(second_text) '''
    backward_txt1.reverse()
    backward_txt2.reverse()
    backward_joined = (backward_txt1[:6]) + (backward_txt2[:6])
    return backward_joined


print(join_backwards_last_six_letters(first_text, second_text))  # h,g,f,e,d,c,q,p,o,n,m,l

