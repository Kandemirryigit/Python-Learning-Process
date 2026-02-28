from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

content_portals=driver.find_element(By.LINK_TEXT,"Content portals")
content_portals.click()






input()