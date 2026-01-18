
import turtle as t
from turtle import *  # From turtle import everything
import random  # To use random firstly we should import it


tim=t.Turtle() # To define turtle

my_screen=Screen()  # To define screen
my_screen.bgcolor("black")  # To determine background color black


t.colormode(255)  # To use rgb colors between 0-255
tim.speed(20)     # To define tim's speed 20
tim.hideturtle()  # To hide the cursor


def random_color():
    r=random.randint(0,255)  # To determine a random color
    g=random.randint(0,255)  # To determine a random color
    b=random.randint(0,255)  # To determine a ranodm color
    random_color=(r,g,b)
    return random_color

for i in range(75):   # Repeat this 75 times
    tim.color(random_color()) # To define tim's color random_color
    tim.circle(100)   # To define circle's radius 100 
    tim.left(5)       # Turn left 5 degrees



my_screen.exitonclick()   # I can see the screen if I don't close the screen 