from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 270)
        self.color("White")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", move=False, align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.data_score()
        self.score = 0
        self.update_score()

    def score_func(self):
        self.score += 1
        self.clear()
        self.update_score()

    def data_score(self):
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
