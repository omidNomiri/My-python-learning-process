is_factorial = int(input("Please enter your number: "))

if is_factorial == 0 or is_factorial == 1:
    print("Yes")
    
for number in range(2, is_factorial):
    if is_factorial % 2 != 0:
        print("No")
        break
    else:
        print("Yes")
        break
