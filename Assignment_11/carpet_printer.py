def carpet_printer(number):
    carpet = []
    for i in range(number):
        row = []
        for j in range(number):
                pattern = min(i, j, number - i - 1, number - j - 1)
                if pattern == 0:
                    row.append("🟫")
                elif (pattern % 2) != 0:
                    row.append("🟩")
                elif (pattern % 2) == 0:
                    row.append("🟦")

        carpet.append(row)

    for row in carpet:
        for item in row:
            print(item, end=" ")
        print()

carpet_printer(11)