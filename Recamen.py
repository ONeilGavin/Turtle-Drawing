import turtle
import random

def draw(show,speed):
    if show:
        turtle.speed(speed)
    else:
        turtle.tracer(0,0)
    turtle.penup()
    turtle.colormode(255)
    turtle.setpos(-950,0)
    turtle.pendown()

    used = list()
    number = 0

    for position in range(1, 100):
        reverse = number - position
        turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if reverse > 0 and reverse not in used: #If this number has not been used, create a circle proportional to the position
            turtle.setheading(90)
            turtle.circle(position/2 * 10, 180)
            number = reverse
            used.append(number)
        else: #Else, circle until we can find a number that works
            turtle.setheading(270)
            turtle.circle(position/2 * 10, 180)
            number += position
            used.append(number)

    turtle.exitonclick()