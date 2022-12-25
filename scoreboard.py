from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-290, 260)
        self.write(f"Level: {self.score}", 20, font = FONT)

    def level(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(-70, 0)
        self.write("GAME OVER", 20, font = FONT)

