from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("http://www.ezhrs.com/project1/potdb/login.asp")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME,value="username").send_keys("admin.admin")
driver.find_element(By.NAME,value="password").send_keys("welcme")
driver.find_element(By.NAME,value="SUBMIT").click()
time.sleep(3)
#capturing full error message using selectorhub
errormsg=driver.find_element(By.XPATH,value="//tbody/tr/td/b[1]").text
print(errormsg)
extracted1=errormsg[:9]
#print("Printing extracted1:",extracted1)
extracted2=errormsg[26:]
#print("Printing extracted2:",extracted2)
extracted3=extracted2[:8]
#print("Printing extracted3:",extracted3)
extracted_and_combined=extracted1+" "+extracted3
print(extracted_and_combined)

if(extracted_and_combined=='Incorrect Password'):
    print("Incorrect password entered, verification passed")
else:
    print("Test case failed")

