import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://github.com/login")

driver.find_element(By.ID, "login_field").send_keys("hello")
driver.find_element(By.ID, "password").send_keys("89hello")
driver.find_element(By.NAME, "commit").click()

time.sleep(2)
driver.quit()

