from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.get("http://www.ezhrs.com/ezCourses/admin/admin.asp?action=admin")

#Finding the element for username
username=driver.find_element(By.NAME,value="uname")
#Typing admin for username
username.send_keys("admin")

#Finding element for password
password=driver.find_element(By.NAME,value="password")
#Typing pass for password
password.send_keys("pass")

#Finding element for Login button
login=driver.find_element(By.NAME,value="SUBMIT")
#To click the button login
login.click()

#Click on Students
std=driver.find_element(By.LINK_TEXT,value="Students")
std.click()

time.sleep(3)

#Select the added student and click it . Please note the selector has space in name, so use partial xpath or full xpath.
a=driver.find_element(By.CSS_SELECTOR,value="body > table:nth-child(5) > tbody:nth-child(1) > tr > td > table:nth-child(11) > tbody > tr > td > table > tbody > tr > td > div > table:nth-child(9) > tbody:nth-child(1) > tr > td > table > tbody > tr:nth-child(5) > td > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr > td > a")
a.click()
time.sleep(10)
#Click the edit student button

driver.find_element(By.LINK_TEXT,value="Edit Student").click()
time.sleep(10)
last_name=driver.find_element(By.NAME,value="Lname").get_attribute('value')  #Always make sure to add the get_attribute along with driver.find element statement..
print("Printing lastname:",last_name)
if(last_name=='N'):
    print("TC passed")
else:
    print("Test case failed")
driver.quit()