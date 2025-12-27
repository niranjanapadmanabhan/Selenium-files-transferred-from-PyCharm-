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
username.get_attribute("value")
print(username)

#Finding element for password
password=driver.find_element(By.NAME,value="password")
#Typing pass for password
password.send_keys("pass")

#cookie=driver.find_element(By.LINK_TEXT,value="Welcome: Administrator").text
 #This will grab the text Welcome Administrator seen on top right of the screen
#Now we can put it in a variable for comparing
#print(cookie)
#time.sleep(4)