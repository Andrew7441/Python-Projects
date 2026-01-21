# import colorgram

# colors = colorgram.extract("image.jpg", 30)
# rgb = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)

from turtle import *
from random import *

colormode(255)

colors = [(248, 238, 219), (223, 155, 90), (214, 240, 228), (240, 206, 90), (104, 170, 203), (36, 109, 149), 
          (199, 227, 239), (113, 193, 161), (153, 61, 94), (208, 78, 109), (243, 215, 226), (25, 134, 101), 
          (224, 81, 59), (205, 133, 155), (184, 59, 43), (177, 166, 36), (138, 219, 198), (39, 54, 113), 
          (238, 161, 180), (105, 40, 73), (137, 215, 228), (239, 168, 157), (14, 93, 69), (60, 166, 132), 
          (27, 47, 88), (53, 157, 186), (109, 116, 170), (72, 36, 65), (14, 69, 51), (180, 186, 218)] 

andrew = Turtle()

andrew.penup()
andrew.goto(-400, -300)
andrew.pendown()

andrew.speed("fastest")

def draw():
    for _ in range(17):
        andrew.dot(20, choice(colors))
        andrew.penup()
        andrew.fd(50) 
        andrew.pendown()  

def goback():
    andrew.penup()
    andrew.setheading(90)
    andrew.fd(50)
    andrew.setheading(180)
    andrew.forward(850)
    andrew.setheading(0)

for _ in range(14):
    draw()  
    goback()

screen = Screen()
screen.exitonclick()