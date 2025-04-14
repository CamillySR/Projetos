import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
snake = Snake()
food = Food()
score = Score()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
screen.listen()


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    screen.onkeypress(snake.move_up, "Up")
    screen.onkeypress(snake.move_down, "Down")
    screen.onkeypress(snake.turn_left, "Left")
    screen.onkeypress(snake.turn_right, "Right")

    if snake.head.distance(food) < 15:
        food.refresh_food()
        score.counting_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.xcor() < -280:
        game_on = False
        score.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()




screen.exitonclick()