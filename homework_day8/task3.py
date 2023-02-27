import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.online.citibank.co.in/")

if driver.find_element(By.XPATH,"//a[@title='Close']"):
    driver.find_element(By.XPATH,"//a[@title='Close']").click()

time.sleep(2)
driver.quit()