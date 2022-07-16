from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake[0].distance(food) < 13:
        food.food_pos()
        snake.extend()
        scoreboard.inc_score()

    if snake.snake[0].xcor() > 295 or snake.snake[0].xcor() < -300 or snake.snake[0].ycor() > 275 or snake.snake[0].ycor() < -295:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.snake[1:]:
        if snake.snake[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
