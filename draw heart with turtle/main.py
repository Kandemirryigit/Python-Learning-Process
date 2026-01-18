
from turtle import * # From turtle import everything

turtle =Turtle()  # To define turtle
screen=Screen()   # to define screen

screen.bgcolor("black")  # .To determine screen's background color
screen.setup(width=600,height=600)  # To determine screen's size
turtle.speed(3)  # To determine turtle's speed
turtle.color("red")  # To determine line's color

turtle.hideturtle()  # To hide turtle
turtle.penup()  # To not draw anything
turtle.goto(x=0,y=-100)  # To sent our tutle a specific location
turtle.pendown()  # To can draw something
turtle.showturtle()  # to show turtle

turtle.begin_fill()  # To start filling

# To draw our heart's shape
turtle.left(140) 
turtle.forward(180)
turtle.circle(-90, 200)
turtle.left(120)
turtle.circle(-90, 200)
turtle.forward(180)

turtle.end_fill()  # To stop filling
turtle.hideturtle()  # To hide turtle

screen.exitonclick()  # If I don't click exit button the screen won't close
