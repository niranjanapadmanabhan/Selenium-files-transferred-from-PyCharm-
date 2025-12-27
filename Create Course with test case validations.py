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

Title.send_keys("MyCourse5")

#Finding the element Level
Level=driver.find_element(By.NAME,value="course_Level")

#Selecting from dropdown
ddm2=Select(Level)
ddm2.select_by_value("1")
time.sleep(3)

#Adding Description
Desc=driver.find_element(By.NAME,value="Description")
Desc.send_keys("1234")
Desc1=Desc.get_attribute('value')
print("Description added before is:",Desc1)
time.sleep(3)

#Finding the element Certificate
cert=driver.find_element(By.NAME,value="Cert")
cert.click()
time.sleep(3)

#Finding element for Create Course button
create=driver.find_element(By.NAME,value="Submit")
create.click()
time.sleep(5)
#After clicking the submit button , the course will be created. We will still be in the Schedule Courses page but the new course will be seen as added which is hyperlinked.
#Now  click the newly added course as below:
driver.find_element(By.LINK_TEXT,value="MyCourse5").click()
time.sleep(10)
#After clicking, get the description text box value which should then be compared with Desc1
Desc2=driver.find_element(By.NAME,value="Description").get_attribute("value")
print("Description seen now is:",Desc2,"which matches with the Description added before:",Desc1)
if(Desc2==Desc1):
    print("Test Case Passed")
else:
    print("Test Case Failed")

