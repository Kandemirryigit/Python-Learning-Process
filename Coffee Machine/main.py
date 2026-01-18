
from art import *  # From art.py import everything to main.py so we can use things inside art.py
import time        # To use time module firstly we should import it
from menu_and_warehouse import *  # From menu_andwarehouse import everything inside main.py

MAIN_PAGE_LOOP=True  # To create an infinitive loop
BOX=0


print("\n"*50)  # To create a fresh screen
print(welcome_to_coffe_world_logo)
time.sleep(3)     # To wait 3 seconds before make other operation


def reduce_supplies():
    global BOX  # We are inside a function and if we want to use global variable we should use this method
    ware_house["water"]-=menu[order]["ingredients"]["water"]
    ware_house["milk"]-=menu[order]["ingredients"]["milk"]
    ware_house["coffee"]-=menu[order]["ingredients"]["coffee"]


def coffee_preaparing_screen():
    print("\n"*50)
    print(prepearing_logo)
    time.sleep(3)    # To wait 3 seconds before make other operation
    print("\n"*50)
    print(ready_logo)
    print("You can take your coffee")
    input("\nWhen you took your coffee please press enter...")
    print("\n"*50)


def order_or_finish_function():
    global MAIN_PAGE_LOOP   # We are inside a function and if we want to use this variable we should use this method
    print(another_one_logo)
    finish_or_main_page_question=input("To finish operation write: finish: , to return main page write: main page: ").lower()  # whatever you write is going to be all lowercase
    if finish_or_main_page_question=="finish":
        print("\n"*50)
        print(bye_bye_logo)
        MAIN_PAGE_LOOP=False  # To stop loop
    elif order_or_finish_function=="main page":
         main_page_function()
    



def control():
            global BOX  # We are inside a function and if we want to use this variable we should use this method

            if  ware_house["water"]>=menu[order]["ingredients"]["water"] and ware_house["milk"]>=menu[order]["ingredients"]["milk"] and ware_house["coffee"]>=menu[order]["ingredients"]["coffee"]:
                print("\n"*50)
                print(checkout_logo)
                money=int(input("Give the money: "))

                if money==menu[order]["cost"]:
                    coffee_preaparing_screen()
                    order_or_finish_function()
                    reduce_supplies()
                    BOX+=menu[order]["cost"]  # To add costs inside box variable
                elif money>menu[order]["cost"]:
                    print("\n"*50)
                    print(extra_logo)
                    print("you gived eksta money")
                    extra_money_question=input("Do you wanna take that extra money? To yes write: y , To no write: n ").lower()
                    if extra_money_question=="y":
                        coffee_preaparing_screen()
                        reduce_supplies()
                        order_or_finish_function() 
                        BOX+=menu[order]["cost"]    
                    elif extra_money_question=="n":   # you can use else but I think elif is much more readable and I prefer to use it
                        print("\n"*50)
                        print(thanks_logo)
                        print("Thanks for extra money")
                        time.sleep(3)
                        coffee_preaparing_screen()
                        reduce_supplies()
                        order_or_finish_function()
                        BOX+=money
                elif money<menu[order]["cost"]:
                    print("\n"*50)
                    print(not_enough)
                    print("You gived some money but its not enough to your coffee")
                    print("We refunded your money")
                    try_again=input("Do you wanna try again: To yes write: y , To no write: n ").lower()
                    if try_again=="y":
                        print("\n"*50)
                        print(checkout_logo)
                        give_money_again=int(input("give money: "))
                        if menu[order]["cost"]==give_money_again:
                            coffee_preaparing_screen()
                            reduce_supplies()
                            order_or_finish_function()
                            BOX+=menu[order]["cost"]     
                        else:
                            print("\n"*50)
                            print(sorry_logo)
                            print("Sorry I cant give your coffee")
                            time.sleep(3)
                            order_or_finish_function()
                    else:
                        print("\n"*50)
                        print(bye_bye_logo)
                        time.sleep(3)
            else:
                print("\n"*50)
                print(ask_for_help_logo)
                print("Sorry I don't have enough supply to give you coffee")
                do_you_wanna_talk_to_staff_question=input("Do you want to talk with stuff to solve the problem? To yes write: y , To no write: n : ").lower()
                if do_you_wanna_talk_to_staff_question=="y":
                    print("\n"*50)
                    print(supply_adding)
                    time.sleep(3)
                    # To determine new measures 
                    ware_house["water"]=400
                    ware_house["milk"]=300
                    ware_house["coffee"]=200
                    ware_house["tea"]=200
                else:
                    print("\n"*50)
                    print(sorry_logo)
                    print("Sorry I can't have enough supply because of that I cant give you your coffee")
                    time.sleep(3)











def main_page_function():
    global order,MAIN_PAGE_LOOP    # We are inside a function and if we want to use this variables we should use this method

    
    while MAIN_PAGE_LOOP:  # While true
                print("\n"*50)
                print(main_page_logo)
                print("To see beverages and prices page write : 1\nTo see technical questions page write: 2\nTo see order page write: 3")
                page_question=input("\nwhich page do you wanna see? ")
                if page_question=="1":
                    print("\n"*50)
                    print(beverages_and_price_logo)
                    print("\nEspresso: 30$\nLatte: 30$\nCappuccino: 30$\nturkish coffee: 30$\n")  # \n means new line
                    input("Press enter to the main page...")

            

                elif page_question=="2": 
                    technical_page_loop=True      # To create an infinitive loop
                    while technical_page_loop:    # While true
                        print("\n"*50)
                        print(technical_questions_logo)
                        print("To see box write: box\nto see warehouse write: warehouse\nTo turn off the machine write: off\nTo turn main page write: main page")
                        technical_questions=input("\nwhat's your choice: ").lower()

                        # To turn off machine
                        if technical_questions=="off":   
                            print("\n"*50)
                            print(off_logo)
                            print("Machine is off")
                            technical_page_loop=False   # To stop loop
                            MAIN_PAGE_LOOP=False        # To stop loop
                        # To see the box
                        elif technical_questions=="box":  
                            print("\n"*50)
                            print(box_symbol)
                            print(f"box: {BOX}$")
                            input("\nPress enter to the Technical page...")
                        # To see warehouse
                        elif technical_questions=="warehouse":
                            print("\n"*50)
                            print(ware_house_logo)
                            print(f"Water: {ware_house["water"]}\nMilk: {ware_house["milk"]}\nCoffee: {ware_house["coffee"]}")
                            input("\nPress enter to the Technical page...")
                        elif technical_questions=="main page":
                            technical_page_loop=False   # To stop loop
                

                if page_question=="3":
                    print("\n"*50)
                    print(choose_logo)
                    print("-to drink espresso write: espresso\n-to drink latte write: latte\n-to drink cappuccino write: cappuccino\n-To drink turkish coffee write: turkish coffee")
                    order=input("\nWhat's your choice:")
                    control()  # To run function

main_page_function()  # To run function
                        



                