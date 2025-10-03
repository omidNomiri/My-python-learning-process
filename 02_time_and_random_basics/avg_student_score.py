total_score = 0
total_student_score_count = 0

while True:
    student_score = float(input("Please enter student score: "))
    total_score += student_score
    total_student_score_count += 1

    exit = input("Do you want to exit (y/n): ")

    if exit == "y":
        average_score = total_score / total_student_score_count
        print("Your student's average score is: ", average_score)
        break