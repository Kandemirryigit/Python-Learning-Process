#Hirst painting

from turtle import *  # From turtle import everything
import random   # To use random module firstly we should import it


tim=Turtle()  # To define Turtle
tim.speed(10)  # To determine turtle's speed
tim.hideturtle()  # To hide cursor


my_screen=Screen()  # To define screen
my_screen.bgcolor("black")  # To define backgroundcolor black
my_screen.title("Hirst Painting")  # To determine our screen's title


# colors
colours=["cornflowerblue","darkOrchid","Indianred","deepskyblue","LightSeaGreen","wheat","SlateGray","SeaGreen","AntiqueWhite","AntiqueWhite4","Deepskyblue2","gold1","green","hotpink","LightSkyBlue"]



tim.setheading(270) # To change turtle's heading
tim.penup()  # Pen-up so turtle can draw anything
tim.forward(200) # To move our turtle
tim.setheading(180)
tim.forward(225)
tim.setheading(0)


def dot1():
    for i in range(10): # Repeat this 10 times
        tim.dot(20,random.choice(colours))   # 20 = point's size 
        tim.forward(50)
        

def one():
    dot1()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)


for i in range(10):
    one()
    tim.backward(500)




my_screen.exitonclick()  # If I don't click exit button my screen is not going to close
