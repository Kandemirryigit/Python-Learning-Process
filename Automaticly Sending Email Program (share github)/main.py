# Automaticly Sending Email Program


import random  # To use random module firstly we should import it
import datetime as dt  # To use datetime module firstly we should import it and I didn' want to see it like datetime because of that I did import it as dt
import smtplib   # To use smtplib module firstly we should import it


"""The password variable is so much important if it not be true python is going to be show you erors.
and in this code the password is mine because of that this is not going to work in your mail addresses.
you have to take your own password.I explained how can you take your own password in the readme file."""


MY_EMAİL="kyigit293@gmail.com"  # This mail sends the message
PASSWORD="swdfglhalxjkpoie"   # This one is not gonna work in your code
recipients_mail="kandemirryigit@gmail.com"  # This mail takes the message



"""The path is not gonna run properly in your computer you have to write your own path to here"""

with open("C:/Users/CASPER/Desktop/python_projects/project42/quotes.txt") as quotes:  # To open quotes.txt file and close it automaticly.
    lines=quotes.readlines()  # To read all lines inside quotes file
    random_message=random.choice(lines)  # To choose a random line inside quotes file


my_message=random_message


"""Computer starts to count from zero because of that for example if the day is monday the output is going to be 0,
if the day is tuesday the output is going to be 1"""

now=dt.datetime.now()
day=now.weekday()


if day==0: # It means the day is monday
    with smtplib.SMTP("smtp.gmail.com") as connection:   # This section can be different if you are using hotmail or yahoo or other things
        connection.starttls()
        connection.login(user=MY_EMAİL,password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAİL,
            to_addrs=recipients_mail,
            msg=f"Subject:Monday Motivation\n\n{my_message}" 
    )












