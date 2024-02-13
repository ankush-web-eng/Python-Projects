from turtle import Turtle
import random
t = Turtle()
directions = [0,90,180,270]
def random_walk(numbers):
    for i in range(numbers):
        t.forward(random.randint(45,90))
        t.right(random.choice(directions))

random_walk(50)

