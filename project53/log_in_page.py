from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME="kandemirryigit"
PASSWORD="Asdfgh1903."

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome()
driver.get("https://www.instagram.com/?flo=true")



username_text=driver.find_element(By.NAME,"username")
username_text.send_keys(USERNAME)

password_text=driver.find_element(By.NAME,"password")
password_text.send_keys(PASSWORD)

login_text=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button')
login_text.click()


input()