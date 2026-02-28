from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()

# This is your real Chrome user data path
options.add_argument("user-data-dir=C:\\Users\\CASPER\\AppData\\Local\\Google\\Chrome\\User Data")

# Optional: Start maximized (just looks nicer)
options.add_argument("--start-maximized")

# Launch browser
driver = webdriver.Chrome(options=options)

# Go to YouTube Music — and you're already logged in!
driver.get("https://music.youtube.com")

wait=WebDriverWait(driver,10)


search_youtube= wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Şarkı, albüm, sanatçı veya podcast arayın']")))
search_youtube.clear()
search_youtube.send_keys("bozulmuş kalbim",Keys.ENTER)

time.sleep(3)

save= wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Oynatma listesine kaydet']")))
save.click()




input()

