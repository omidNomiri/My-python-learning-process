snake_length = int(input("Enter the length of the snake: "))
    
for i in range(snake_length):
    if i % 2 == 0:
            print("*", end="")
    else:
            print("#", end="")
