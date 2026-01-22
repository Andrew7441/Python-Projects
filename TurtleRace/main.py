from turtle import *
from random import *

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Place Bet", prompt="Bet on turtle color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y = -80

for i in range(6):
    x = Turtle("turtle")
    x.penup()
    x.color(colors[i])
    x.goto(-230, y)
    y += 30
    turtles.append(x)


race_on = False

if bet: # Start race only when user places a bet
    race_on = True

while race_on:

    for t in turtles:
        if t.xcor() > 230:
            winning_color = t.pencolor()
            race_on = False
            break

        distance = randint(0, 10)
        t.forward(distance)   

if winning_color == bet:
    print("Congratulations! You Won!")
else:
    print("You Lost!")
    print(f"Winning turtle is: {winning_color}")



screen.exitonclick()