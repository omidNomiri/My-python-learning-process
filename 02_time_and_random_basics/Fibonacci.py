number = int(input("Please enter your number: "))
number1 = 0
number2 = 1
next_number = number2 
count = 1

while count <= number:
	print(next_number,end=" ")
	count += 1
	number1, number2 = number2, next_number
	next_number = number1 + number2
