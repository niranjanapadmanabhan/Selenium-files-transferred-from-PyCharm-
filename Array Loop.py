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

#To click the hyperlink Create Courses
new_course=driver.find_element(By.LINK_TEXT,value="Create New Course")
new_course.click()
time.sleep(3)

ddm=Select(driver.find_element(By.NAME,value="Cat"))
#Looping i.e, verify drop down menu with options
for x in ddm.options:
    print(x.text)  # if text is not given , we will see message like webelement instead of actual options...so remember to use .text

print(len(ddm.options))
optionlength=len(ddm.options)

if(optionlength==5):
    print("Test case passed")
else:
    print("Test case failed")

    #Loop level ddm, print the length
    #Verify that the level has two options.
ddm1=Select(driver.find_element(By.NAME,value="course_Level"))
for x in ddm1.options:
    print(x.text)
leveloptions=len(ddm1.options)
print("Level drop down has",leveloptions,"options")

if(leveloptions==2):
    print("PASS")
else:
    print("FAIL")

