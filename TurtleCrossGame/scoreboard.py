from turtle import Turtle

FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-290, 270)
        self.Update_Score()
    
    def Update_Score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def Increase_Score(self):
        self.level += 1
        self.Update_Score()

    def Game_Over(self):
        self.goto(-50,0)
        self.write(f"GAME OVER", font=FONT)