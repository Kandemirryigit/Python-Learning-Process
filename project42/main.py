import datetime as dt
import pandas
import smtplib
import random

birthdays_file=pandas.read_csv("C:/Users/CASPER/Desktop/python_projects/project42/birthdays.csv")

MY_EMAIL="kyigit293@gmail.com"
PASSWORD="swdfglhalxjkpoie" 

dad_mail=birthdays_file["email"][0]
mom_mail=birthdays_file["email"][1]
sister_mail=birthdays_file["email"][2]


now=dt.datetime.now()
month=now.month
day=now.day


month_of_bd_dad=birthdays_file["month"][0]
month_of_bd_mom=birthdays_file["month"][1]
month_of_bd_sister=birthdays_file["month"][2]


day_of_bd_dad=birthdays_file["day"][0]
day_of_bd_mom=birthdays_file["day"][1]
day_of_bd_sister=birthdays_file["day"][2]





with open("C:/Users/CASPER/Desktop/python_projects/project42/letter1.txt","r") as letter1:
    content=letter1.read()

with open("C:/Users/CASPER/Desktop/python_projects/project42/letter1.txt","a") as letter:
    if month==month_of_bd_mom and day==day_of_bd_mom:
        message=content.replace("NAME","Mom")
        with smtplib.SMTP("smtp.gmail.com") as connection:  
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=mom_mail,
                msg=f"Subject:Happy Birthday\n\n{message}" 
        )
    if month==month_of_bd_dad and day==day_of_bd_dad:
        message=content.replace("NAME","Dad")
        with smtplib.SMTP("smtp.gmail.com") as connection:  
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=dad_mail,
                msg=f"Subject:Happy Birthday\n\n{message}" 
        )
    if month==month_of_bd_sister and day==day_of_bd_sister:
        message=content.replace("NAME","Sister")
        with smtplib.SMTP("smtp.gmail.com") as connection:  
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=sister_mail,
                msg=f"Subject:Happy Birthday\n\n{message}" 
        )

 






    











































