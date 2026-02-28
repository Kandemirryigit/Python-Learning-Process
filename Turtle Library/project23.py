from turtle import *  # From turtle import everything
import random  # To use random module firstly we should import it


tim=Turtle()
colours=["cornflowerblue","darkOrchid","Indianred","deepskyblue","LightSeaGreen","wheat","SlateGray","SeaGreen"]

def draw_shape(num_sides):
    angle=360/num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_number in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_number)




my_screen=Screen()
my_screen.exitonclick()