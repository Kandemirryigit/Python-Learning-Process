from selenium import webdriver
from selenium.webdriver.common.by import By
import pywhatkit as kit


PHONE_NUMBER="+905346246409"


chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome()
driver.get("https://www.getmidas.com/canli-borsa/?search=")

usd=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[4]/div[2]/a/div/span').text
eur=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[4]/div[3]/a/div/span').text
gold=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[4]/div[4]/a/div/span').text


result_usd=float(usd.replace(",","."))
result_eur=float(eur.replace(",","."))

gold2=gold.replace(",",".")
gold_parts=gold2.split(".")
result_gold=float(".".join(gold_parts[:2]))


if result_usd<40:
    kit.sendwhatmsg_instantly(PHONE_NUMBER,f"Usd: {result_usd}$")
if result_eur<45:
    kit.sendwhatmsg_instantly(PHONE_NUMBER,f"Eur: {result_eur}€")
if result_gold<4.150:
     kit.sendwhatmsg_instantly(PHONE_NUMBER,f"gold: {result_gold}TL")



