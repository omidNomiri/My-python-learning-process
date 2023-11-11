import random

while True:
  dice_number = random.randint(1, 6)
  print("Dice number:", dice_number)

  if dice_number == 6:
    print("You win! You can roll again.")
  else:
    print("Sorry, you lose. Try again.")
    break
