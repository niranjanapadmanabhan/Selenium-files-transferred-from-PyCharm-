from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
#LOGIN
driver = webdriver.Chrome()
driver.get("http://www.ezhrs.com/ezCourses/admin/admin.asp?action=admin")
driver.find_element(By.NAME, "uname").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("pass")
driver.find_element(By.NAME, "SUBMIT").click()
time.sleep(3)
driver.maximize_window()
#CLICK MANAGE COURSE BUTTON
driver.find_element(By.LINK_TEXT,value="Manage Courses").click()
time.sleep(3)
#SAVE THE NAME OF THE ACTIVE COURSE BY GETTING THE TEXT IN A VARIABLE AND PRINT IT
active_course=driver.find_element(By.LINK_TEXT,value="01111").text
print("The selected active course for adding students is:",active_course)
time.sleep(3)
#CLICK ADD STUDENT FOR THE FIRST SEEN 01111 ACTIVE COURSE
driver.find_element(By.XPATH,value="/html/body/table[2]/tbody[1]/tr/td/div/p/table[1]/tbody/tr[4]/td/div/table/tbody/tr[5]/td[7]/div/b/font/a/img").click()
time.sleep(3)
#SELECT 5 STUDENTS CHECKBOX
driver.find_element(By.NAME,value="CB_5").click()
driver.find_element(By.NAME,value="CB_4").click()
driver.find_element(By.NAME,value="CB_3").click()
driver.find_element(By.NAME,value="CB_2").click()
driver.find_element(By.NAME,value="CB_6").click()
time.sleep(3)
#CLICK REGISTER STUDENTS BUTTON
driver.find_element(By.NAME,value="submit")
time.sleep(3)
#TO GO BACK TO THE ACTIVE COURSES PAGE AFTER REGISTERING STUDENTS
driver.back()
time.sleep(3)
#SAVE THE NAME OF THE COURSE WHICH HAS STUDENT ADDED BY GETTING THE TEXT IN A VARIABLE AND PRINT IT
course_name=driver.find_element(By.LINK_TEXT,value="01111").text
time.sleep(5)
print("The course name which has 5 students added is:",course_name)
time.sleep(3)
if(active_course==course_name):
    print("Test case passed")
else:
    print("Test case failed")
driver.close()
