#Rock,Paper,Scissors Game


import random  # To use random module firstly we should import that library to our .py file
import time    # To use time module firstly we should import that library to our .py file
from art import welcome,draw,lose,win,victory,defeat,wanna_play_again_logo,game_over  # To use our logos we should import them from art.py to main.py


game_on2=True  # To create an infinitive loop
my_score=0     # First score is going to be 0 because the game didn't start
computer_score=0  # First score is going to be 0 because the game didn't start


def welcome_screen():    
    print("\n"*25)  # to create a fresh screen
    print("My Score: 0\nComputer's Score: 0")   # \n means create new line
    print(welcome)

welcome_screen()  # To run function

    
while game_on2:   # While True
    
        user_choice=input("select one option:\n \nrock\npaper\nscissors\n").lower()  # whatever you typed is going to be lowercase because ı used .lower() method
        list=["rock","paper","scissors"]
        computer_choice=random.choice(list)   # to choose a random index from list

       
        if user_choice==computer_choice:
            print("\n"*20)  # To create a fresh screen
            print(f"computer score:{computer_score}")
            print(f"my score: {my_score}")
            print(draw)  # To Show draw logo
            print(f"computer's choice was {computer_choice} too \n")
            
            
        if (user_choice=="rock" and computer_choice=="paper") or (user_choice=="paper" and computer_choice=="scissors") or (user_choice=="scissors" and computer_choice=="rock"): 
            print("\n"*20)  # To create a fresh screen
            computer_score+=1  # I lost because of that computer's score is going to increase
            print(f"computer score:{computer_score}")
            print(f"my score: {my_score}")
            print(lose)  # To show lose logo
            print(f"computer's choice was {computer_choice}")
            print(f"your choose was {user_choice}\n")
        


        if (user_choice=="rock" and computer_choice=="scissors") or (user_choice=="paper" and computer_choice=="rock") or (user_choice=="scissors" and computer_choice=="paper"):
                print("\n"*20)
                my_score+=1  # I won so my score is going to increase
                print(f"computer score:{computer_score}")
                print(f"my score: {my_score}")
                print(win)
                print(f"computer's choice was {computer_choice}")
                print(f"your choose was {user_choice}\n")
                
    

        def count_down():
            my_time=5    # I created this variable because ı wanted to write my code more readable if you want you can directly write this in the range method
            for i in range(my_time,0,-1):   # (from 3 , to o , count -1)
                time.sleep(1)  # This means wait 1 second before doing other operation

     
        if my_score==3:
            print("\n"*50)  # To create a fresh screen
            print(f"computer's final score: {computer_score}")
            print(f"my final score: {my_score}")
            print(victory) # To show victory logo
            count_down()  # To run count_down() function
            print("\n"*30)  # To create a fresh screen
            print(wanna_play_again_logo)  # To show wanna play again logo
            wanna_play_again_question=input("Do you wanna play again? y/n: ").lower()  # Whatever you write is gonna be lowercase because ı added .Lower() method
            if wanna_play_again_question=="n":
                print("\n"*50)    # To create a fresh screen
                print(game_over)  # To show game over logo
                game_on2=False    # to stop loop
            else:
                my_score=0   # To reset score because the game is gonna start again
                computer_score=0  # To reset score because the game is gonna start again
                welcome_screen()  # To eun welcome screen function
                

        if computer_score==3:
            print("\n"*50)  # To create a fresh screen
            print(f"computer's final score: {computer_score}")
            print(f"my final score: {my_score}")
            print(defeat)  # To show defeat logo 
            count_down()  # To run count_down() function
            print("\n"*30)
            print(wanna_play_again_logo)
            wanna_play_again_question2=input("Do you wanna play again? y/n: ").lower()
            if wanna_play_again_question2=="n":
                print("\n"*50)  # to create a fresh screen
                print(game_over) # To show game over logo
                game_on2=False  # to stop infinitive loop
            else:
                my_score=0   # To reset score because the game is gonna start again
                computer_score=0   # To reset score because the game is gonna start again
                welcome_screen()  # To run welcome_screen() function
                
            


    
    





 
  









