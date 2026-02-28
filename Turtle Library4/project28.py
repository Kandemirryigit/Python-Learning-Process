from turtle import Turtle,Screen

tim=Turtle()

my_screen=Screen()
my_screen.listen()



def move_right():  
    new_heading=tim.heading()-10
    tim.setheading(new_heading)


def move_left():  
    new_heading=tim.heading()+10
    tim.setheading(new_heading)


def move_up():
    tim.forward(10)


def move_down():
    tim.backward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def undo():
    tim.undo()
    



my_screen.onkey(key="D",fun=move_right)
my_screen.onkey(key="d",fun=move_right)
my_screen.onkey(key="Right",fun=move_right)


my_screen.onkey(key="A",fun=move_left)
my_screen.onkey(key="a",fun=move_left)
my_screen.onkey(key="Left",fun=move_left)


my_screen.onkey(key="W",fun=move_up)
my_screen.onkey(key="w",fun=move_up)
my_screen.onkey(key="Up",fun=move_up)


my_screen.onkey(key="S",fun=move_down)
my_screen.onkey(key="s",fun=move_down)
my_screen.onkey(key="Down",fun=move_down)


my_screen.onkey(key="C",fun=clear)
my_screen.onkey(key="c",fun=clear)

my_screen.onkey(key="g",fun=undo)
my_screen.onkey(key="G",fun=undo)




my_screen.exitonclick()
