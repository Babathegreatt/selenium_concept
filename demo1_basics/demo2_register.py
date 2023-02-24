import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

driver.find_element(By.NAME, "reg_email__").send_keys("wick@123.com")
driver.find_element(By.NAME, "reg_email_confirmation__").send_keys("wick@123.com")

# Enter Password
driver.find_element(By.ID, "password_step_input").send_keys("Thatis@12235")

# Click on radio button - custom
driver.find_element(By.XPATH, "//input[@value='-1']").click()
#//label[text()='Custom']
#Grouping of XPath - (//input[@name='sex'])[3] ##

#Select from Dropdown

select_day = Select(driver.find_element(By.ID,"day"))
select_day.select_by_visible_text('20')

select_month = Select(driver.find_element(By.ID,"month"))
select_month.select_by_visible_text('May')

select_year = Select(driver.find_element(By.ID,"year"))
select_year.select_by_visible_text('2000')

select_pronoun = Select(driver.find_element(By.NAME,"preferred_pronoun"))
select_pronoun.select_by_visible_text('He: "Wish him a happy birthday!"')

time.sleep(3)

#CLick on Sign Up
driver.find_element(By.NAME, "websubmit").click()

time.sleep(10)
driver.quit()