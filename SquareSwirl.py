import turtle
import random

def draw(show, speed):
    if show == True:
        turtle.speed(speed)
    else:
        turtle.tracer(0, 0)

    turtle.colormode(255)

    height = 10
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    for j in range(360):
        if b > 255: #Increment the other RBG values when one reaches the max
            g += 5
            b = 0
        if g > 255:
            g = 0
            r += 5
        if r>255:
            r = 0
        turtle.pencolor(r, g, b)


        for i in range(5): #Draw Square
            turtle.forward(h)
            turtle.right(90)

        turtle.right(3) #Turn to create a spiral
        height = height * 1.03
        b += 5
    turtle.exitonclick()

