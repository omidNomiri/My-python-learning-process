import random

def chess_page_output(row: int,column: int):
    chess_list = [[0]*column for _ in range(row)]
    for i in range(row):
        for j in range(column):
            chess_list[i][j]= random.randint(1,9)

    print(chess_list)

chess_page_output(int(input("Please ener your row: ")),int(input("Please ener your column: ")))

