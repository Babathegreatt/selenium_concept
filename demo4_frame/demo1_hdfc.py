import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://netbanking.hdfcbank.com/netbanking/")

#switch to frame
#//frame[contains(@src, 'RSNBLogin.html?v=13')]
driver.switch_to.frame(driver.find_element(By.XPATH,"//frame[@name='login_page']"))

driver.find_element(By.NAME,"fldLoginUserId").send_keys("test123")
driver.find_element(By.XPATH,"//a[text()='CONTINUE']").click()

#switch to main html

driver.switch_to.default_content()

time.sleep(2)
driver.quit()


