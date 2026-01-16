# Calculator


from art import *   # From art.py import everything to main.py 
import time         # To use time module firstly we should import it
RESULT=0            # The first result is equal zero because we didn't make any operation



def count_down():
    for i in range(3,0,-1):   # ( from 3 , to 0 , count -1)
        time.sleep(1)         # wait 1 minute before make other operation



def summation():
    global RESULT           # I added this in every function because RESULT is a global variable and if I wanna use that inside my functions I should use this method
    RESULT=number1+number2

def subtraction():
    global RESULT
    RESULT=number1-number2

def multiple():
    global RESULT
    RESULT=number1*number2

def division():
    global RESULT
    RESULT=number1/number2

def exponential_operations():
    global RESULT
    RESULT=number1**number2

def remainder():
    global RESULT
    RESULT=number1%number2

def quotient():
    global RESULT
    RESULT=number1//number2





print("\n"*50)
print(calculator_logo)
print("Welcome to the Calculator")
count_down()
print("\n"*50)
print(operations_logo)
print("\n-Summation(+)\n-Substraction(-),\n-Multiple(*)\n-Division(/)\n-Exponent(**)\n-Remainder(%)\n-Quotient(//)\n")   # \n means new line


number1=float(input("number1: "))   # Input's default data type is str but I need float  because of that I converted it to float
operation=input("operation: ")
number2=float(input("number2: "))


if operation=="+":
    summation()
elif operation=="-":
    subtraction()
elif operation=="*":
    multiple()
elif operation=="/":
    division()
elif operation=="**":
    exponential_operations()
elif operation=="%":
    remainder()
elif operation=="//":
    quotient()



is_play_on=True   # To create an infinitive loop

while is_play_on:
    Result_or_cont=input("\nTo see Result: result , To Reset: reset , To contiune: cont :").lower()   # Whatever you write is going to be lowercase because I added .lower() method

    if Result_or_cont=="result":
        print(f"Result: {RESULT}") 
    elif Result_or_cont=="reset":
        RESULT=0   
        print(f"Result: {RESULT}")
    else:
        operation=input("Operation: ")
        number=float(input("Number: "))
        if operation=="+":
            RESULT=RESULT+number
        elif operation=="-":
            RESULT=RESULT-number
        elif operation=="*":
            RESULT=RESULT*number
        elif operation=="/":
            RESULT=RESULT/number
        elif operation=="**":
            RESULT=RESULT**number
        elif operation=="%":
            RESULT=RESULT%number
        elif operation=="//":
            RESULT=RESULT//number







