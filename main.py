from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

TIME_REFRESH_IN_SEC = 0.07

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("black")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

while True:
    snake.move_forward()
    time.sleep(TIME_REFRESH_IN_SEC)

    screen.update()
    if snake.food_collision(food):
        scoreboard.update_score()
    if snake.border_collision() or snake.body_collision():
        scoreboard.game_over()
        break

screen.exitonclick()
