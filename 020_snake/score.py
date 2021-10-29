from turtle import Screen, Turtle

class Score_board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def add_point(self):
        self.score += 1
        self.clear()
        self.show_score()

    def end_game(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 16, "normal"))
