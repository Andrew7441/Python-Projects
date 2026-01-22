from turtle import *

andrew = Turtle()
screen = Screen()
screen.listen()

def move_forward():
    andrew.fd(10)

def move_backward():
    andrew.bk(10)

def move_left():
    andrew.lt(10)

def move_right():
    andrew.rt(10)

def clear():
    andrew.reset()

def penup():
    andrew.penup()

def pendown():
    andrew.pendown()

screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="space", fun=clear)
screen.onkey(key= "Shift_L", fun= penup)
screen.onkey(key= "z", fun= pendown)



screen.exitonclick()