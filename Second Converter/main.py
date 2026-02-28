from art import *   # From art.py import everything

is_convert_on=True  # To create loop

while is_convert_on:  # While True

    print("\n"*50) # To create a fresh screen
    print(seconds_logo)

    #I converted input's type int.Default is str
    second=int(input("Can you write how much seconds you wanna convert? : ")) 

    print("\n"*50)
    print(result_logo)

    hour=second//3600
    minute=int((second-hour*3600)/60)
    second=(second-minute*60)%60

    print(f"hour: {hour} minute: {minute} second: {second} ")
    input("\nPress enter to contiune... ")

    print("\n"*50)
    print(y_n_logo)

    # Whatever you write is going to be all lowercase because I added .lower method
    again_question=input("Do you wanna convert again? (y/n) : ").lower()
    if again_question=="n":
        print("\n"*50)
        print(bye_bye_logo)
        is_convert_on=False












