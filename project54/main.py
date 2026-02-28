from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(5)

language=driver.find_element(By.ID,"langSelect-EN")
language.click()

time.sleep(5)



while True:

    for i in range(70):
        cokkie=driver.find_element(By.ID,"bigCookie")
        cokkie.click()

    result=[]
    cokkies=driver.find_element(By.ID,"cookies").text
    result.append(cokkies)
    count_cokkies=float(result[0].split()[0])


    if count_cokkies<=200:
        cursor=driver.find_element(By.ID,"product0")
        cursor.click()
    elif count_cokkies>200 and count_cokkies<500:
        grandma=driver.find_element(By.ID,"product1")
        grandma.click()
    elif count_cokkies>500:
        farm=driver.find_element(By.ID,"product2")
        farm.click



    




