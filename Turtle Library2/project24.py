import turtle as t
from turtle import Screen
import random


tim=t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
  

ways=[0,90,180,270]


tim.width(9)
tim.speed(2)

for i in range(50):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(ways))


my_screen=Screen()
my_screen.exitonclick()