from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

MAIL="kyigit293@gmail.com"
PASSWORD="31cekenmartı"

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome()
driver.get("https://www.linkedin.com/feed/?trk=sem-ga_campid.19331681909_asid.168715020864_crid.698313460548_kw.linkedin_d.c_tid.kwd-148086543_n.g_mt.e_geo.9056770")

time.sleep(1)

mail=driver.find_element(By.ID,"username").send_keys(MAIL)
time.sleep(1)

password=driver.find_element(By.ID,"password").send_keys(PASSWORD)
time.sleep(1)

login=driver.find_element(By.CSS_SELECTOR,".btn__primary--large.from__button--floating").click()
time.sleep(3)

job=driver.find_elements(By.CSS_SELECTOR,'.HyRpFmCjAWIuRxNzmfOWKyciaWbRBoTwI')[3].click()
time.sleep(2)

search_click=driver.find_element(By.CSS_SELECTOR,'.basic-input.jobs-search-box__text-input.jobs-search-box__keyboard-text-input.jobs-search-global-typeahead__input')
search_click.click()
time.sleep(1)

search_write=driver.find_element(By.CSS_SELECTOR,'.basic-input.jobs-search-box__text-input.jobs-search-box__keyboard-text-input.jobs-search-global-typeahead__input')
search_write.send_keys("Python Developer",Keys.ENTER)
time.sleep(3)

publish_time=driver.find_element(By.ID,'searchFilter_timePostedRange').click()
time.sleep(3)

last_month=driver.find_elements(By.CSS_SELECTOR,'.search-reusables__value-label')[1].click()
time.sleep(2)

ok=driver.find_elements(By.CSS_SELECTOR,'.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.ml2')[0].click()
time.sleep(2)

experience=driver.find_element(By.ID,'searchFilter_experience').click()
time.sleep(2)

intern=driver.find_elements(By.CSS_SELECTOR,'.search-reusables__value-label')[4].click()
time.sleep(2)

ok2=driver.find_elements(By.CSS_SELECTOR,'.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.ml2')[1].click()
time.sleep(2)

easy_apply=driver.find_element(By.XPATH, '//*[@aria-label="Kolay Başvuru filtre."]')
easy_apply.click()
time.sleep(2)

input()