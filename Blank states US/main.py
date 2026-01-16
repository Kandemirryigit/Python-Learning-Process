from turtle import *  # From turtle import everything
import pandas  # To data analysis and manipulation.

turtle=Turtle() # to define turtle
screen=Screen() # to define screen
screen.bgcolor("Black")  # To determine backgroundcolor 
screen.title("U.S. states Game")  # to determine screen's title
# Image's path and this one is special for my computer it won't work in your computer
image="C:/Users/CASPER/Desktop/python_projects/Blank states US/blank_states_img.gif"  
screen.addshape(image)  # To create a shape
turtle.shape(image)  # To add image inside that shape

# To read csv file and this path is special for my computer
data=pandas.read_csv("C:/Users/CASPER/Desktop/python_projects/Blank states US/50_states.csv")
all_states=data.state.to_list()  # to convert state column to a list

guessed_states=[]  # To store
while len(guessed_states)<50:
    # .title() means capitilaze
    answer_state=screen.textinput(f"{len(guessed_states)}/50 States  correct","what's the State's name? ").title()

    if answer_state=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv()
        print(new_data)  # If user wants to exit then show all states
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=Turtle()  # To define turtle
        t.hideturtle()  # To hide tutle
        t.penup()  # To not draw anything
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)



screen.exitonclick()  # If I don't click exit button the screen won't close



