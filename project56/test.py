from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instagram credentials
USERNAME = "kandemirryigit"  # Replace with your Instagram username
PASSWORD = "Asdfg1903."  # Replace with your Instagram password

# Initialize WebDriver
driver = webdriver.Chrome()

# Go to Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# Wait for username field to be present and log in
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
driver.find_element(By.NAME, "username").send_keys(USERNAME)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

# Wait for the inbox link to appear (login successful)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='/direct/inbox/']"))
)

# Go to the direct messages page
driver.get("https://www.instagram.com/direct/inbox/")

# Wait for the conversation with the specific person to load
# Replace 'Person Name' with the actual name of the person you want to message
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Kerem Kurt')]"))
)

# Find the conversation and click it
conversation = driver.find_element(By.XPATH, "//span[contains(text(),'Kerem Kurt')]")
conversation.click()

# Wait for the message input field to be present
message_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Message...']"))
)

# Type and send the message
message_input.send_keys("Hello, this is a test message!")  # Replace with your desired message
message_input.send_keys(Keys.RETURN)  # Press Enter to send the message

# Optionally, you can wait a bit to see the result or close the driver
# WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "some_element_after_message_is_sent")))

# Close the browser after sending the message (optional)
# driver.quit()
