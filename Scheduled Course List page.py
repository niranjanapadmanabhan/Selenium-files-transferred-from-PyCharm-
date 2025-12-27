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
#time.sleep(5)

#Finding element for Schedule Courses
Schedule_Courses=driver.find_element(By.LINK_TEXT,value="Schedule Courses")

#To click the hyperlink Schedule Courses
Schedule_Courses.click()
time.sleep(3)
