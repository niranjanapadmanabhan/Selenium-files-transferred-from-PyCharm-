#create script for entering wrong username and verifying it
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
#Loop wrong username 5 times and verify error msg
for x in range(1,6):
    driver = webdriver.Chrome()
    driver.get("http://www.ezhrs.com/ezCourses/admin/admin.asp?action=admin")
    driver.find_element(By.NAME, "uname").send_keys("admins")
    driver.find_element(By.NAME, "password").send_keys("pass")
    driver.find_element(By.NAME, "SUBMIT").click()
    time.sleep(3)
    driver.maximize_window()

#error message
    error=driver.find_element(By.LINK_TEXT,value="Try again").text
    print(error)
    if(error=="Try again"):
        print("Test case passed")
    else:
        print("Test case failed")
#Click the Try again button
    driver.find_element(By.LINK_TEXT,value="Try again").click()
    time.sleep(3)
    driver.find_element(By.NAME,value="uname").clear()