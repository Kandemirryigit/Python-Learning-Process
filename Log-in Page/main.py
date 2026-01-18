#Log-in Page


# To use our logos firstly we should import them from art.py to main.py
from art import password_logo,username_logo,phone_number_logo,question_logo,log_in_succesful,invalid_username,all_invalid,invalid_password,invalid_phone_number,try_again,bye_bye
import time  # To use time module firstly we should import them


# I created this global variables because if you wanna change this variables you don't have to find those ones in the code you can directly change it in here
USERNAME="username"
PHONE_NUMBER="123"  # if you don't change input's data type then you should do this str because input's default data type is str
PASSWORD="aaa"


game_on=True  # To create an infinitive loop


def count_down():
    my_time=2    # To make the code much more readable ı created this variable
    for i in range(my_time,0,-1):   # ( from 2 , to 0 , count -1)
        time.sleep(1)   # Wait 1 second before make other operation

def bye_bye_screen():
    game_on=False # To stop infinitive loop
    print("\n"*50)
    print(bye_bye)

def try_again_question_screen():
    global username_show,phone_number_show   # I created a function because of that if ı wanna use variables outside from function ı gotta use this global method to use that variables inside my function
    count_down()   # To run count_down()function
    print("\n"*50)
    print(try_again)
    try_again_question=input("Do you wanna try again? y/n: ").lower()  # Whatever you write is gonna be lowercase because ı used .lower() method
    if try_again=="n":
        bye_bye_screen()
    else:
        username_show=""       # I'm going try again because of that the variables gotta be empty
        phone_number_show=""   # I'm going try again because of that the variables gotta be empty


# To store our answers ı created this variables
username_show=""
phone_number_show=""


while game_on:  # While True

    print("\n"*50) # I used this ones in the code to create a fresh screen
    print(question_logo)
    username_or_phone_number_question=input("which one do you wanna use username or phone number? ").lower()  # whatever you write is gonna be lowercase because ı used .lower() method

    if username_or_phone_number_question=="username":
        print("\n"*50)
        print(username_logo)
        username_question=input("What is your username? ")
        username_show+=username_question  # To add our answer to username string
        print("\n"*50)
        print(f"username: {username_show}")
        print(password_logo)
        password_question=input("What is your password? ")
        if username_question==USERNAME and password_question==PASSWORD:
            print("\n"*50)
            print(log_in_succesful)
            game_on=False
        elif username_question!=USERNAME and password_question==PASSWORD :
            print("\n"*50)
            print(invalid_username)
            try_again_question_screen()
        elif username_question!=USERNAME and password_question!=PASSWORD:
            print("\n"*50)
            print(all_invalid)
            try_again_question_screen()
        elif username_question==USERNAME and password_question!=PASSWORD:
            print("\n"*50)
            print(invalid_password)
            try_again_question_screen()


    elif username_or_phone_number_question=="phone number":  # you can use else block its optional but ı think elif is much more readable
        print("\n"*50)
        print(phone_number_logo)
        phone_number_question=input("What is your phone number? ")
        phone_number_show+=phone_number_question  # To add answer of phone number question in the phone number show string
        print("\n"*50)
        print(f"phone number: {phone_number_show}")
        print(password_logo)
        password_question=input("What is your password? ")
        if phone_number_question==PHONE_NUMBER and password_question==PASSWORD:
            print("\n"*50)
            print(log_in_succesful)
            game_on=False
        elif phone_number_question!=PHONE_NUMBER and password_question==PASSWORD :
            print("\n"*50)
            print(invalid_phone_number)
            try_again_question_screen()
        elif phone_number_question!=PHONE_NUMBER and password_question!=PASSWORD:
            print("\n"*50)
            print(all_invalid)
            try_again_question_screen()
        elif phone_number_question==PHONE_NUMBER and password_question!=PASSWORD:
            print("\n"*50)
            print(invalid_password)
            try_again_question_screen()












