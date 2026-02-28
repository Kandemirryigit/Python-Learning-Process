#Password Generator

import random   # To use random module firstly we should import 
import time     # To use time module firstly we should import
from art import password_generator_logo,letter_logo,number_logo,symbol_logo,password_symbol  # To import our logos from art.py to main.py


letters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=["*","/","-","_","!","@","+","^","$","&","?","#"]


print("\n"*50)  # To create a fresh screen
print(password_generator_logo)
my_time=2   # I wanted to create this variable because in my opinion the code is much more readable like this.you can directly write it in the range method
for i in range(my_time,0,-1):   # (from 2 , to 0 , count -1)
    time.sleep(1)   # Wait 1 minute before make other operation

print("\n"*50)
print(letter_logo)  # To show letter logo
letter_count=int(input("How many letters do you wanna use in your password? "))   # Input's default data type is string so I added int because ı need a number so integer not str

print("\n"*50)
print(number_logo)  # To show number logo
number_count=int(input("how many numbers do you wanna use in your password? "))   # Input's default data type is string so I added int because ı need a number so integer not str

print("\n"*50)
print(symbol_logo)  # To show symbol logo
symbol_count=int(input("How many symbol do you wanna use in your password? "))    # Input's default data type is string so I added int because ı need a number so integer not str


# I created this empty strings because ı'm going to add random things (random letters,random numbers,random symbols) here
# Actually the main idea of creating this ones is storing data
all_chracters=""
password=""


for i in range(letter_count):
    random_letter=random.choice(letters)
    all_chracters+=random_letter

for i in range(number_count):
    random_number=random.choice(numbers)
    all_chracters+=random_number

for i in range(symbol_count):
    random_symbol=random.choice(symbols)
    all_chracters+=random_symbol


lenght=len(all_chracters)  # To determine how many chrachter ı have
shuffled=random.sample(all_chracters,lenght)   # To create a random sequence between my random chosen chracters 
final_password=password.join(shuffled)         # To concenate strings 


print("\n"*50)
print(password_symbol)  # To show password symbol
print(f"your password: {final_password}")









    





















    







    




   