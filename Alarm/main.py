# Alarm 

import time  # To use time module firstly we should import it
from art import *  # From art.py import everything 


print("\n"*50)
print(alarm_logo)
time.sleep(2)
print("\n"*50)
print(how_much_logo)
my_time=int(input("How much seconds you wanna set your alarm: ")) 
print("\n"*50)


for i in range(my_time,0,-1):  # (start,stop,count)
    seconds=i%60
    minutes=int(i/60)%60
    hours=int(i/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")   # :02 means show 2 chracter
    time.sleep(1)  # Wait 1 second before make other operation
print("Alarm!!! Alarm!!! Alarm!!! ")






