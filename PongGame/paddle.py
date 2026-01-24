from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self,pos):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=3)
        self.penup()
        self.goto(pos)

    def up(self):
        newY = self.ycor() + 20
        self.goto(self.xcor() ,newY)
    
    def down(self):
        newY = self.ycor() - 20
        self.goto(self.xcor() , newY)
    