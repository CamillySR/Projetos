import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="make your bet",  prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "purple", "blue"]



tartarugas = []
espacamento = 50
x_fixo = -230
y_inicial = -100
for i in range(5):
    tim = Turtle(shape="turtle")
    tim.penup()
    y = y_inicial + i * espacamento
    tim.goto(x_fixo, y)
    tartarugas.append(tim)
    tim.color(colors[i])


is_race_on = True

while is_race_on:
    for turtle in tartarugas:
        if turtle.xcor() > 230:
            is_race_on = False
            winning = turtle.pencolor()
            if winning == user_bet:
                print(f"You've won! The {winning} turtle is the winner! ")
            else:
                print(f"You've lost! The {winning} turtle is the winner! ")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()