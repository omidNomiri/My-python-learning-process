import random

options = ["Rock", "Paper", "Scissors"]
computer_score = 0
user_score = 0

while True:

    user_choice = input("Choose Rock, Paper, or Scissors: ")

    computer_choice = random.choice(options)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Check for winner
    if user_choice == computer_choice:
        print("There are equal!")
    
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        user_score += 1
        print("You win!")
    else:
        computer_score += 1
        print("Computer wins!")

    if user_score == 3 or computer_score == 3:
        break

print(f"Your score:", user_score)
print(f"Computer's score:", computer_score)
