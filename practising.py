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

#To click the hyperlink Schedule Courses
new_course=driver.find_element(By.LINK_TEXT,value="Create New Course")
new_course.click()
time.sleep(3)

ddm=driver.find_element(By.NAME,value="Cat")
ddm1=Select(ddm)
ddm1.select_by_index(3)

#Finding the element Title

Title=driver.find_element(By.NAME,value="Title")

Title.send_keys("Nir Course")
time.sleep(3)

#Finding the element Level
Level=driver.find_element(By.NAME,value="course_Level")

#Selecting from dropdown
ddm2=Select(Level)
ddm2.select_by_value("1")
time.sleep(3)

#Adding Description
Desc=driver.find_element(By.NAME,value="Description")
Desc.send_keys("1234")
time.sleep(3)

#Finding the element Certificate
cert=driver.find_element(By.NAME,value="Cert")
cert.click()
time.sleep(3)

#Finding element for Create Course button
create=driver.find_element(By.NAME,value="Submit")
create.click()
time.sleep(5)

coursename=driver.find_element(By.NAME,value="test course")
coursename.click()
time.sleep(5)
description==driver.find_element(By.NAME,value="Description")
description1=description.get_attribute("value")
if(description==Description):
    print("TC passed")
else:
    print("TC failed")