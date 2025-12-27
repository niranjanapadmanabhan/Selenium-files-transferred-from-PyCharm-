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

# Click on schedule course
#driver.find_element(By.XPATH,"//tbody/tr[3]/td[5]/div[1]/a[1]/img[1]").click()
#using absolute xpath (comment on other methods otherwise it will throw error, hence commenting out the first one.
driver.find_element(By.XPATH,"/html[1]/body[1]/table[2]/tbody[1]/tr[1]/td[1]/div[1]/p[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/table[2]/tbody[1]/tr[3]/td[5]/div[1]/a[1]/img[1]").click()

#Finding element for Instructor
instructor=driver.find_element(By.NAME,value="instructor")
ddm1=Select(instructor)
ddm1.select_by_index(3)

#Finding element for location
location=driver.find_element(By.NAME,value="ClassID")
ddm2=Select(location)
ddm2.select_by_index(2)

#Finding element for SelectOffice
office=driver.find_element(By.NAME,value="OfficeID")
ddm2=Select(office)
ddm2.select_by_index(5)

#Finding element for Date
Date=driver.find_element(By.NAME,value="firstinput")
Date.send_keys("2024/07/25")

#Finding element for StartTime
StartTime=driver.find_element(By.NAME,value="mTime")
ddm3=Select(StartTime)
ddm3.select_by_index(3)
time.sleep(3)

#Finding element for Duration
Duration=driver.find_element(By.NAME,value="duration")
ddm4=Select(Duration)
ddm4.select_by_index(1)
time.sleep(3)

#Finding element for CourseCapacity
CCapacity=driver.find_element(By.NAME,value="Limit")
ddm5=Select(CCapacity)
ddm5.select_by_index(3)
time.sleep(3)

#Finding element for Schedule Button and click it
Schedule=driver.find_element(By.XPATH ,value="//tbody/tr[1]/td[2]/input[1]")
Schedule.click()
time.sleep(2)

driver.get("http://www.ezhrs.com/ezCourses/admin/course_manager.asp?action=active")

Active_Courses=driver.find_element(By.CSS_SELECTOR,"tr:nth-child(1) td:nth-child(1) div:nth-child(1) a:nth-child(1) > b:nth-child(1)")

#To click the hyperlink Schedule Courses
Active_Courses.click()
time.sleep(3)