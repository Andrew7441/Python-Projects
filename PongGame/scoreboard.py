from turtle import Turtle

FONT = ("Courier", 60, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.L_score = 0
        self.R_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.L_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.R_score}", align=ALIGNMENT, font=FONT)
    
    def L_increase(self):
        self.L_score += 1
        self.update_score()
    
    def R_increase(self):
        self.R_score += 1
        self.update_score()
