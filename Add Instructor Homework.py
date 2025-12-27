from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.get("http://ezhrs.com/project1/ezcourses/admin/admin.asp?action=admin")

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

time.sleep(3)

#Add Instructor
addinstructor=driver.find_element(By.LINK_TEXT,value="Instructor")
addinstructor.click()
time.sleep(4)

#Fill the form
fname=driver.find_element(By.NAME,value="fname")
fname.send_keys("Niranjana")
lastname=driver.find_element(By.NAME,value="lname")
lastname.send_keys("P")
time.sleep(4)
uname=driver.find_element(By.NAME,value="username")
uname.send_keys("Niranj")
email=driver.find_element(By.NAME,value="email")
email.send_keys("hithere@gmail.com")
time.sleep(4)
tel=driver.find_element(By.NAME,value="phone_code")
tel.send_keys("4165702899")
time.sleep(4)
#Click Add Instructor Button
buttonclick=driver.find_element(By.NAME,value="submit")
buttonclick.click()
time.sleep(4)