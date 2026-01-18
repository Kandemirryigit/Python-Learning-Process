#İs the year a leap year or not

from art import is_leap_year_logo,year_logo,leap_year_logo,not_leap_year_logo  # To import our logos from art.py to main.py
import time  # to use time module firstly we should import it


""" if year%4=0 and year%100!=0 year is a leap year
    if year%400=0 year is a leap year
    if year%100!=0 and year%400==0 year is a leap year """


def count_down():
     for i in range(2,0,-1):  # (from 2 , to 0 ,count -1)
        time.sleep(1)        # Wait 1 second before make other operation

def start_again():
    count_down()
    print("\n"*50)


print("\n"*50) # To create a fresh screen
print(is_leap_year_logo)  
count_down()  # To run count_down() function
print("\n"*50)


while True:
    
    print(year_logo)
    year=int(input("Write a year? "))  # İnput's default data type is str but I need a int data type because of that I added int before input
    
    if year%4==0 and year%100!=0:
        print("\n"*50)
        print(leap_year_logo)
        start_again()   # to run start_again() function
    elif year%400==0:
        print("\n"*50)
        print(leap_year_logo)
        start_again()
    elif year%100!=0 and year%400==0:
        print("\n"*50)
        print(leap_year_logo)
        start_again()
    else:
        print("\n"*50)
        print(not_leap_year_logo)
        start_again()

        
    





   