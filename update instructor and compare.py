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

#Click Instructor
instructor=driver.find_element(By.LINK_TEXT,value="Instructors")
instructor.click()
time.sleep(5)

#Update Instructor
driver.find_element(By.XPATH,value="/html/body/table[2]/tbody[1]/tr/td/div/table/tbody/tr/td/table/tbody/tr/td/div/table[2]/tbody/tr/td/div/table/tbody/tr[10]/td[3]/div[2]/a/img").click()
time.sleep(3)

driver.find_element(By.NAME,value="Fname").clear()
driver.find_element(By.NAME,value="Fname").send_keys("Tic")
fname=driver.find_element(By.NAME,value="Fname").get_attribute("value")
print("First name entered is:",fname)
time.sleep(3)

driver.find_element(By.NAME,value="Lname").clear()
driver.find_element(By.NAME,value="Lname").send_keys("Tac")
lname=driver.find_element(By.NAME,value="Lname").get_attribute("value")
print("Last name entered is:",lname)
time.sleep(3)

#Click Update button
driver.find_element(By.NAME,value="submit").click()
time.sleep(5)
textupdated=driver.find_element(By.XPATH,value="/html/body/table[2]/tbody[1]/tr/td/div/table/tbody/tr/td/table/tbody/tr/td/div/table[2]/tbody/tr/td/div/table/tbody/tr[14]/td[3]/div[2]/a/img").text
if(textupdated=="Tic Tac"):
    print("Test case passed")
else:
    print("TC failed")
time.sleep(8)