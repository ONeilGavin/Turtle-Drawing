import turtle
import random

def prime(number): #Method to check if number is prime
    for i in range(2,number):
         if(number % i ) == 0:
            return False
    return True

def draw(show, speed):
    if(show):
        turtle.speed(speed)
    else:
        turtle.tracer(0,0)
    turtle.left(90)
    turtle.colormode(255)
    turtle.penup()
    counter = 0
    side = 1

    for number in range (2, 13000):
        turtle.forward(5)
        if prime(number): #Make a dot if the number is prime
            turtle.pencolor(random.randint(0,255),  random.randint(0,255),  random.randint(0,255))
            turtle.dot(3)
        counter += 1

        if counter == side: #Change direction to keep going in a spiral
            counter = 0
            turtle.left(90)
            if turtle.heading() in (90, 270):
                side += 1

    turtle.exitonclick()