import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

#Enter email and password.
driver.find_element(By.ID,"email").send_keys("hello123@fb.com")
driver.find_element(By.ID,"pass").send_keys("hello")

#CLick on Login
driver.find_element(By.NAME,"login").click()

time.sleep(5)

driver.quit()

