import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.oracle.com/in/database/")

driver.find_element(By.XPATH,"//span[text()='View Accounts']").click()
#driver.find_element(By.ID,"acctBtnLabel").click()

#driver.find_element(By.XPATH," //a[text()='Sign-In']").click()
driver.find_element(By.XPATH,"  //a[@data-lbl='profile:sign-in-account']").click()

driver.get("https://login.oracle.com/mysso/signon.jsp")

print(driver.title)
print(driver.current_url)

driver.find_element(By.ID,"ssousername").send_keys("john")
driver.find_element(By.ID,"ssopassword").send_keys("john123")
driver.find_element(By.ID,"signin_button").click()

time.sleep(2)
driver.quit()