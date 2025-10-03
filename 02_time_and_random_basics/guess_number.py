import random

random_number = random.randint(1, 100)

how_many_time = 10

for i in range(how_many_time):

    user_guess = int(input("Enter your guess: "))

    if user_guess == random_number:
        print("You win!")
        break

    elif user_guess < random_number:
        print("Your guess is bigger than you think. Try again.")

    elif user_guess > random_number:
        print("Your guess is smaller than you think. Try again.")

print(f"You try {i + 1} time.")
