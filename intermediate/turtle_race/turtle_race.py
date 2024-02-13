from turtle import Turtle, Screen
from random import randint

is_race = False
screen = Screen()
screen.setup(width=1000,height=800)
user_bet = screen.textinput(title="Turtle Race", prompt="Which turtle will win the race? Chose your color: ")
colors = ["red", "green","orange", "yellow", "blue", "purple"]
y_positions = [-140,-80,-20,40,100,160]
all_turtles = []

for i in range(6):
    t = Turtle(shape="turtle")
    t.penup()
    y_col = colors[i]
    y_new = y_positions[i]
    t.goto(x=-470,y=y_new)
    t.color(y_col)
    all_turtles.append(t)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 470:
            is_race = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You have won the bet! {winning_turtle} is the Winner!!")
                print(f"Your choice was {user_bet}")
            else:
                print(f"You have lost the bet! {winning_turtle} is the Winner!!")
                print(f"Your choice was {user_bet}")

        random_int = randint(0,10)
        turtle.forward(random_int)


screen.exitonclick()