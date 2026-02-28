from turtle import Screen
import time  # to use time module 
from snake import Snake  # To use snake file
from food import Food  # To use food file
from scoreboard import Scoreboard  # To use scoreboard file


screen=Screen() # To define screen
screen.bgcolor("black") # To determine background color of the screen
screen.setup(600,600)  # To determine screensize
screen.title("Snake Game")  # To determine title of the screen
screen.tracer(0)  # Pause

snake=Snake()  # To define snake
food=Food()  # To define food
scoreboard=Scoreboard()  # To define scoreboard

screen.listen()  # give response to my alerts

screen.onkey(snake.up,"Up")  # If I click up in my keyboard run up function
screen.onkey(snake.down,"Down")  # If I click down in my keyboard run down function
screen.onkey(snake.left,"Left")  # If I click left in my keyboard run left function
screen.onkey(snake.right,"Right")  # If I click right in my keyboard run right function



is_game_on=True  # To create loop
while is_game_on:  # While True
    screen.update()  # contiune
    time.sleep(0.1)  # Sleep 0.1 seconds before make other opertion
    snake.move()  # run move function

    if snake.head.distance(food)<15: # If snake collision with the food
        food.refresh() # run refresh function
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        scoreboard.reset()
        snake.reset()
      

    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()

    
   
    



















screen.exitonclick()  # If I don't clock exit button the screen won't close