from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.UpdateScore()
    
    def UpdateScore(self):
        self.clear()
        self.write(f"Score: {self.score}", align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align= ALIGNMENT, font= FONT)

    def Increase(self):
        self.score += 1
        self.UpdateScore()