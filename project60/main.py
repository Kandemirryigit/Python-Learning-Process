from bs4 import BeautifulSoup
import requests
import smtplib


MY_EMAIL = "kyigit293@gmail.com"
MY_PASSWORD = "ppunsiwcrftcvwml"
TO_EMAIL="kandemirryigit@gmail.com"

response=requests.get("https://www.trendyol.com/mavi/logo-baskili-yesil-tisort-slim-fit-dar-kesim-065781-81570-p-799002255?boutiqueId=61&merchantId=63&v=group-l")
soup=BeautifulSoup(response.text,"html.parser")


price=soup.find(class_="prc-dsc").text
price2=price.replace("TL","")
price3=float(price2.replace(",","."))


if price3<330:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg="the price of T-shirt is under 330 TL you can look it"
        )

