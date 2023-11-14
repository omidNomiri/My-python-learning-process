def print_diamond(number):
    for i in range(number):
        print(' ' * (number - i - 1), end='')
        print('*' * (2 * i + 1))

    for i in range(number - 2, -1, -1):
        print(' ' * (number - i - 1), end='')
        print('*' * (2 * i + 1))

print_diamond(int(input("Please ener your number: ")))
