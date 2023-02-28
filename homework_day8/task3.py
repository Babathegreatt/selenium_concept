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

driver.find_element(By.XPATH, "//img[@title='LOGIN NOW']").click()
driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH,"//div[@onclick='ForgotUserID();']").click()

driver.find_element(By.XPATH,"//a[text()='select your product type']").click()
driver.find_element(By.XPATH,"//a[text()='Credit Card']").click()


driver.find_element(By.CSS_SELECTOR,'#citiCard1').send_keys("4545")
driver.find_element(By.CSS_SELECTOR,"input[name='citiCard2']").send_keys("7897")
driver.find_element(By.CSS_SELECTOR,"[name='citiCard3']").send_keys("7897")
driver.find_element(By.ID,"citiCard4").send_keys("9998")

driver.find_element(By.NAME,"CCVNO").send_keys("123")

driver.find_element(By.NAME,"DOB").click()

#approach 1 - enter date directly not working
# d.find_element(By.ID,"bill-date-long").send_keys("14/04/2022")

#approach 2 to select date.
# select_year=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
# select_year.select_by_visible_text("2022")
# select_month=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
# select_month.select_by_visible_text("Apr")
# driver.find_element(By.PARTIAL_LINK_TEXT,"14").click()

#approach 3 - javascript
driver.execute_script("document.querySelector('#bill-date-long').value='11/09/2000'")

#ele1= driver.find_element(By.XPATH,"//input[@name='DOB']")
#driver.execute_script("arguements[0].value='11/09/2000'", ele1)

driver.find_element(By.XPATH,"//input[@value='PROCEED']").click()


text=driver.find_element(By.XPATH,"//li[contains(text(),'Terms)']").text
print(text)

time.sleep(5)
driver.quit()