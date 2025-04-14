from turtle import Turtle
FONT = ("courier", 22, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}", move=True, align="center", font=FONT)
        self.hideturtle()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font= FONT)
    def counting_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}", move=True, align="center", font=FONT)

