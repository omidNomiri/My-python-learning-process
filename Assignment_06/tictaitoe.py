import pyfiglet
from colorama import Fore
import time
import random

start_time = time.time()

def show():
    for row in game_page:
        for cell in row:
            print(cell,end=" ")
        print()

def check_winner():
    for i in range(3):
        if game_page[i][0]== game_page[i][1]== game_page[i][2] != "-":
            if game_page[i][0]== "X":
                print("Player1 win")
            else:
                print("Player2 win")
        if game_page[0][i]== game_page[1][i]== game_page[2][i] != "-":
            if game_page[i][0]== "X":
                print("Player1 win")
            else:
                print("Player2 win")

    if game_page[0][0]== game_page[1][1]== game_page[2][2]== "X":
        print("Player1 win")
    if game_page[0][2]== game_page[1][1]== game_page[2][0]== "X":
        print("Player1 win")
    if game_page[0][0]== game_page[1][1]== game_page[2][2]== "O":
        print("Player2 win")
    if game_page[0][2]== game_page[1][1]== game_page[2][0]== "O":  
        print("Player2 win")
    if "-" not in game_page[0] and "-" not in game_page[1] and "-" not in game_page[2]:
        print("Equal!")

title = pyfiglet.figlet_format("Tic Tai toe", font="slant")
print(title)

game_page = [["-","-","-"],
             ["-","-","-"],
             ["-","-","-"]]

game_mode = int(input("If you want player vs cpu enter number 1 and for player vs player enter number 2: "))

show()
if game_mode == 1:
    while True:
        print("Player 1")
        while True:
            row = int(input("Your target row:"))
            column = int(input("Your target column:"))

            if row >= 0 and row <= 2 and column >= 0 and column <= 2:

                if game_page[row][column] == "-":
                    game_page[row][column] = Fore.BLUE + "X" + Fore.RESET
                    break

                else:
                    print("Don,t cheat")

            else:
                print("Please enter your row and column between 0 and 2")

        show()
        print("CPU")
        check_winner()
        while True:
            row = random.randint(0,2)
            column = random.randint(0,2)

            if game_page[row][column] == "-":
                game_page[row][column] = Fore.RED + "O" + Fore.RESET
                break

        show()
        print("CPU")


elif game_mode == 2:
    while True:
        print("Player 1")

        while True:
            row = int(input("Your target row:"))
            column = int(input("Your target column:"))

            if row >= 0 and row <= 2 and column >= 0 and column <= 2:

                if game_page[row][column] == "-":
                    game_page[row][column] = Fore.BLUE + "X" + Fore.RESET
                    break

                else:
                    print("Don,t cheat")

            else:
                print("Please enter your row and column between 0 and 2")

        show()
        print("Player 2")
        check_winner()

        while True:
            row = int(input("Your target row:"))
            column = int(input("Your target column:"))

            if row >= 0 and row <= 2 and column >= 0 and column <= 2:

                if game_page[row][column] == "-":
                    game_page[row][column] = Fore.RED + "O" + Fore.RESET
                    break
                
                else:
                    print("Don,t cheat")

            else:
                print("Please enter your row and column between 0 and 2")
        show()
        check_winner()

end_time = time.time()
print("Time: ", end_time - start_time)
