from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import tkinter as tk
from tkinter import ttk

# Dictionary for brands and their XPaths
markalar = {
    'Mavi': '//*[@id="sticky-aggregations"]/div/div[3]/div[3]/div/div/div[1]/div/a/div[1]',
    'Angemiel': '//*[@id="sticky-aggregations"]/div/div[3]/div[3]/div/div/div[2]',
    'Lufian': '//*[@id="sticky-aggregations"]/div/div[3]/div[3]/div/div/div[2]',
    'Jack&jones': '//*[@id="sticky-aggregations"]/div/div[3]/div[3]/div/div/div[4]'
}



# Function when the search button is clicked
def search_action():
    global what,marka,min_price_result,max_price_result

    what = what_entry.get()
    marka = marka_combo.get()
    min_price_result = min_price_entry.get()
    max_price_result = max_price_entry.get()


    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach",True)

    driver=webdriver.Chrome()
    driver.get("https://www.trendyol.com/")

    time.sleep(3)


    search=driver.find_element(By.CLASS_NAME,"V8wbcUhU")
    search.send_keys(what,Keys.ENTER)

    time.sleep(3)

    marka_result=markalar[marka]

    marka=driver.find_element(By.XPATH,marka_result)
    marka.click()


    price=driver.find_element(By.XPATH,'//*[@id="sticky-aggregations"]/div/div[10]')
    price.click()

    time.sleep(5)

    min_price=driver.find_element(By.XPATH,'//*[@id="sticky-aggregations"]/div/div[10]/div[2]/div/input[1]')
    min_price.send_keys(min_price_result)

    max_price=driver.find_element(By.XPATH,'//*[@id="sticky-aggregations"]/div/div[10]/div[2]/div/input[2]')
    max_price.send_keys(max_price_result)

    button=driver.find_element(By.XPATH,'//*[@id="sticky-aggregations"]/div/div[10]/div[2]/div/button')
    button.click()

    time.sleep(3)

    lists=driver.find_element(By.XPATH,'//*[@id="search-app"]/div/div/div/div[2]/div[1]/div[2]/div/div')
    lists.click()

    min_price_button=driver.find_element(By.XPATH,'//*[@id="search-app"]/div/div/div/div[2]/div[1]/div[2]/div/ul/li[2]')
    min_price_button.click()


    input()


# GUI setup
root = tk.Tk()
root.title("Trendyol Scraper GUI")
root.geometry("400x320")

# What you wanna take
tk.Label(root, text="What you wanna take:").pack()
what_entry = tk.Entry(root, width=30)
what_entry.pack(pady=5)

# Which brand you wanna take
tk.Label(root, text="Which brand you wanna take:").pack()
marka_combo = ttk.Combobox(root, values=list(markalar.keys()), state="readonly")
marka_combo.pack(pady=5)
marka_combo.current(0)

# Min price
tk.Label(root, text="Min price:").pack()
min_price_entry = tk.Entry(root)
min_price_entry.pack(pady=5)

# Max price
tk.Label(root, text="Max price:").pack()
max_price_entry = tk.Entry(root)
max_price_entry.pack(pady=5)

# Search Button
search_button = tk.Button(root, text="Search", command=search_action)
search_button.pack(pady=10)

root.mainloop()









