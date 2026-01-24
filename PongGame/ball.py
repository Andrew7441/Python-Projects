from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.Xmove = 10
        self.Ymove = 10
        self.spd = 0.1

    def move(self):
        newX = self.xcor() + self.Xmove
        newY = self.ycor() + self.Ymove
        self.goto(x=newX, y=newY)

    def bounceY(self):
        self.Ymove *= -1
    
    def bounceX(self):
        self.Xmove *= -1
        self.spd *= 0.5
    
    def Reset_Position(self):
        self.goto(0, 0)
        self.spd = 0.1
        self.bounceX()

