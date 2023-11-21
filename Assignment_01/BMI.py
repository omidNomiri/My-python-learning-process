weight = float(input("Please enter your weight(kg): "))
height = float(input("Please enter your height(m): "))

BMI = weight / (height ** 2)

if BMI < 18.5:
    print(f"your BMI is {BMI} and you'r a Under weight")
if 24.9 > BMI > 18.5:
    print(f"your BMI is {BMI} and you'r a Normal weight")
if 29.9 > BMI > 25:
    print(f"your BMI is {BMI} and you'r a Over weight")
if 34.9 > BMI > 30:
    print(f"your BMI is {BMI} and you'r a Obesity")
if 39.9 > BMI > 35:
    print(f"your BMI is {BMI} and you'r a Extreme obesity ")