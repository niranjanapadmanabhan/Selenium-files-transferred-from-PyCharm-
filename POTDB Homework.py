from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("http://www.ezhrs.com/project1/potdb/login.asp")
driver.find_element(By.NAME,value="username").send_keys("admin.admin")
uname=driver.find_element(By.NAME,value="username").get_attribute("value")
unameextracted=uname[0:5]
print(unameextracted)
driver.find_element(By.NAME,value="password").send_keys("welcome")
driver.find_element(By.NAME,value="SUBMIT").click()
cookie=driver.find_element(By.XPATH,value="/html/body/table[1]/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr[1]/td/table/tbody/tr/td/div/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td/b").text
print("Cookie is:",cookie)
cookieextracted=cookie[13:]
print("Cookie extracted is:",cookieextracted)
#compare cookie to username
if(unameextracted==cookieextracted):
    print("Test case passed")
else:
    print("Test case failed")
driver.quit()


