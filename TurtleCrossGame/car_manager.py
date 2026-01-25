from turtle import Turtle
from random import choice,randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POSITIONS = [
    -240, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 
    0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 240
]
X_POSITIONS = 300

# Factory / Manager for creating many car objects
class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def Create_Car(self):
        ypos = choice(Y_POSITIONS)

        if randint(1,6) < 3:
            return 
        
        for c in self.cars:
            if abs(c.ycor() - ypos) < 30:
                return

        car = Turtle("square")
        car.color(choice(COLORS))
        car.penup()
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.goto(x=X_POSITIONS, y=ypos)
        car.setheading(180)
        self.cars.append(car)

    def Move_Cars(self):
        for car in self.cars[:]:
            car.forward(self.speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)

    def IncreaseSpeed(self):
        self.speed += MOVE_INCREMENT