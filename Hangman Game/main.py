#Guess random word Game 

import random      # To use random module firstly we should import it
import time
from art import *  # From art.py import everything
LIVES=6            # I chose to create this global variable because if you wanna change this variable you can easily do from top of the page 
IS_GAME_ON=True    # To create an infinitive loop


correct_letters=[]
words=["apple","banana","cherry","car","bus","ball","child","person","headphone","phone","computer","engineer"]
random_word=random.choice(words)   # To choose a random index from words list
lengt_of_random_word=len(random_word)  # To determine word's lenght
words_str=",".join(words)  # To convert our list's chracters str



def count_down():
   for i in range(3,0,-1):  # ( from 3 , to 0 , count -1)
      time.sleep(1)         # wait 1 minute before make other operation



def play_again():
   global display,correct_letters,LIVES,IS_GAME_ON,random_word   # We are inside a function because of that we should take inside the variables outside 
   wanna_play_again_question=input("Do you wanna play again? (yes/no): ").lower()  # Whatever you write is going to be lowercase because I added .lower() method
   if wanna_play_again_question=="yes":
      display=""  # To create an empty string
      correct_letters=[]  # To create an empty list
      LIVES=6
      random_word=random.choice(words)
      starting_screen()
      descriptions()
   elif wanna_play_again_question=="no":   # you can use else its optional but in my opinion elif is much more readable
      print("\n"*50)
      print(game_over_logo)
      IS_GAME_ON=False  # To stop loop
     


# I created this function because I used same things in the play again function too and I don't wanted to be write same things again and again
def starting_screen():
   print("\n"*50)
   print(hangman_game_logo)
   count_down()
   print("\n"*50)
   print(words_logo)
   print(words_str)
   count_down()
   print("\n"*50)
   print(guess_logo)
   print("_ "*lengt_of_random_word)  # İf you look carefully you can see there is a space after (_) I did it because I wanna take this output( _ _ _ _ ) not this (_____)


starting_screen()  # to run function


# I created this function because I wanted to give hints about the word
def descriptions():
   if random_word=="apple":
      print("\n-It's a fruit.\n-It has green,yellow,red colors\n")
   elif random_word=="banana":
      print("\n-It's a fruit.\n-It's color is yellow\n")
   elif random_word=="cherry":
      print("\n-It's a fruit.\n-It's color is red\n")
   elif random_word=="car":
      print("\n-It's a vehicle.\n-It mostly can carry 5 people\n")
   elif random_word=="bus":
      print("\n-It's a vehicle.\n-It's uses for public transport\n")
   elif random_word=="ball":
      print("\n-It's a thing.\n-We can play a lot of game with this thing(football,basketball...)\n")
   elif random_word=="child":
      print("\n-It's a human.\n-It's little human\n")
   elif random_word=="person":
      print("\n-It's a thing.\n-For example you are this thing\n")
   elif random_word=="headphone":
      print("\n-It's a thing.\n-You can listen something with this thing\n")
   elif random_word=="phone":
      print("\n-It's a thing.\n-you are using this thing every day\n")
   elif random_word=="computer":
      print("\n-It's a thing.\n-It works with 0 and 1\n")
   elif random_word=="engineer":
      print("\n-It's a job.\n-they are intelligent and so cool :)\n")

descriptions()  # To run function



while IS_GAME_ON:  # While True

   display=""

   guess_letter_or_word=input("guess a letter or word: ")
   print("\n"*50)


   if guess_letter_or_word in correct_letters:
      print(f"you have already guessed {guess_letter_or_word},please guess another letter\n")
      

   
   for letter in random_word:
      if letter==guess_letter_or_word:
         display+=letter  # To add letter to the display string
         correct_letters.append(letter)
      elif letter in correct_letters:
         display+=letter  # To add letter to the display string
      else:
         display+=" _"  # To add _ to the display string
   print(display)


   if guess_letter_or_word not in random_word:
      LIVES-=1    # İf I guess wrong letter or word I'll lose a life
      print(f"********** {LIVES} ********")
   if "_" not in display or guess_letter_or_word==random_word:   # this means you knew the word correct
      print("\n"*50)
      print(correct_logo)
      print(f"The word {random_word}.You guessed correct")
      count_down()
      play_again()
   if LIVES==0:
      print(lives_0_logo)
      print(f"you lost.the man died. The word was {random_word.upper()}")  # I added .upper() method the word is going to be seem full uppercase
      play_again()
   if guess_letter_or_word in random_word and IS_GAME_ON==True:  # If I don't add if IS_GAME_ON==True then if I answer no the wanna play question then the print is going to run
      print(f"******** {LIVES} *******")


   if IS_GAME_ON==True:  # If I dont add this block here and if I answer no the  wanna play again question then a logo going to run.
      if LIVES==6:
         print(lives_6_logo)
      elif LIVES==5:
         print(lives_5_logo)
      elif LIVES==4:
         print(lives_4_logo)
      elif LIVES==3:
         print(lives_3_logo)
      elif LIVES==2:
         print(lives_2_logo)
      elif LIVES==1:
         print(lives_1_logo)
         



   
   







         



      













   

















   






