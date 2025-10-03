reversed_list = []

while True:
    exit_request = input("Do you want to exit (y/n): ")
    if exit_request.lower() == "y":
        break
    input_list = int(input("Please enter your number: "))
    reversed_list.append(input_list)
    
print(reversed_list[::-1])
