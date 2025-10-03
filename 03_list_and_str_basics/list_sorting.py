user_numbers = []

while True:
    exit_request = input("Do you want to exit (y/n): ")
    if exit_request.lower() == "y":
        break

    user_input = input("Please enter a number: ")
    number = int(user_input)
    user_numbers.append(number)
    print("Number added.")

is_sorted = sorted(user_numbers)

if is_sorted == user_numbers:
    print("The list is sorted.")
    print(user_numbers)
else:
    print(user_numbers)
    print("The list is not sorted.")
