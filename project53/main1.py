from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome()
driver.get("https://www.amazon.com.tr/Instant-Pot-110-0045-01-EU-Paslanmaz-%C3%87elik/dp/B0979HTPDQ/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.Eeei7InJLnlmlw1sMmA_Z4SHVYkPXSzVs0gufyCUNZPLXQIMdPui0E7UsLKw-HoWiwAiDZ9aXDQaaVM-jSW3Ex8zOO6U631vifJRbhR4wmF5GX8A3_aWH0ipCiDazogASyHK8ZKDoyuWoostjhAEYqJ-YD4NNDuJdAwx7gWaBxWoYt03ms9HcEoHWyfuF9oUCWdykP9yan8W_t1Hj-e0fWgyaPhCb0vRAIh2SelgIU6Fo9GZ_V9XWfIg5pbUw7Q0vJZOqBMnIrqGS5hXjizvmjLICR_bcT8Bgfw0qF2YrIo.Tm4DbFI6LH7W3RWePu0Ry3dI8geXjk6qGwQ1jVb-yOs&dib_tag=se&keywords=electric%2Bpressure%2Bcooker&qid=1744408693&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

price_dollar_whole=driver.find_element(By.CLASS_NAME,"a-price-whole")
print(f"Price is: {price_dollar_whole.text} TL ")


driver.quit()








