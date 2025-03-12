import turtle as t
import random
timmy_the_turtle = t.Turtle()
timmy_the_turtle.speed(0)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, b, g)
    return random_color
for _ in range(100):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.left(5)


screen = t.Screen()
screen.exitonclick()




