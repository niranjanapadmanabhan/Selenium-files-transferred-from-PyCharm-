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
driver.find_element(By.XPATH,value="/html/body/table[2]/tbody[1]/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/div/table[3]/tbody[1]/tr/td/table/tbody/tr[5]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/a").click()
time.sleep(10)
#Click the edit student button

driver.find_element(By.LINK_TEXT,value="Edit Student").click()
time.sleep(10)
last_name=driver.find_element(By.NAME,value="Lname").get_attribute('value')  #Always make sure to add the get_attribute along with driver.ind element statement..
print("Printing lastname:",last_name)
if(last_name=='N'):
    print("TC passed")
else:
    print("Test case failed")
driver.quit()