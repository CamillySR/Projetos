import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("purple")
        self.shapesize(0.5)
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh_food(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
