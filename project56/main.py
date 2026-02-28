from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USERNAME="kandemirryigit"
PASSWORD="Asdfg1903."

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome()
driver.get("https://www.instagram.com/")

time.sleep(3)

username=driver.find_element(By.NAME,"username")
username.send_keys(USERNAME)

time.sleep(1)

password=driver.find_element(By.NAME,"password")
password.send_keys(PASSWORD)

time.sleep(1)

login=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]')
login.click()

time.sleep(5)

not_now=driver.find_element(By.CSS_SELECTOR,'.x173jzuc.x1yc6y37')
not_now.click()



time.sleep(10)

messages=driver.find_element(By.XPATH,"//a[@href='/direct/inbox/']")
messages.click()

time.sleep(5)


not_now2=driver.find_element(By.XPATH,"//*[text()='Şimdi Değil']")
not_now2.click()










input()