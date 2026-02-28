import pywhatkit as kit     # To send message from whatsapp web we need this 
from datetime import datetime   # To determine time we need this

PHONE_NUMBER=""  # You should write the phone number of the person you want to send a message to here.

now=datetime.now()  # To determine current time
hour=now.hour  # To determine hour
minute=now.minute  # To determine minute

if hour==8 and minute==00:  # If hour and minute is equal (which time you want you can determine it)
     kit.sendwhatmsg_instantly(PHONE_NUMBER,"Good morning babe Love you so much")  
