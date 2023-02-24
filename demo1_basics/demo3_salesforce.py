import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")

#Enter First Name, work email

driver.find_element(By.NAME, 'UserFirstName').send_keys('John')
driver.find_element(By.NAME, 'UserEmail').send_keys('john.wick@mustang.com')

#Select dropdown

select_job= Select(driver.find_element(By.NAME,'UserTitle'))
select_job.select_by_visible_text('IT Manager')

select_employees = Select(driver.find_element(By.NAME,'CompanyEmployees'))
select_employees.select_by_visible_text('101 - 500 employees')

#Click checkbox and start my free trial

driver.find_element(By.XPATH,"//div[@class='checkbox-ui']").click()
driver.find_element(By.NAME,'start my free trial').click()

time.sleep(3)




