from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.ezhrs.com/project1/potdb/login.asp")
# username
driver.find_element(By.NAME,"username").send_keys("admin.admin")
#password
driver.find_element(By.NAME,"password").send_keys("welcome")
#Click login
driver.find_element(By.NAME,"SUBMIT").click()
time.sleep(35)
#Click the PO named TORcat2014-105 in the list seen
driver.find_element(By.LINK_TEXT,"TORgrm2014-123").click()
#edit and add the input text for purchase for:
Purchased_for=driver.find_element(By.NAME,"edt_Orderby")
Purchased_for.clear()
update1=driver.find_element(By.NAME,"edt_Orderby").send_keys("Niranjana")
update2=driver.find_element(By.NAME,"edt_Orderby").get_attribute("value")
print("Updated name is:",update2)
#Click submit button
driver.find_element(By.XPATH,"//input[@name='submit']")
