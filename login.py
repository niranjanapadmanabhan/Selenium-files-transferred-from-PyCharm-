import time


from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
#launch course management app
## at username field enter username admin
## at password field enter password pass
## click on login button
#verify main screen is displayed  -> means print the title and print and compare with that title

driver.get("http://www.ezhrs.com/ezCourses/admin/admin.asp?action=admin")
driver.find_element(By.NAME,value="uname").send_keys("admin")
driver.find_element(By.NAME,value="password").send_keys("pass")
driver.find_element(By.NAME,value="SUBMIT").click()
title=driver.title
print(title)

if(title=="Admin"):
    print("Test Case Passed")
else:
    print("Test Case Failed")
driver.find_element(By.LINK_TEXT, value="Schedule Courses").click()
#time.sleep(5)
driver.find_element(By.LINK_TEXT, value="Create New Course").click()

time.sleep(5)
ddm1=Select(driver.find_element(By.NAME,value="Cat"))
time.sleep(5)


#first way to select visible text
ddm1.select_by_visible_text("DB 101")
time.sleep(5)

#Select by index  ->fastly it will show Music and art
ddm1.select_by_index(3)
time.sleep(5)

#Select by value -> expand after inspecting the drop down and in options for qa test is value 1, also value is string so give 1 in quotes.
ddm1.select_by_value("1")
time.sleep(5)

#To do homework
#title
driver.find_element(By.NAME,value="Title").send_keys("Nir_Course")
time.sleep(5)
ddm2=Select(driver.find_element(By.NAME,value="course_Level"))


ddm2.select_by_value("1")
time.sleep(5)
