from art import *  # From art.py import everything

g=9.81

is_operation_on=True  # To create loop

while is_operation_on:  # While True

    # I changed imputs type float.Default is string

    print("\n"*50)
    print(start_x_logo)
    start_x=float(input("What is start x coordinate: "))
    print("\n"*50)
    print(start_y_logo)
    start_y=float(input("What is start y coordinate: "))
    print("\n"*50)
    print(speed_x_logo)
    speed_x=float(input("what is speed of x coordinate: "))
    print("\n"*50)
    print(speed_y_logo)
    speed_y=float(input("what is speed of y coordinate: "))
    print("\n"*50)
    print(how_much_time_logo)
    how_much_time_passed=float(input("How much time passed (second)? "))

    # Those are formul you should know physics to write this ones
    result_x=start_x+(speed_x*how_much_time_passed)
    result_y=start_y+(speed_y*how_much_time_passed-(g*how_much_time_passed**2)/2)

    print("\n"*50)
    print(result_logo)

    print(f"last x corrdinate: {result_x}\nlast y coordinate: {result_y}")
    input("\nPress enter to contioune...")
    
    print("\n"*50)
    print(y_n_logo)

    # Whatever you write is going to be all lowercase
    question=input("do you wanna make another operation? (y/n) : ").lower()
    if question=="n":
        print("\n"*50)
        print(bye_bye_logo)
        is_operation_on=False  # To stop loop
        

