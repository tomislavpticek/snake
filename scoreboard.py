from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.sety(280)

        self.score = 0

        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center")

    def update_score(self):
        self.clear()
        self.score += 1
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score}", False, align="center")
