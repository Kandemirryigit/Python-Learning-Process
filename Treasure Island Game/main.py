#Treasure Island game


# To import logos from art.py to main.py
from art import treasure_island,lake,attack_trout,fall_hole,doors,win,fire,beast,game_over,wanna_play_again,byebye
# İf you wanna use time module firstly you should import it
import time


# I used while loop and functions because of that I don't wanted to struggle with variables and I created global variable
RUN=True  # To create an infinitive loop


def wanna_play_again_func():
    global RUN # I used this method to use Gloval variable in local(in my function's inside)
    wanna_play_again_question=input("Do you wanna play again? y/n: ").lower()  # Y->y and N->n
    if wanna_play_again_question=="n":
        print("\n"*50)  # To show a fresh screen
        print(byebye)
        RUN=False
    elif wanna_play_again_question=="y":  # You can also use else it's optional I think this version i smuch more readable
        print("\n"*50)



def count_down():
    my_time=2   # this is optional you can directly write your time inside range.But in my opinion this is muh more readable
    for i in range(my_time,0,-1):   # to create a loop (from 3 , to 0 , count -1)
        time.sleep(1)   # This means: wait 1 second befoe make other operation



def to_go_wanna_play_again_screen():
    count_down()    # To use count_down function
    print("\n"*50)
    print(wanna_play_again)
    wanna_play_again_func()  # To use wanna_play_again_func function



# While True
while RUN:

    print("\n"*50) # To create a fresh screen
    print(treasure_island)
    print("Welcome to the treasue Island\nyour mission is to find the treasure")
    direction=input("You are at a cross road.Where do you want to go? type 'left' or 'right': ").lower()  # Left or LEFT -> left , Right or RİGHT -> right  because I used .lower() method

    if direction=="left":
        print("\n"*50)  # To create a fresh screen
        print(lake)
        print("You have come to a lake.There is an island in the middle of the lake")
        wait_swim_question=input("Type 'wait' to wait for a boat.Type 'swim' to swim across ").lower()  # Wait or WAİT -> wait , Swim or SWIM -> swim because I used .lower() method
        if wait_swim_question=="wait":
            print("\n"*50)
            print(doors)
            print("You arrive at the island unharmed.There is a house with 3 doors")
            door_question=input("one red,one yellow,one blue which one do you prefer? ").lower()
            if door_question=="yellow":
                print("\n"*50)
                print(win)
                print("You win!")
                to_go_wanna_play_again_screen()
            elif door_question=="red":
                print("\n"*50)
                print(fire)
                print("Burned by fire,Game Over")
                count_down()
                print("\n"*50)
                print(game_over)
                to_go_wanna_play_again_screen()
            elif door_question=="blue":   # you can also use else because there are 3 options(doors) and this is last one but ı thin elif is much more readable
                print("\n"*50)
                print(beast)
                print("Eaten by beasts,Game Over")
                count_down()
                print("\n"*50)
                print(game_over)
                to_go_wanna_play_again_screen()
        
        else:
            print("\n"*50)
            print(attack_trout)
            print("Attacked by trout,Game Over")
            count_down()
            print("\n"*50)
            print(game_over)
            to_go_wanna_play_again_screen()

    else:
        print("\n"*50)
        print(fall_hole)
        print('Fall into a hole,Game Over')
        count_down()
        print("\n"*50)
        print(game_over)
        to_go_wanna_play_again_screen()
