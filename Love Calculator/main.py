# Love Calculator

from art import *   # From art.py import everything to main.py
import time         # To use time module we firstly import it


print("\n"*50)  # To show a fresh screen
print(love_calculator_logo)
time.sleep(3)   # To wait 3 seconds before make other operation


names=input("Could you write your own name and your girlfriend's name? ")

T=int(names.lower().count("t"))  # this means whatever you write inside names variable is gonna be lowercase and we will count how many t inside names variable
R=int(names.lower().count("r"))
U=int(names.lower().count("u"))
E=int(names.lower().count("e"))

total1=str(T+R+U+E)   # I converted this str becuase I need that for example str(10)+str(10)=1010 so I need this operation

L=int(names.lower().count("l"))
O=int(names.lower().count("o"))
V=int(names.lower().count("v"))
E=int(names.lower().count("e"))

total2=str(L+O+V+E)

print(f"\nT occurs {T} times")     # \n means create new line
print(f"R occurs {R} times")
print(f"U occurs {U} times")
print(f"E occurs {E} times\n")

print(f"L occurs {L} times")
print(f"O occurs {O} times")
print(f"V occurs {V} times")
print(f"E occurs {E} times\n")


input("To see your score type Enter ")

print("\n"*50)
print(love_score_is_coming_logo)
time.sleep(2)
print(f"yours love score is: {total1+total2} ")