from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.get("http://www.ezhrs.com/ezCourses/admin/admin.asp?action=admin")

#Finding the element for username
username=driver.find_element(By.NAME,value="uname")
#Typing admin for username
username.send_keys("admina")

#Finding element for password
password=driver.find_element(By.NAME,value="password")
#Typing pass for password
password.send_keys("pass")

#Finding element for Login button
login=driver.find_element(By.NAME,value="SUBMIT")
#To click the button login
login.click()
time.sleep(5)
tryagain=driver.find_element(By.LINK_TEXT,value="Try again")
tryagain.click()
time.sleep(3)
#skip Username
username.clear()
time.sleep(5)
#password.send_keys("pass")  -> If I want to give password pass again, no need to repeat this step as pwd will already be shown..so either skip this step or clear first and add this step.
time.sleep(2)
login.click()
time.sleep(2)