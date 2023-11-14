def chess_page_output(row: int,column: int):
    for i in range(row):
        for j in range(column):

            if (i + j) % 2 == 0:
                print("⬛", end='')

            else:
                print("⬜", end='')

        print()

chess_page_output(int(input("Please ener your row: ")),int(input("Please ener your column: ")))
