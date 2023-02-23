import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.facebook.com/")

# Click on create new account

driver.find_element(By.LINK_TEXT, "Create new account").click()

# Enter First name as john
driver.find_element(By.NAME, "firstname").send_keys("john")

# Enter last name
driver.find_element(By.NAME, "lastname").send_keys("wick")

# Enter Password
driver.find_element(By.ID, "password_step_input").send_keys("Thatis@12235")

# Click on radio button - custom
driver.find_element(By.XPATH, "//input[@value='-1']").click()
#//label[text()='Custom']
#Grouping of XPath - (//input[@name='sex'])[3]

driver.find_element(By.NAME, "websubmit").click()

time.sleep(5)
