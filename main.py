from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Amarjeet's Snake Game!")
screen.tracer(0)  # Turn off the animation for this screen.


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.update()  # turn on the animation.

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# def show_score_on_screen():
#     """will show the user current score on screen."""
#     pass


game_is_on = True

while game_is_on:
    screen.tracer(0)
    snake.move()
    snake.check_out_of_screen()
    screen.update()
    time.sleep(0.1)

    # will check food collision here.
    if food.distance(snake.head) <= 15:
        food.update_food()
        snake.update_new_portion_in_snake()
        scoreboard.refresh()
        # print("food updated")

    # check boundary collision here
    if snake.head.xcor() == 280 or snake.head.xcor() == -280 or snake.head.ycor() == 280 or snake.head.ycor() == -280:
        # end the game here
        scoreboard.game_over()
        game_is_on = False

    # check iff snake touched it's tail
    for segment in snake.segment_square[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
