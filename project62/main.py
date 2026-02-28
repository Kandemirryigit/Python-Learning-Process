from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd




df=pd.read_csv("C:/Users/CASPER/Desktop/python_projects/project62/song_names2.csv").iloc[0:55]

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

wait=WebDriverWait(driver,10)


def close_window():
    main_window = driver.current_window_handle
    all_windows = driver.window_handles
    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(window)
            driver.close()

    driver.switch_to.window(main_window)


x=0
urls=[]
for index,row in df.iterrows():

    parts=row[0].split('-')
    new_song = '-'.join(parts[:-1])

    driver.get("https://www.youtube.com/?app=desktop&hl=TR")

    search_youtube= wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
    search_youtube.clear()

    search_youtube.send_keys(row[0],Keys.ENTER)
    
    
    try:
        music = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(@title, '{new_song}')]"))) 
        music.click()
    except:
        with open("C:/Users/CASPER/Desktop/python_projects/project62/youtube_error.txt","a",encoding="UTF-8") as file:
            file.writelines(f"{row[0]}\n")
        continue
        

    url=driver.current_url
    urls.append(url)
    
    driver2=driver.get("https://ytmp3.la/wCLi/")

    
    search_mp3 = wait.until(EC.presence_of_element_located((By.NAME, "v")))
    search_mp3.send_keys(urls[x])
    x+=1
    

    convert = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Convert']")))
    convert.click()
    
    
    try:
        download = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Download']")))
        download.click()
        close_window()
        
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']")))
        next_button.click()
        
    except:
        with open("C:/Users/CASPER/Desktop/python_projects/project62/ytpm3_error.txt","a",encoding="UTF-8") as file:
            file.writelines(f"{row[0]}\n")
        continue
        

    
input()
    





