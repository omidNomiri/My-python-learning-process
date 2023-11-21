import turtle

draw = turtle.Turtle()
draw.shape("turtle")

draw.goto(30,30)
draw.goto(30,-30)
draw.goto(0,0)

draw.penup()
draw.goto(-20,35)
draw.pendown()

for i in range(4):
    draw.forward(80)
    draw.right(90)

number_side = 5
x,y = -30,70
side_length = 100

for i in range(5):
    draw.penup()
    draw.goto(x,y)
    draw.pendown()

    x -= 10
    y += 20

    
    
    angle = 360.0 / number_side 
    
    for i in range(number_side):
        draw.forward(side_length)
        draw.right(angle)

    number_side += 1
    side_length += 20

turtle.done()