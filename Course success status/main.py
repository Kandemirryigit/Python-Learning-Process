
from art import *  # From art.py import evertyhing 
import time  # To use time module firstly we should import it


def inavlid_note():
    print("\n"*50)
    print(invalid_logo)
    input("You wrote Invalid first or second exam note.Press Enter to write again...")


def not_succesful():
    print("\n"*50)
    print(not_succesful_logo)
    print(f"Avarege not: {total_note} Not Succesful!\n")


is_program_on=True  # To create a loop a created this variable

while is_program_on:

    print("\n"*50)
    print(course_succes_status_logo)
    time.sleep(2)  # wait 2 seconds before make other operation


    while True:  # to create a loop
        
        print("\n"*50)
        print(first_note_logo)
        first_exam=int(input("What is your first exam note: "))
        print("\n"*50)
        print(second_note_logo)
        second_exam=int(input("What is your second exam note: "))

        if (first_exam >= 0 and first_exam <= 100) and (second_exam <= 100 and second_exam >= 0):
            break  # To get out from while loop
        else:
            inavlid_note()
        


    first_exam_main_note=first_exam*0.3    # first exam is valid %30 
    second_exam_main_note=second_exam*0.7  # Second exam is valid %70
    total_note=first_exam_main_note+second_exam_main_note
    after_first_exam=60-first_exam_main_note  # If you wanna be succesful your total note is going to be equal or greather than 60
    what_should_you_take_from_second_exam=int(after_first_exam*10/7)  # to determine what you should take second exam to be succesful

        

    if total_note<50:
        not_succesful()
        print(f"you should have taken {what_should_you_take_from_second_exam} from second exam to be succesful.")
        time.sleep(3)
        print("\n"*50)
        print(question_logo)
        third_exam_question=input("\nAre you gonna take third exam? (y/n) : ").lower()  # Whatever you write is going to be all lowercase
        if third_exam_question=="n":
            not_succesful()
            print(sorry_for_you_logo)
            break  # To get out from while loop
            

        while True:
            print("\n"*50)
            print(third_note_logo)
            third_exam=int(input("What is your third exam note: "))
            if third_exam<100 and third_exam>0:
                break # To get out from while loop
            else:
                inavlid_note()
            
        last_total_note=int(first_exam_main_note+third_exam*0.7)   # Third exam is valid %70
        if last_total_note<50:
            print("\n"*50)
            print(not_succesful_logo)
            print(f"Avarege note: {last_total_note} Not Succesful!")
            break  # To get out from while loop

        else:
            print("\n"*50)
            print(succesful_logo)
            print(f"Avagare note: {last_total_note} Succesful")
            break  # To get out from while loop

    else:
        print("\n"*50)
        print(succesful_logo)
        print(f"Avagere note: {total_note} Succesful")
        break  # To get out from while loop


