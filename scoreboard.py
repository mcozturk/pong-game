from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score_1} l {self.score_2}", align="center", font=("Arial", 30, "bold"))

    def add_score(self, player):
        if player == "left":
            self.score_1 += 1
        else:
            self.score_2 += 1
        self.update_scoreboard()
