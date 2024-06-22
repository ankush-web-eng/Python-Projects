from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Arcade Game")
screen.tracer(0)

r_paddle = Paddle((380,0))
l_paddle = Paddle((-380,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

is_game_on = True

# def is_game_over():
#     is_game_on = False

# screen.listen(is_game_over, "o")

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect Collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 :
        ball.bounce_x()
        scoreboard.r_point()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()
        scoreboard.l_point()

    #Detect Missing paddles
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset_position()
        scoreboard.end_game()
        is_game_on = False


screen.exitonclick()