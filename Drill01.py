import turtle
import random

distance = 50
d = distance

def move_up():
    turtle.setheading(90)
    turtle.forward(d)
    turtle.stamp()

def move_down():
    turtle.setheading(270)
    turtle.forward(d)
    turtle.stamp()

def move_right():
    turtle.setheading(0)
    turtle.forward(d)
    turtle.stamp()

def move_left():
    turtle.setheading(180)
    turtle.forward(d)
    turtle.stamp()

def restart():
    turtle.reset()


turtle.shape('turtle')

turtle.onkey(move_up,'w')
turtle.onkey(move_down,'s')
turtle.onkey(move_right,'d')
turtle.onkey(move_left,'a')
turtle.onkey(restart,'Escape')
turtle.listen()
