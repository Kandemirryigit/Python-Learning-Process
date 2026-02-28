# Secret Auction Program

from art import *    # From art.py import everything inside main.py
import time   # To use time module firstly we should import it


anyone_else_loop=True  # To create an infinitive loop
bidder_names=[] # To store names
bid_prices=[]   # To store prices
is_program_on=True


while is_program_on:  # While True/False


    print("\n"*50)
    print(secret_auction_program_logo)
    time.sleep(3)  # Wait 3 seconds before make other operation
    print("\n"*50)


    while anyone_else_loop: # While True/False
            
            print(name_logo)
            bidder_name=input("What is your name: ")
            print("\n"*50)
            print(price_logo)
            bid_price=int(input("What is your price: $"))  # Input's default data type is str but I need int because of that I used int befor input
            bidder_names.append(bidder_name)  # To add bidder name inside bidder_names variable
            bid_prices.append(bid_price)      # To add price inside bid_prices variable
            print("\n"*50)
            print(anyone_else_logo)
            anyone_else_question=input("Are there anyone else to bid? (y/n) :").lower()   # Whatever you write is going to be all lowercase
            if anyone_else_question=="n":
                anyone_else_loop=False  # To stop loop
            else:
                 print("\n"*50)



    bids={}   # To store names and prices inside a dictionaray list
    for i in range(len(bidder_names)):
        bids[bidder_names[i]]=bid_prices[i]   # To create a key value pair

    max_key = max(bids,key=bids.get)
    max_value=bids[max_key]

    
    
    print("\n"*50)
    print(result_is_coming_logo)
    time.sleep(3)   # to wait 3 seconds before make other operation


    print("\n"*50)
    print(result_logo)
    print(f"{max_key}:{max_value}$")
    input("\nPress enter to see all bids...")


    print("\n"*50)
    print(bids_logo)
    for i in range(len(bidder_names)):
         print(f"{bidder_names[i]}: {bid_prices[i]}$")
    input("\nPress enter to continue...")


    print("\n"*50)
    print(restart_program_logo)
    restart_program_question=input("Do you wanna restart program? (y/n) : ").lower()  #whatever you write is going to be all lowercase
    if restart_program_question=="n":
         print("\n"*50)
         print(bye_bye_logo)
         is_program_on=False  # To stop loop
    else:
         anyone_else_loop=True  # To start this loop again
         bidder_names=[]        # To clear previous informations
         bid_prices=[]          # To clear previous informations
    




























































