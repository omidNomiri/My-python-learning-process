Student_name = input("please enter your student name: ")
Student_family = input("please enter your student family:")
Student_score1 = int(input("please enter your student first score:"))
Student_score2 = int(input("please enter your student second score:"))
Student_score3 = int(input("please enter your student third score:"))

Avg_student_score = (Student_score1 + Student_score2 + Student_score3) / 3

if Avg_student_score > 17:
    print(f"{Student_name}{Student_name} is Great student")
if 17 > Avg_student_score >= 12:
    print(f"{Student_name}{Student_name} is Normal student")
if 12 > Avg_student_score:
    print(f"{Student_name}{Student_name} he/she Fail")