from turtle import Screen, Turtle

class Score_board(Turtle):

    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.show_score()

    def show_score(self):
        self.write(f"Score\n{self.score_l} :: {self.score_r}", align="center", font=("Arial", 16, "normal"))

    def add_point_l(self):
        self.score_l += 1
        self.clear()
        self.show_score()

    def add_point_r(self):
        self.score_r += 1
        self.clear()
        self.show_score()

    def end_game(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 16, "normal"))
