from turtle import Screen, Turtle

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Arcade Game")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.penup()
paddle.goto(380,0)


def go_up():
    paddle.goto(paddle.xcor(), paddle.ycor() + 20)
def go_down():
    paddle.goto(paddle.xcor(), paddle.ycor() - 20)

screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")

is_game_on = True
while is_game_on:
    screen.update()
    


screen.exitonclick()