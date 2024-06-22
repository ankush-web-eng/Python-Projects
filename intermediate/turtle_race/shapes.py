from turtle import Turtle
import random
t = Turtle()

colours = ["red", "green", "blue", "pink", "purple", "orange", "violet",]

def shapes(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        t.forward(50)
        t.right(angle)

for sides in range(3,10):
    t.color(random.choice(colours))
    shapes(sides) 