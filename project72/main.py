import pandas as pd
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
import os
from gui import run_gui

""" I didn't want to write all morse codes manually( because it's hard and maybe I can write it false -they semms same-) 
to the my csv file because of that I used beautifulSoup to web scraping.I took the alphabet from the web."""

BASE_PATH="C:/Users/CASPER/Desktop/python_projects/project72/"
CSV_PATH=BASE_PATH+"mors_alphabet.csv"



if not os.path.exists(CSV_PATH):

    print("Csv not found.Scraping website...")

    response=requests.get("https://wildwalks.com/bushcraft/technical-stuff/morse-code-and-phonetic-alphabet.html")
    soup=BeautifulSoup(response.text,"html.parser")

    alphabet=[]
    morse_codes=[]
    clean_morse_codes=[]

    letters_in_site=soup.find_all(class_="xl26")
    morse_codes_in_site=soup.find_all(class_="xl27")

    for letters in letters_in_site:
        alphabet.append(letters.text)

    # This loop gives me the list like this: ['·/xa0–', '–\xa0·\xa0·\xa0·', '–\xa0·\xa0–\xa0·', '–\xa0·\xa0·']
    for codes in morse_codes_in_site:
        morse_codes.append(codes.text)

        
    # This loop for clean the list from /xa0 chracters 
    for code in morse_codes:
        cleaned=code.replace("\xa0","") 
        clean_morse_codes.append(cleaned)

    
    df=pd.DataFrame({"chars":alphabet,"morse_code":clean_morse_codes}) # "chars" and "morse_code" is the name of the column
    # If you want to apply this code to your computer you gotta change this path.This path is special for my computer
    df.to_csv(CSV_PATH,index=False)  
    df2=pd.read_csv(CSV_PATH)

    # I added this chracters manually because in the web site we scraped this chracters doesen't exist
    new_data=[
            {"chars":" ","morse_code":" "},
            {"chars":"?","morse_code":" ..--.."},
            {"chars":"=","morse_code":"-...-"},
            {"chars":",","morse_code":"--..--"},
            ]
    df2=df2._append(new_data, ignore_index=True)
    df2.to_csv(CSV_PATH, index=False)


else:
     print("Csv already exist.Skipping web scraping")
     

run_gui()







