
import random      # To use random module firstly we should import it
from art import *  # From art.py import everything inside main.py
from character import data  # From chracters.py import data to main.py
import time        # To use time module firslt we should import it


first_competitors_score=0
second_competitors_score=0
round_number=0
nobody_won=True   # To create an infinitive loop




def start_screen():
    global first_competitors_name,second_competitors_name  # We are inside a function and if we want to use variables from outside function we should use this method
    print("\n"*50)
    print(higher_lower_logo)
    time.sleep(3)  # To wait 3 seconds before make other operation

    print("\n"*50)
    print(first_competitors_name_logo)
    first_competitors_name=input("What is first competitor's name: ")
    print("\n"*50)
    print(second_competitors_name_logo)
    second_competitors_name=input("What is second competitor's name: ")

start_screen()  # To run function


def scores():
    global first_competitors_score,second_competitors_score   # We are inside a function and if we want to use a variable from outside function we should use this method
    if (true_answer=="a" and answer=="a" and round_number%2==1) or (true_answer=="b" and answer=="b" and round_number%2==1):
        first_competitors_score+=1   # To increase variable's value +1
    elif (true_answer=="a" and answer=="a" and round_number%2==0) or (true_answer=="b" and answer=="b" and round_number%2==0):
        second_competitors_score+=1  # To increase variable's value +1


def right_wrong_answer_function():
    global first_competitors_score,second_competitors_score   # We are inside a function and if we want to use a variable from outside function we should use this method
    if (true_answer=="a" and answer=="a") or (true_answer=="b" and answer=="b"):
        scores()
        print("\n"*50)
        print(f"{first_competitors_name}'s score: {first_competitors_score}\n{second_competitors_name}'s score: {second_competitors_score}")
        print(right_answer_logo)
        print("congrats you knew it right...")
        input("\nPress enter to the next question...")
    else:
        scores()
        print("\n"*50)
        print(f"{first_competitors_name}'s score: {first_competitors_score}\n{second_competitors_name}'s score: {second_competitors_score}")
        print(wrong_answer_logo)
        print("Sorry...Your answer is wrong!")
        input("\nPress enter to the next question...")



def wanna_play_again_function():
    global first_competitors_score,second_competitors_score,selected_chracters,round_number,nobody_won,is_game_on   # We are inside a function and if we want to use a variable from outside function we should use this method
    print("\n"*50)
    print(wanna_play_again_logo)
    wanna_play_again_question=input("do you wanna restart game? (y/n) :").lower()  # Whatever you write is going to be all lowercase
    if wanna_play_again_question=="n":
        print("\n"*50)
        print(game_over_logo)
        nobody_won=False   # To stop loop
    else:
        # To clear all previous informations
        first_competitors_score=0  
        second_competitors_score=0
        selected_chracters=[]
        round_number=0
        start_screen()
        
 

while nobody_won:  # While True/False
        
        round_number+=1   # To count every single restart
        
        # To choose random index from data
        chracter1=random.choice(data) 
        chracter2=random.choice(data) 

        while chracter1==chracter2:
            chracter1=random.choice(data)
            chracter2=random.choice(data)

        chracter1_follower_count=chracter1["follower_count"]
        chracter2_follower_count=chracter2["follower_count"]

        print("\n"*50)
        if round_number%2==1:    # Odd number
            print(first_competitors_round_logo)
            time.sleep(2)
            print("\n"*50)
        else:                   # Even number
            print(second_competitors_round_logo)
            time.sleep(2)
            print("\n"*50)


        print(question_logo)
        print(f"A: {chracter1["name"]} , {chracter1["team"]} , {chracter1["country"]}")
        print(vs_logo)
        print(f"B: {chracter2["name"]} , {chracter2["team"]} , {chracter2["country"]}")
        answer=input("\nWhich fotbaal player has more follower on instagram? (A/B) : ").lower()   # Whatever you write is going to be all lowercase

        if chracter1_follower_count>chracter2_follower_count:
            true_answer="a"
            right_wrong_answer_function()
        elif chracter1_follower_count<chracter2_follower_count:    # You can directly use else because there are no other option but I think elif is much more clear and readable
            true_answer="b"
            right_wrong_answer_function()

        if first_competitors_score>=3 and (first_competitors_score-second_competitors_score>=2):
            print("\n"*50)
            print(first_competitor_won_logo)
            input("\npress enter to continue...")
            wanna_play_again_function()
        elif second_competitors_score>=3 and (second_competitors_score-first_competitors_score>=2):
            print("\n"*50)
            print(second_competitor_won_logo)
            input("\nPress enter to continue...")
            wanna_play_again_function()



    


        

            

    










    


    

