from turtle import * # From Turtle import everything
import random  # To use random module firstly we should import it


my_screen=Screen()  # To define screen
my_screen.bgcolor("black")  # To determine Screen's background color 
guess=my_screen.textinput("question","which turtle gonna win the race? blue/yellow/pink/orange/purple").lower() #Pop-Up


# To define every single turtle's name and their shapes
tim=Turtle("turtle")
tommy=Turtle("turtle")
rick=Turtle("turtle")
morty=Turtle("turtle")
sane=Turtle("turtle")
line=Turtle("turtle")


disatnce=[5,10,15,20,25,30]  # Random distances


tim.color("DeepSkyBlue2")  # To determine turtle's color
tim.backward(305)
tim.clear()  # To clear lines

tommy.color("gold1")
tommy.goto(-310,100)
tommy.clear()

rick.color("VioletRed2")
rick.goto(-310,-100)
rick.clear()

morty.color("sienna1")
morty.goto(-310,200)
morty.clear()

sane.color("magenta4")
sane.goto(-310,-200)
sane.clear()

line.speed(500)
line.goto(310,300)
line.clear()



# To create a finish line
for i in range(60):
    line.dot(30,"white")
    line.setheading(270)
    line.forward(10)


# If game is on every single turtle should move randomly
while tim.xcor()<=310 and tommy.xcor()<=310 and rick.xcor()<=310 and morty.xcor()<=310 and sane.xcor()<=310:
    tim.forward(random.choice(disatnce))
    tim.clear()
    tommy.forward(random.choice(disatnce))
    tommy.clear()
    rick.forward(random.choice(disatnce))
    rick.clear()
    morty.forward(random.choice(disatnce))
    morty.clear()
    sane.forward(random.choice(disatnce))
    sane.clear()



blue=tim.xcor()
yellow=tommy.xcor()
green=rick.xcor()
orange=morty.xcor()
purple=sane.xcor()



if blue>310:
    if guess=="blue":
        tim.write("Right",align="center",font=("Arial", 16, "normal"))
    else:
        tim.write("Wrong",align="center",font=("Arial", 16, "normal"))
elif yellow>310:
    if guess=="yellow":
        tommy.write("Right",align="center",font=("Arial", 16, "normal"))
    else:
        tommy.write("Wrong",align="center",font=("Arial", 16, "normal"))
elif green>310:
    if guess=="green":
        rick.write("Right",align="center",font=("Arial", 16, "normal"))
    else:
        rick.write("Wrong",align="center",font=("Arial", 16, "normal"))
elif orange>310:
    if guess=="orange":
        morty.write("Right",align="center",font=("Arial", 16, "normal"))
    else:
        morty.write("Wrong",align="center",font=("Arial", 16, "normal"))
elif purple>310:
    if guess=="purple":
        sane.write("Right",align="center",font=("Arial", 16, "normal"))
    else:
        sane.write("Wrong",align="center",font=("Arial", 16, "normal"))



my_screen.exitonclick() # If I don't click exit button my screen is not gonna close.







