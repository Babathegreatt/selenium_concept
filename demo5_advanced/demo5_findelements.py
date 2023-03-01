import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.google.com/")

elements = driver.find_elements(By.XPATH, "//a")

for element in elements:
    text = element.text
    print(text)
    hr=element.get_attribute("href")
    print(hr)


driver.quit()
