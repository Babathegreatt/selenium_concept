import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.db4free.net/")

#driver.find_element(By.PARTIAL_LINK_TEXT, "phpMyAdmin").click()
driver.find_element(By.XPATH, "//b[contains(text(),'phpMy')]").click()

#print(driver.window_handles[0])

#Switch to second tab
driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.ID,"input_username").send_keys("mark")
driver.find_element(By.ID,"input_password").send_keys("welcome123")
driver.find_element(By.ID,"input_go").click()



time.sleep(2)
driver.close()

time.sleep(2)
#driver.quit()
driver.quit()