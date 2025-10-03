import math
import mpmath

print("Welcome to calculator \n"
    "What do you want: \n"
    "1= sum : + \n"
    "2= subtraction : - \n"
    "3= multiplication : * \n"
    "4= division : / \n"
    "5= square root : √ \n"
    "6= sinus : sin \n"
    "7= cosine : cos \n"
    "8= tangent : tan \n"
    "9= Cotangent : cot \n"
    "10= factorial : fact"
    )

Op_user_want = int(input("please select between number 1 until number 10:"))

if Op_user_want == 1 or Op_user_want == 2 or Op_user_want == 3 or Op_user_want == 4:
    Number1 = float(input("please enter your first number:"))
    Number2 = float(input("please enter your second number:"))
    
    if Op_user_want == 1:
        print("your result =",Number1 + Number2)
        
    if Op_user_want == 2:
        print("your result =",Number1 - Number2)
            
    if Op_user_want == 3:
        print("your result =",Number1 * Number2)
            
    if Op_user_want == 4:
        print("your result =",Number1 / Number2)

if Op_user_want == 5 or Op_user_want == 6 or Op_user_want == 7 or Op_user_want == 8 or Op_user_want == 9 or Op_user_want == 10:
    Number1 = float(input("please enter your number:"))
    
    if Op_user_want == 5:
        print(math.sqrt(Number1))
    if Op_user_want == 6:
        Number1 = math.radians(Number1)
        print(math.sin(Number1))    
    if Op_user_want == 7:
        Number1 = math.radians(Number1)
        print(math.cos(Number1))    
    if Op_user_want == 8:
        Number1 = math.radians(Number1)
        print(math.tan(Number1))
    if Op_user_want == 9:
        Number1 = math.radians(Number1)
        print(mpmath.cot(Number1))
    if Op_user_want == 10:
        print(mpmath.factorial(Number1))
    