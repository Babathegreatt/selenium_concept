import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.openemr.io/b/openemr/")

driver.find_element(By.CSS_SELECTOR,"#authUser").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,"#clearPass").send_keys("pass")
select_lang=Select(driver.find_element(By.XPATH,"//select[@name='languageChoice']"))
select_lang.select_by_visible_text("English (Indian)")
driver.find_element(By.CSS_SELECTOR,"#login-button").click()

#Click on New Patient
driver.find_element(By.XPATH,"//div[text()='Patient']").click()
driver.find_element(By.XPATH,"//div[text()='New/Search']").click()

#Add first name

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@name='pat']"))
driver.find_element(By.ID,"form_fname").send_keys("Dave")
driver.find_element(By.ID,"form_lname").send_keys("Specter")

# Add DOB
driver.find_element(By.XPATH,"//input[@name='form_DOB']").send_keys("2023-03-01")

select_gender= Select(driver.find_element(By.XPATH,"//select[@name='form_sex']"))
select_gender.select_by_visible_text('Male')
driver.find_element(By.ID,"create").click()

driver.switch_to.default_content()

#Click on confirm new patient

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='modalframe']"))
driver.find_element(By.XPATH,"//input[@value='Confirm Create New Patient']").click()

driver.switch_to.default_content()

#wait for alert is present - Implicit wait

wait=WebDriverWait(driver,30)
wait.until(expected_conditions.alert_is_present())

#wait until element is located by ID
#wait.until(expected_conditions.visibility_of_element_located(By.ID,"email"))

actual_alert_text = driver.switch_to.alert.text
print(actual_alert_text)

driver.switch_to.alert.accept()

#handle birthday alert


time.sleep(5)
quit()