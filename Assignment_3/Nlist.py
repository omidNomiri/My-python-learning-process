import random

length_user_list = int(input("Please enter your length: "))

numbers = list(range(length_user_list))
random.shuffle(numbers)

list_user_want = []

for n in numbers:
    if n not in list_user_want:
        list_user_want.append(n)


print(list_user_want)

    