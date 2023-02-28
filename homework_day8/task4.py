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

driver.find_element(By.ID,"id24_344").click()
driver.find_element(By.ID,"id1").send_keys("Dan")
driver.find_element(By.ID,"id2").send_keys("Brown")
driver.find_element(By.ID,"id10").send_keys("Engineer")

driver.find_element(By.ID,"id195").send_keys("www.getIN.com")
driver.find_element(By.ID,"id3").send_keys("EPFO")
driver.find_element(By.ID,"id11").send_keys("9999999999")

country_name=Select(driver.find_element(By.ID,"id7"))
country_name.select_by_value("189")

driver.find_element(By.ID,"id6").send_keys("chennai")
time.sleep(2)
driver.find_element(By.ID,"id339_2327").click()
driver.find_element(By.XPATH,"//input[@value='Submit']").click()

msg=driver.find_element(By.XPATH,"//li[text()='Email Address is required.']").text
print(msg)




time.sleep(5)
driver.quit()