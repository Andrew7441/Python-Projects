from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"C:\Users\andre\Desktop\Github\Python-Projects\SnakeGame\High_Score.txt") as data:
           self.HighScore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.UpdateScore()
    
    def UpdateScore(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.HighScore}", align= ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.HighScore:
            self.HighScore = self.score
            with open(r"C:\Users\andre\Desktop\Github\Python-Projects\SnakeGame\High_Score.txt", mode="w") as data:
                data.write(f"{self.HighScore}")

        self.score = 0
        self.UpdateScore()

    def Increase(self):
        self.score += 1
        self.UpdateScore()