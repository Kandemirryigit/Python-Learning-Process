from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome()
driver.get("https://www.python.org/")

events=[]

i=1
while i<=5:
    event=driver.find_element(By.XPATH,f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]').text
    events.append(event)
    i+=1

cleaned_events=[item.replace("\n"," ") for item in events]

i=1
with open("C:/Users/CASPER/Desktop/python_projects/project53/events.txt","a") as file:
    for event in cleaned_events:
        file.write(f"{i}-) {event}"+"\n")
        i+=1
    


driver.quit()





