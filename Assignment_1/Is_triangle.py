Side_1 = input("please enter first side: ")
Side_2 = input("please enter second side: ")
Side_3 = input("please enter third side: ")

Is_triangle = Side_1 + Side_2 > Side_3

if Is_triangle == True:
    print("you can draw a triangle")
elif Is_triangle == False:
    print("you can't draw a triangle")
