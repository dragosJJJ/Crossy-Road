from turtle import Turtle

FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-250, 250)
        self.ht()
        self.level = 1
        self.write(f'Level {self.level}', font=FONT)

    def update_level(self):
        self.clear()
        self.write(f'Level {self.level}', font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT, align="center")
        self.goto(0,-30)
        self.write(f'Lost at level {self.level}', font=("Courier", 16, "normal"),align="center")

