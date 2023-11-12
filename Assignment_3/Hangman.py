import random

word_bank = ["tree","bank","alarm","clock","book"]
user_mistake = 0
good_char = []
wrong_char = []

random_word = random.randint(0, len(word_bank)-1)
word = word_bank[random_word]

while user_mistake < 6:
    if set(good_char) == set(word):
        print("You win!")
        break
    
    for i in range(len(word)):
        if word[i] in good_char:
            print(word[i], end=" ") 
        else:
            print('_', end=" ")
            
    user_char = input("Please enter your guess: ")
    if len(user_char) == 1:
        if user_char.lower() in word:
            good_char.append(user_char)
            print("correct word")
        else:
            wrong_char.append(user_char)        
            user_mistake =+ 1
            print("Wrong word")
    else:
        print("Please enter one character")

if user_mistake == 6:
    print("You lose")