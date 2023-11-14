def multiplication_table(row: int,column: int):
    for i in range(row):
        for j in range(column):

            if i == 0 or j == 0:
                continue
            else:
                number = i * j
                print(number,end=" ")

        print()

multiplication_table(int(input("Please ener your row: ")),int(input("Please ener your column: ")))
