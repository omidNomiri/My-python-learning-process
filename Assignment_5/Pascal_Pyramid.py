def Pascal_Pyramid(number):
    triangle = []

    for i in range(number):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    for row in triangle:
        print(row)

Pascal_Pyramid(int(input("Please ener your number: ")))
