not_same_object_list = []

while True:
    exit_request = input("Do you want to exit (y/n): ")
    if exit_request.lower() == "y":
        break

    input_list = int(input("Please enter your number: "))
    if input_list not in not_same_object_list:
        not_same_object_list.append(input_list)
        
print(not_same_object_list)
