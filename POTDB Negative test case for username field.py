from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("http://www.ezhrs.com/project1/potdb/login.asp")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME,value="username").send_keys("admin")
driver.find_element(By.NAME,value="password").send_keys("welcome")
driver.find_element(By.NAME,value="SUBMIT").click()
time.sleep(3)
#capturing full error message using selectorhub
errormsg=driver.find_element(By.XPATH,value="//tbody/tr/td/b[1]").text
print(errormsg)
extracted=errormsg[:18]
print(extracted)

if(extracted=='Incorrect Username'):
    print("Incorrect username entered, verification passed")
else:
    print("Test case failed")



