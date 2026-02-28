from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

search=driver.find_element(By.ID,"id-search-field")
search.send_keys("anan",Keys.ENTER)












