import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.automationworld.com/")
driver.find_element(By.LINK_TEXT,"Subscribe").click()

driver.switch_to.window(driver.window_handles[1])


time.sleep(5)
driver.quit()